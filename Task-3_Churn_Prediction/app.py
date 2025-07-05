import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

# App title
st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("💼 Bank Customer Churn Prediction")
st.markdown("Upload customer data to predict who might churn.")

# Upload section
uploaded_file = st.file_uploader("📁 Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Basic check
    if 'Exited' in df.columns:
        df.drop(columns=['Exited'], inplace=True)

    # Encoding (assuming input has 'Geography' and 'Gender')
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    df = pd.get_dummies(df, columns=['Geography'], drop_first=True)

    # Ensure all required columns exist
    required_cols = ['CreditScore', 'Gender', 'Age', 'Tenure', 'Balance',
                     'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
                     'Geography_Germany', 'Geography_Spain']

    for col in required_cols:
        if col not in df.columns:
            df[col] = 0

    # Reorder columns
    df = df[required_cols]

    # Scale the data
    df_scaled = scaler.transform(df)

    # Predict
    predictions = model.predict(df_scaled)

    # Output results
    result_df = pd.DataFrame(df)
    result_df['Churn_Predicted'] = predictions
    result_df['Churn_Predicted'] = result_df['Churn_Predicted'].map({0: "No", 1: "Yes"})

    st.success("✅ Predictions complete!")
    st.dataframe(result_df)

    churn_count = (predictions == 1).sum()
    st.write(f"🔍 **{churn_count} customers are likely to churn**.")

    st.download_button("📥 Download Results as CSV", result_df.to_csv(index=False), file_name="churn_predictions.csv")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 14px;'>Made with ❤️ by <b>Reva Pande</b></div>", unsafe_allow_html=True)

