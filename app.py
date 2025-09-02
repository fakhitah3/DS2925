import streamlit as st

# App title
st.title("My First Streamlit App")

# Add some text
st.write("Hello! 👋 This is a simple Streamlit app.")

# Input from user
name = st.text_input("Enter your name:")

# Button
if st.button("Greet Me"):
    st.success(f"Hello, {name}! Welcome to Streamlit 🚀")
