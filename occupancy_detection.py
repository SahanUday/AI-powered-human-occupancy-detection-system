import requests
import cv2
import numpy as np
from keras.models import load_model
import time
import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ====== Configuration ======
ESP32_CAM_IP = os.getenv('ESP32_CAM_IP', '192.168.1.100')
ESP32_CAM_PORT = os.getenv('ESP32_CAM_PORT', '80')
ESP32_CAM_URL = f'http://{ESP32_CAM_IP}:{ESP32_CAM_PORT}/capture'
MODEL_PATH = os.getenv('MODEL_PATH', 'human_classifier.keras')
DETECTION_INTERVAL = int(os.getenv('DETECTION_INTERVAL', '5'))
THRESHOLD = float(os.getenv('THRESHOLD', '0.5'))
FIREBASE_SERVICE_ACCOUNT_FILE = os.getenv('FIREBASE_SERVICE_ACCOUNT_FILE', 'firebase-service-account.json')
FIREBASE_DB_URL = os.getenv('FIREBASE_DB_URL', 'https://your-project-default-rtdb.region.firebasedatabase.app/')

# ====== Setup ======
# Load ML model
print("[INFO] Loading model...")
model = load_model(MODEL_PATH)

# Initialize Firebase
print("[INFO] Initializing Firebase...")
try:
    cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_FILE)
    firebase_admin.initialize_app(cred, {
        'databaseURL': FIREBASE_DB_URL
    })
    firebase_initialized = True
    print("[INFO] Firebase initialized successfully.")
except Exception as e:
    print(f"[ERROR] Firebase initialization failed: {e}")
    firebase_initialized = False

# ====== Detection Loop ======
print("[INFO] Starting real-time detection...")
while True:
    try:
        # Step 1: Fetch image from ESP32-CAM
        response = requests.get(ESP32_CAM_URL, timeout=5)
        if response.status_code == 200:
            print("[INFO] Image captured successfully")

            # Step 2: Decode image from response (in-memory)
            image_data = np.frombuffer(response.content, np.uint8)
            img = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
            if img is None:
                print("[WARNING] Failed to decode image.")
                continue

            # Step 3: Preprocess image
            img_resized = cv2.resize(img, (224, 224)) / 255.0
            img_batch = np.expand_dims(img_resized, axis=0)

            # Step 4: Predict
            prediction = model.predict(img_batch)[0][0]

            # Step 5: Determine result
            occupancy_status = "occupied" if prediction > THRESHOLD else "not_occupied"
            print(f"{'✅' if occupancy_status == 'occupied' else '❌'} {occupancy_status.capitalize()}")

            # Step 6: Update Firebase
            if firebase_initialized:
                try:
                    db.reference("sensor_data/occupancy").set(occupancy_status)
                    print(f"[FIREBASE] Updated occupancy: {occupancy_status}")
                except Exception as firebase_err:
                    print(f"[FIREBASE ERROR] {firebase_err}")

        else:
            print(f"[ERROR] Failed to fetch image, status code: {response.status_code}")

    except Exception as e:
        print(f"[ERROR] Exception: {e}")

    # Wait before next capture
    time.sleep(DETECTION_INTERVAL)
