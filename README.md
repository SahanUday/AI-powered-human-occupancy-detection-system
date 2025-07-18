# 🕵️‍♂️ AI-Powered Human Occupancy Detection System

This project is an **AI-powered human occupancy detection system** that integrates an **ESP32-CAM module**, a **TensorFlow-based human detection model**, and **Firebase Realtime Database (RTDB)** for real-time occupancy monitoring. It captures images using the ESP32-CAM, processes them with a trained AI model to detect human presence, and updates the occupancy status in Firebase RTDB.

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

> ![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=FFFF00)
> ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?logo=tensorflow&logoColor=white)
> ![OpenCV](https://img.shields.io/badge/OpenCV-%235C3EE8.svg?logo=opencv&logoColor=white)
> ![Firebase](https://img.shields.io/badge/Firebase-%23FFCA28.svg?logo=firebase&logoColor=black)
> ![ESP32](https://img.shields.io/badge/ESP32-%23000000.svg?logo=espressif&logoColor=white)

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

* **Hardware**:
  * ESP32-CAM module with configured firmware for image capture.
* **Software**:
  * Python 3.8+
  * TensorFlow: `pip install tensorflow`
  * OpenCV: `pip install opencv-python`
  * Requests: `pip install requests`
  * Firebase Admin SDK: `pip install firebase-admin`
* **Firebase Setup**:
  * A Firebase project with Realtime Database enabled.
  * Service account JSON file (e.g., `airvix-ef027-firebase-adminsdk-fbsvc-18f86681a5.json`).
* **ESP32-CAM Setup**:
  * Configured ESP32-CAM with a static IP address (e.g., `192.168.8.144`).

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
git clone https://github.com/<your-username>/human-occupancy-detection.git
cd human-occupancy-detection
```

**2. Install Dependencies**:
```bash
pip install -r requirements.txt
```

**3. Train the Model** (if not already trained):
```bash
python train_model.py
```

**4. Run the Detection Script**:
```bash
python occupancy_detection.py
```

---

## 📂 Project Structure

```
human-occupancy-detection/
├── classification_data/        # Dataset for training (human/ and no_human/ subfolders)
├── train_model.py             # Script for training the human detection model
├── occupancy_detection.py     # Main script for real-time detection and Firebase updates
├── human_classifier.keras     # Trained model file
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── <service_account>.json     # Firebase service account JSON file
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

Fork the repo, create a feature branch, and submit a pull request!

---

## 🛠 Built With

* 🐍 Python 3.8+ – Core programming language.
* 🧠 TensorFlow/Keras – For the human detection model.
* 📸 OpenCV – For image processing.
* 🔥 Firebase Admin SDK – For real-time database updates.
* 🌐 ESP32-CAM – For image capture.

---

## 📜 License

This project is licensed under the MIT License.
