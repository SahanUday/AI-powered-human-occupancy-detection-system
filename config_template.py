# Configuration file for sensitive data
# Copy this file to config.py and fill in your actual values

# ESP32-CAM Configuration
ESP32_CAM_IP = "192.168.x.x"  # Replace with your ESP32-CAM IP address
ESP32_CAM_PORT = "80"  # Default port, change if needed

# Firebase Configuration
FIREBASE_SERVICE_ACCOUNT_FILE = "path/to/your/firebase-service-account.json"
FIREBASE_DB_URL = "https://your-project-default-rtdb.region.firebasedatabase.app/"

# Model Configuration
MODEL_PATH = "human_classifier.keras"
DETECTION_INTERVAL = 5  # seconds
THRESHOLD = 0.5  # Detection threshold (0.0 to 1.0)
