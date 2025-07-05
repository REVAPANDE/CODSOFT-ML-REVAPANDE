import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Page config
st.set_page_config(page_title="Credit Card Fraud Detection", page_icon="💳", layout="centered")

# Styling
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    footer {
        visibility: hidden;
    }
    .footer-text {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        font-size: 0.9rem;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.title("💳 Credit Card Fraud Detection")
st.markdown("Upload transaction data and detect fraudulent activities in real-time with machine learning.")

# File uploader
uploaded_file = st.file_uploader("📁 Upload a CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)

    st.subheader("🔎 Preview of Uploaded Data")
    st.dataframe(data.head())

    # Apply scaling on Amount and Time if present
    if 'Amount' in data.columns and 'Time' in data.columns:
        data[['scaled_amount', 'scaled_time']] = scaler.transform(data[['Amount', 'Time']])
        data = data.drop(['Amount', 'Time'], axis=1)

    if 'Class' in data.columns:
        data = data.drop('Class', axis=1)

    # Prediction
    predictions = model.predict(data)
    data['Prediction'] = predictions

    # Show results
    st.subheader("📊 Prediction Results")
    st.dataframe(data[['Prediction']])

    frauds = data['Prediction'].sum()
    st.success(f"🚨 Detected {frauds} fraudulent transaction(s)")

st.markdown("</div>", unsafe_allow_html=True)

# Custom footer with Reva Pande branding
st.markdown("""
<div class="footer-text">
    Made with ❤️ by <strong>Reva Pande</strong> | Credit Card Fraud Detection App
</div>
""", unsafe_allow_html=True)
