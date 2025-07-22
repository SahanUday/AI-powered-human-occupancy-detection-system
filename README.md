# 🕵️‍♂️ AI-Powered Human Occupancy Detection System

**AI-Powered Human Occupancy Detection System** is an intelligent system that detects human presence using machine learning, real-time image capture, and Firebase integration. Developed in Python, it leverages the ESP32-CAM for image capture, a TensorFlow-based MobileNetV2 model for human detection, and Firebase Realtime Database (RTDB) for real-time occupancy updates. This project is part of a broader system for smart space management, such as the **Smart-AC-Control-System**, which includes features like temperature prediction and automated control. For more details, visit the main repository at [Smart-AC-Control-System](https://github.com/SahanUday/Smart-AC-Control-System.git).

---

## 📌 Overview

The **Human Occupancy Detection System** is designed to:

* Capture images using an **ESP32-CAM module**.
* Process images with a **MobileNetV2-based AI model** to detect human presence.
* Update occupancy status ("occupied" or "not_occupied") in **Firebase RTDB**.
* Run continuously with configurable detection intervals.

This system is ideal for applications like smart home automation, security monitoring, or space management.

---

## 🔍 Key Features

* 📸 **ESP32-CAM Integration**: Captures images from the ESP32-CAM module over HTTP.
* 🧠 **AI-Powered Detection**: Uses a pre-trained MobileNetV2 model for accurate human detection.
* 🔥 **Firebase RTDB**: Stores real-time occupancy status for remote monitoring.
* ⏱️ **Configurable Interval**: Adjust detection frequency via a configurable interval.
* ✅ **Robust Error Handling**: Handles network failures and image processing errors gracefully.
* 🖼️ **Image Preprocessing**: Resizes and normalizes images for model compatibility.

---

## 🔧 Technologies & Tools Used

* **Python 3.8+** – Core programming language for AI and Firebase integration.
* **TensorFlow/Keras** – For training and deploying the human detection model.
* **OpenCV** – For image capture and preprocessing.
* **Firebase Admin SDK** – For real-time database updates.
* **ESP32-CAM** – Hardware for image capture.
* **Requests** – For fetching images from the ESP32-CAM HTTP server.
* **Python-dotenv** – For secure environment variable management.

> ![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=FFFF00)
> ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?logo=tensorflow&logoColor=white)
> ![OpenCV](https://img.shields.io/badge/OpenCV-%235C3EE8.svg?logo=opencv&logoColor=white)
> ![Firebase](https://img.shields.io/badge/Firebase-%23FFCA28.svg?logo=firebase&logoColor=black)
> ![ESP32](https://img.shields.io/badge/ESP32-%23000000.svg?logo=espressif&logoColor=white)

---

## 📊 Dataset

The machine learning model was trained on the **Person vs No Person Dataset** from Kaggle:

| Feature         | Description                              |
|-----------------|------------------------------------------|
| `image`         | Image captured by ESP32-CAM (224x224)    |
| `label`         | Binary label (human/no_human)            |

- **Dataset Link**: [Person vs No Person Dataset](https://www.kaggle.com/datasets/sahanudayanga/person-vs-no-person-dataset)
- **Structure**: 
  - `human/` - Images containing people
  - `no_human/` - Images without people
- **Purpose**: Binary classification for human occupancy detection
- **Usage**: Download and extract to `classification_data/` folder for training

---

## ⚙️ How It Works

1. **Image Capture**: The ESP32-CAM captures images and serves them via an HTTP endpoint.
2. **Image Preprocessing**: Images are fetched, decoded, resized to 224x224, and normalized.
3. **AI Prediction**: The pre-trained MobileNetV2 model predicts human presence (binary classification: occupied/not_occupied).
4. **Threshold Check**: A prediction threshold (e.g., 0.5) determines the occupancy status.
5. **Firebase Update**: The occupancy status is updated in Firebase RTDB.
6. **Loop**: The process repeats at a specified interval (e.g., every 5 seconds).

---

## 🧰 Setup & Run Guide

### ✅ Requirements

- Python 3.8+
- All dependencies listed in `requirements.txt`
- Firebase Admin SDK credentials
- Configured ESP32-CAM with a static IP address

---

### 🔐 Configuration

1. **Firebase Setup**:
   * Create a Firebase project and enable Realtime Database.
   * Download the service account JSON file and place it in the project directory.
   * Update the `SERVICE_ACCOUNT_FILE` and `FIREBASE_DB_URL` in `occupancy_detection.py`.

2. **ESP32-CAM Setup**:
   * Flash the ESP32-CAM with firmware to serve images via HTTP.
   * Update the `ESP32_CAM_URL` in `occupancy_detection.py` with your ESP32-CAM’s IP address.

3. **Model Training**:
   * Prepare a dataset in `classification_data` with two subfolders: `human` and `no_human`.
   * Run the training script (`train_model.py`) to generate `human_classifier.keras`.

---

### 🚀 Run the Project Locally

**1. Clone the Repository**:
```bash
git clone https://github.com/SahanUday/AI-powered-human-occupancy-detection-system.git
cd AI-powered-human-occupancy-detection-system
```

**2. Install Dependencies**:
```bash
pip install -r requirements.txt
```

**3. Configure Environment**:
```bash
# Edit .env with your actual values
# ESP32_CAM_IP=192.168.1.100
# FIREBASE_SERVICE_ACCOUNT_FILE=your-firebase-service-account.json
# etc.
```

**4. Prepare Dataset**:
```bash
# Download the dataset from Kaggle
```
*Dataset Link*: [Person vs No Person Dataset](https://www.kaggle.com/datasets/sahanudayanga/person-vs-no-person-dataset)

**5. Train the Model** (if not already trained):
```bash
python train_model.py
```

**6. Run the Detection Script**:
```bash
python occupancy_detection.py
```

---

## 📂 Project Structure

```
human-occupancy-detection/
├── classification_data/        # Dataset from Kaggle (see classification_data/README.md)
│   ├── human/                  # Images containing people
│   ├── no_human/               # Images without people
│   └── README.md               # Dataset documentation and download instructions
├── train_model.py             # Script for training the human detection model
├── occupancy_detection.py     # Main script for real-time detection and Firebase updates
├── human_classifier.keras     # Trained model file
├── requirements.txt           # Python dependencies
├── .env.example               # Environment variables template
├── config_template.json       # Template for Firebase service account
├── .gitignore                 # Git ignore file for security
└── README.md                  # Project documentation
```

---

## 🧪 Demo

The system continuously captures images, detects human presence, and updates Firebase RTDB. Example output:
```
[INFO] Image captured successfully
✅ Occupied
[FIREBASE] Updated occupancy: occupied
```

> 🧠 The system is designed for real-time monitoring and can be extended for IoT applications!

---

## 🤝 Contribution

We welcome contributions to enhance the project, such as:
* 📈 Improving model accuracy with additional data or fine-tuning.
* 🖼️ Adding image logging for debugging.
* 🔧 Supporting multiple ESP32-CAM modules.
* 🔔 Adding notifications for occupancy changes.
* 📊 Enhancing the dataset with more diverse images.

Fork the repo, create a feature branch, and submit a pull request!

---

## 🛠 Built With

* 🐍 Python 3.8+ – Core programming language.
* 🧠 TensorFlow/Keras – For the human detection model.
* 📸 OpenCV – For image processing.
* 🔥 Firebase Admin SDK – For real-time database updates.
* 🌐 ESP32-CAM – For image capture.
* 🔧 Python-dotenv – For secure environment configuration.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
