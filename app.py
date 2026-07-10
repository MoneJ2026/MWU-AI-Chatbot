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


st.title(APP_NAME)

st.write(WELCOME_MESSAGE)