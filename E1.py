import streamlit as st

# Page tittle
st.title("Simple Input GUI")

# Question
st.write("What is your name?")

# Input box
name = st.text_input("Enter your name: ")

# Button
if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! Welcome to Streamlit.")
    else:
        st.warning("Please enter your name.")