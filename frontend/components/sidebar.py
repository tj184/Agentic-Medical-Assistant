import streamlit as st


def render_sidebar():

    st.sidebar.title(
        "Medical AI Assistant"
    )

    st.sidebar.info(
        """
        Multi-Agent AI System
        with RAG + LangGraph
        """
    )

    st.sidebar.success(
        "System Running"
    )