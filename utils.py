import streamlit as st

def clear_chat():
    """Clear chat history."""
    st.session_state.messages = []