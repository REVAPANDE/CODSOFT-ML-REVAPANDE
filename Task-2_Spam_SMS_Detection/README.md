# 📱 Spam SMS Detection App

An intelligent text classification tool that identifies whether an SMS message is **spam** or **legitimate** using machine learning.

🔗 **Live App**: [spam-sms-detection-app-by-revapande.streamlit.app](https://spam-sms-detection-app-by-revapande.streamlit.app/)

---

## 🎯 Objective

The goal of this project is to automatically detect spam messages using NLP techniques and machine learning, trained on the popular **SMS Spam Collection Dataset** from Kaggle.

---

## 🚀 Features

- ✍️ **Single Message Detection** – Instantly check if a typed message is spam.
- 📁 **Bulk CSV Upload** – Upload a file with multiple messages for batch classification.
- 📥 **Downloadable Results** – Get the predictions back in a CSV file.
- 🎨 **Branded UI** – Clean interface with “Made with ❤️ by Reva Pande”.

---

## 🧠 Model Details

- **Text Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Classifier**: Support Vector Machine (SVM)
- **Accuracy**: ~98% on test data

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Pandas
- Joblib
- Streamlit

---

## 📂 Sample CSV Format
![Screenshot 2025-07-04 174523](https://github.com/user-attachments/assets/e63f495b-16ea-4343-a8fe-7f824aa51247)


```csv
message
Congratulations! You’ve won a free iPhone. Claim now.
Hey, are we still on for dinner?
Your KYC is pending. Click this link to verify now.
