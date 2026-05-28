import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("📁 Patient History")

patient_id = st.number_input(
    "Enter Patient ID",
    min_value=1
)

token = st.text_input(
    "JWT Token",
    type="password"
)

if st.button("Fetch Patient"):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{API_URL}/patients/{patient_id}",
        headers=headers
    )

    result = response.json()

    st.json(result)