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


