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


# Page config
st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON
)


# Sidebar
with st.sidebar:

    st.title(APP_NAME)

    st.write(f"Version: {VERSION}")

    st.write(f"Developer: {DEVELOPER}")

    st.markdown("---")

    st.write(
        "MWU AI Chatbot helps students "
        "get university information."
    )

    if st.button("🗑️ Clear Chat"):

        clear_chat()

        st.rerun()



# Language selection

language = st.selectbox(
    "Choose Language / Afaan filadhu / ቋንቋ ይምረጡ",
    [
        "Afaan Oromoo",
        "English",
        "Amharic"
    ]
)


# Welcome message

st.title(APP_NAME)

st.write(WELCOME_MESSAGE)



# Chat history

if "messages" not in st.session_state:

    st.session_state.messages = []



for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])



# User input

user_question = st.chat_input(
    "Gaaffii kee barreessi..."
)



if user_question:


    # user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )


    with st.chat_message("user"):

        st.write(user_question)



    # chatbot response

    answer = get_response(
        user_question,
        language
    )


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    with st.chat_message("assistant"):

        st.write(answer)