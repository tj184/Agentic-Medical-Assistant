import streamlit as st

st.set_page_config(
    page_title="Medical AI Assistant",
    layout="wide"
)

st.title("🏥 Medical AI Assistant")

st.markdown("""
Welcome to the Multi-Agent Medical Diagnosis Assistant.

Use the sidebar to navigate through:
- Dashboard
- Diagnosis
- Patient History
""")