import streamlit as st
import joblib
import pandas as pd

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Page config
st.set_page_config(page_title="Spam SMS Detector", layout="centered")
st.title("📱 SMS Spam Detection")
st.markdown("Enter a message or upload a file to check for spam.")

# Single message prediction
st.subheader("🔍 Predict a Single Message")
user_input = st.text_area("Type your SMS message here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        message_vector = vectorizer.transform([user_input])
        prediction = model.predict(message_vector)[0]
        label = "🚫 Spam" if prediction == 1 else "✅ Legitimate"
        st.success(f"**Prediction:** {label}")

# Bulk prediction
st.subheader("📁 Upload CSV for Bulk Prediction")
csv_file = st.file_uploader("Upload a CSV with a `message` column", type=["csv"])

if csv_file is not None:
    try:
        df = pd.read_csv(csv_file)
        if 'message' not in df.columns:
            st.error("❌ CSV must contain a 'message' column.")
        else:
            message_vectors = vectorizer.transform(df['message'])
            predictions = model.predict(message_vectors)
            df['Prediction'] = ["Spam" if p == 1 else "Legit" for p in predictions]
            st.success("✅ Predictions complete!")
            st.dataframe(df)

            # Download button
            st.download_button("📥 Download Results", df.to_csv(index=False), file_name="spam_predictions.csv")
    except Exception as e:
        st.error(f"❌ Error reading CSV: {e}")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center;'>Made with ❤️ by <b>Reva Pande</b></div>", unsafe_allow_html=True)
