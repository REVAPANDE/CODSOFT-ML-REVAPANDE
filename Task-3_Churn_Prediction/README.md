# 💼 Bank Customer Churn Prediction

This project helps banks and subscription-based services predict whether a customer is likely to leave (churn) using demographic and behavioral data.

---

## 🎯 Objective

Predict customer churn based on:
- Age, Gender, Geography
- Account Balance, Credit Score
- Tenure, Number of Products
- Active Membership, Salary, and more

**Target:**  
`Exited` → 1 = Churned, 0 = Retained

---

## 🚀 Features

- 📁 Upload customer data in CSV format
- 🔮 Real-time churn prediction
- 📊 Downloadable prediction results
- 🎨 Clean, branded UI with a footer: _"Made with ❤️ by Reva Pande"_

---


 Input Format
 ![Screenshot 2025-07-05 134137](https://github.com/user-attachments/assets/06f9fe22-6f17-459d-a978-12dd010d8184)


Your input CSV should look like this:

```csv
CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary
650,France,Female,35,5,50000.0,2,1,1,60000.0
720,Germany,Male,45,10,150000.0,1,0,0,120000.0
580,Spain,Female,30,3,0.0,1,1,1,45000.0
