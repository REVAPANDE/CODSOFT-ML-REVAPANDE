import streamlit as st
import pickle

# Load the model and vectorizer
with open('genre_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

# App design
st.set_page_config(page_title="Movie Genre Classifier", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #e91e63;'>🎬 Movie Genre Predictor</h1>
    <p style='text-align: center;'>A machine learning app by <strong>Reva Pande</strong></p>
""", unsafe_allow_html=True)

plot = st.text_area("✏️ Enter a movie plot summary:")

if st.button("🔮 Predict Genre"):
    if plot.strip() != "":
        transformed = vectorizer.transform([plot])
        prediction = model.predict(transformed)
        st.success(f"🎯 Predicted Genre: **{prediction[0]}**")
    else:
        st.warning("Please enter a plot!")
