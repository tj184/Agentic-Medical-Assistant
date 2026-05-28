import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🩺 AI Diagnosis")

patient_text = st.text_area(
    "Enter Patient Symptoms"
)

medicines = st.text_input(
    "Medicines (comma separated)"
)

token = st.text_input(
    "JWT Token",
    type="password"
)

if st.button("Generate Diagnosis"):

    medicine_list = [
        med.strip()
        for med in medicines.split(",")
        if med.strip()
    ]

    payload = {
        "symptoms": patient_text.split(","),
        "medicines": medicine_list
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        f"{API_URL}/diagnosis/",
        json=payload,
        headers=headers
    )

    result = response.json()

    st.subheader("Diagnosis Result")

    st.json(result)