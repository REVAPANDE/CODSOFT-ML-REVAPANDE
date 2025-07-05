# 💳 Credit Card Fraud Detection App

A machine learning web application that detects fraudulent credit card transactions based on transaction patterns. This app is trained on real anonymized data and built with an aesthetic and branded UI using Streamlit.

🔗 **Live App**: [credit-card-fraud-detection-by-revapande.streamlit.app](https://credit-card-fraud-detection-by-revapande.streamlit.app/)

---

## 🚀 Features

- 📁 Upload your own transaction CSV file
- 🔍 Real-time fraud predictions
- 📊 Prediction summary with fraud count
- 🎨 Clean UI with personalized footer by **Reva Pande**
- 🧠 Built using a trained Random Forest Classifier

---

## 🧠 Model Info

- Algorithm: Random Forest Classifier  
- Preprocessing: Scaled `Amount` and `Time` features  
- Evaluation: ROC-AUC, Confusion Matrix, Classification Report

---

## 📂 Sample Input Format

To make predictions, your CSV should contain 30 columns:
- `V1` to `V28` (PCA-transformed features)
- `scaled_amount`, `scaled_time` (scaled numeric features)
![Screenshot 2025-07-04 153209](https://github.com/user-attachments/assets/f8f2e92b-0667-47ea-8299-de398e4e5372)

Example:
```csv
V1,V2,...,V28,scaled_amount,scaled_time
-1.3598,-0.0728,...,-0.0210,-0.5132,1.2326

