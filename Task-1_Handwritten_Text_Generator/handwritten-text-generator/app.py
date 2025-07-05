import streamlit as st

st.set_page_config(page_title="Handwritten Text Generator")

# Title and instructions
st.title("🖋️ Handwritten Text Generator")
st.write("Type something below, and we'll display it in a handwriting-like style.")

# Text input
user_input = st.text_input("Enter your text:")

# Show result using simple HTML font
if user_input:
    st.markdown(f"""
    <h2 style='font-family: "Comic Sans MS", cursive, sans-serif;
                font-size: 36px;
                color: #444;
                border: 2px dashed #aaa;
                padding: 15px;
                border-radius: 10px;
                background-color: #f0f0f0;
                text-align: center;'>
        {user_input}
    </h2>
    """, unsafe_allow_html=True)


