# 💳 Credit Card Fraud Detection App

A machine learning web application that detects fraudulent credit card transactions based on transaction patterns. This app is trained on real anonymized data and built with an aesthetic and branded UI using Streamlit.

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
![Screenshot 2025-07-05 134125](https://github.com/user-attachments/assets/1415c851-83df-489f-a4f3-009b94f98b86)

To make predictions, your CSV should contain 30 columns:
- `V1` to `V28` (PCA-transformed features)
- `scaled_amount`, `scaled_time` (scaled numeric features)


Example:
```csv
V1,V2,...,V28,scaled_amount,scaled_time
-1.3598,-0.0728,...,-0.0210,-0.5132,1.2326

