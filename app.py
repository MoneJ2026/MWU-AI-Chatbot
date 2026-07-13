from user_manager import add_question
from faq import get_faqs
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

        st.session_state.messages = []

        st.session_state.last_topic = ""

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



# Language code

if language == "Afaan Oromoo":

    lang_code = "om"

elif language == "English":

    lang_code = "en"

else:

    lang_code = "am"



# Title

st.title(APP_NAME)

st.write(WELCOME_MESSAGE)



# Initialize session memory

if "messages" not in st.session_state:

    st.session_state.messages = []


if "last_topic" not in st.session_state:

    st.session_state.last_topic = ""



# Display chat history

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])



# User input

user_question = st.chat_input(
    "Gaaffii kee barreessi..."
)



if user_question:


    # Conversation memory

    follow_up_words = [
        "yoom",
        "eessa",
        "akkam",
        "akkamitti",
        "maal",
        "when",
        "where",
        "how",
        "what"
    ]


    first_word = user_question.lower().split()[0]


    if (
        st.session_state.last_topic
        and first_word in follow_up_words
    ):

        user_question = (
            st.session_state.last_topic
            + " "
            + user_question
        )



    # User message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )


    with st.chat_message("user"):

        st.write(user_question)



    # Get chatbot response

    result = get_response(
        user_question,
        lang_code
    )



    # Handle response

    if isinstance(result, dict):

        answer = result.get(
            "answer",
            "Dhiifama, deebii hin arganne."
        )

        topic = result.get(
            "topic",
            ""
        )

    else:

        answer = result

        topic = ""



    # Save conversation memory

    if topic:

        st.session_state.last_topic = topic



    # Assistant message

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )



    # Show assistant response

    with st.chat_message("assistant"):

        st.write(answer)