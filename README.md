# 🚨 Intrusion Detection System (IDS) using NSL-KDD & Stacking Ensemble

This project implements a **Machine Learning–based Intrusion Detection System (IDS)** trained on the **NSL-KDD dataset**.  
It uses a **Stacking Ensemble Model** (Random Forest + Gradient Boosting + SVM + Logistic Regression) to classify traffic as **Attack** or **Benign**.

The system includes:

- 🔍 **ML Pipeline**: preprocessing, feature engineering, model training  
- 🤖 **Stacking Ensemble Classifier**  
- 🌐 **Flask API for real-time predictions**  
- 📊 **Interactive Dashboard** (HTML/CSS/JS) for visualizing attack patterns  
- 📁 Organized folder structure for datasets, models, notebooks, and API service

---

## 📌 **Project Features**

### 🧠 Machine Learning
- Complete preprocessing: encoding, scaling, feature selection  
- Trained on the NSL-KDD dataset  
- Stacking model combining:
  - Random Forest  
  - Gradient Boosting  
  - Support Vector Machine  
  - Logistic Regression  
- Achieved **~96% accuracy**

### 🌐 Flask API
- Exposes a `/predict` endpoint  
- Accepts input as JSON and returns intrusion classification  
- Suitable for real-time or batch processing

### 📊 Dashboard
- Custom-built monitoring dashboard  
- Attack type distribution  
- Precision/Recall comparison  
- Location-wise attack visualization  
- Real-time logs (prototype)

---

## 📂 **Project Structure**
IDS_project/
│── api/
│ └── app.py # Flask API
│
│── models/
│ ├── stacking_model.pkl # Trained Stacking Model
│ └── scaler.pkl # Preprocessing scaler
│
│── data/
│ ├── KDDTrain+.csv
│ └── KDDTest+.csv
│
│── src/
│ ├── preprocessing.py
│ ├── train_model.py
│ └── evaluate.py
│
│── notebooks/
│ └── NSL_KDD_Analysis.ipynb
│
│── dashboard/
│ ├── templates/
│ └── static/
│
├── requirements.txt
└── README.md
🚀 How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Flask API
cd api
python app.py


API will start at:

http://127.0.0.1:5000/predict

3️⃣ Send a Test Request

Example JSON:

{
  "duration": 0,
  "protocol_type": "tcp",
  "src_bytes": 181,
  "dst_bytes": 5450,
  "flag": "SF"
}

🎯 Model Performance
Metric	Score
Accuracy	96%
Precision	High
Recall	High
F1-Score	Excellent
🛠️ Tech Stack

Python

Pandas, NumPy, Scikit-Learn

Flask

Matplotlib, Seaborn

HTML, CSS, JavaScript

Jupyter Notebook

🤝 Contributions

Pull requests and suggestions are welcome.

📧 Contact

Aishwarya Satyappanmath
GitHub: https://github.com/aishwarya937
Email: aishwaryasattyappanamath@gmail.com


