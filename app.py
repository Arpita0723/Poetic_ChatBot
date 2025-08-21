import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit App
st.set_page_config(page_title="Poetic Chatbot", page_icon="🌸")

st.title("🌸 Poetic Personality Chatbot")
st.write("Talk with me, and I'll reply in poetic verses ✨")


genai.configure(api_key="AIzaSyBRWvtfFkZ0ypr-_ELo4yGxzVleUjUBMVA")
model = genai.GenerativeModel("gemini-1.5-flash")
# Chat input
user_input = st.text_input("You:", "")

if user_input:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        f"Write a short poem in a lyrical style based on this: {user_input}"
    )
    st.markdown(f"**Poet:** {response.text}")
