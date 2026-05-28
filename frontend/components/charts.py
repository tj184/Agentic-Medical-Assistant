import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt


def show_patient_statistics():

    data = pd.DataFrame({
        "Department": [
            "Cardiology",
            "Neurology",
            "General Medicine",
            "Emergency"
        ],
        "Patients": [
            45,
            20,
            70,
            17
        ]
    })

    fig, ax = plt.subplots()

    ax.bar(
        data["Department"],
        data["Patients"]
    )

    ax.set_title(
        "Patients by Department"
    )

    st.pyplot(fig)