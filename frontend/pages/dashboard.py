import streamlit as st

from frontend.components.charts import (
    show_patient_statistics
)

st.title("📊 Dashboard")

st.metric(
    label="Total Patients",
    value="152"
)

st.metric(
    label="Critical Cases",
    value="8"
)

st.metric(
    label="Reports Generated",
    value="320"
)

show_patient_statistics()