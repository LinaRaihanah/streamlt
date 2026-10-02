import streamlit as st

st.title("My first Streamlit app by amalina")

st.write ("Hello! This is my first streamlit application.")

name = st.text_input("Enter your name:")

if name :
    st.success("Hello " + name + "!")