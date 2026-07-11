import streamlit as st
from chatbot import get_response

from config import (
    APP_NAME,
    APP_ICON,
    VERSION,
    DEVELOPER,
    WELCOME_MESSAGE
)

from utils import clear_chat


st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON
)


# Sidebar (kana asitti kaa'i)
with st.sidebar:

    st.title(APP_NAME)

    st.write(f"Version: {VERSION}")

    st.write(f"Developer: {DEVELOPER}")

    st.markdown("---")

    st.write(
        "MWU AI Chatbot helps student "
        "get university information."
    )

    if st.button("🗑️ Clear Chat"):
        clear_chat()
        st.rerun()


# Main page
st.title(APP_NAME)

st.write(WELCOME_MESSAGE)