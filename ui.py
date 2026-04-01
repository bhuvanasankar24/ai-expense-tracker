import streamlit as st
import requests

BASE_URL="http://127.0.0.1:5000"

st.title("AI Implemented Expense Tracker")

st.header("Add Expense")

amount = st.number_input("Amount", min_value=0.0)
category = st.text_input("Category")
description= st.text_input("Description")

if st.button("Add Expense"):
    requests.post(f"{BASE_URL}/expenses", json={
        "amount":amount,
        "category":category,
        "description": description
    })
    st.success("Added successfully!")

st.header("AI Category Predictor")

description=st.text_input("Enter Description")

if st.button("Predict Category"):
    res = requests.post(f"{BASE_URL}/predict", json={
        "description": description
    })
    data = res.json()
    st.write(data)
    if "predicted_category" in data:
        st.success(data["predicted_category"])
    else:
        st.error(f"Error: {data}")

if st.button("Show Expenses"):
    res = requests.get(f"{BASE_URL}/expenses")
    st.json(res.json())