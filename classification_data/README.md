# Classification Dataset

## 📊 Person vs No Person Dataset

This folder contains the training dataset for the human occupancy detection model.

### 🔗 Dataset Source
**Kaggle Dataset**: [Person vs No Person Dataset](https://www.kaggle.com/datasets/sahanudayanga/person-vs-no-person-dataset)

### 📁 Folder Structure
```
classification_data/
├── human/          # Images containing people
├── no_human/       # Images without people
└── README.md       # This file
```

### 🎯 Dataset Purpose
- **Objective**: Binary classification for human occupancy detection
- **Classes**: 
  - `human` - Images with people present
  - `no_human` - Images without people
- **Use Case**: Training a MobileNetV2-based model to detect human presence

### 📥 How to Download
1. Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/sahanudayanga/person-vs-no-person-dataset)
2. Create a Kaggle account if you don't have one
3. Download the dataset
4. Extract the files to this `classification_data/` directory
5. Ensure the folder structure matches the above layout

### 🔧 Usage
Once the dataset is downloaded and extracted:
```bash
# Train the model using this dataset
python train_model.py
```

### 📊 Dataset Statistics
- **Format**: Image files (JPG/PNG)
- **Classes**: 2 (binary classification)
- **Structure**: Organized in separate folders by class
- **Purpose**: Training data for human detection model

### ⚠️ Important Notes
- This folder should contain the actual image files after downloading from Kaggle
- The dataset is not included in the Git repository due to size constraints
- Make sure to download the dataset before training the model
- The folder structure must match the expected format for the training script to work properly