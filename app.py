
import streamlit as st

from chatbot import get_response


# ==========================================================
# MWU CHATBOT APP
# Encapsulation
# ==========================================================

class MWUChatbotApp:

    def __init__(self):
        # Private attributes
        self.__language = "en"
        self.__messages = []

        # Initialize Streamlit session state
        self.__initialize_session()

    # ======================================================
    # PRIVATE METHOD
    # ======================================================

    def __initialize_session(self):

        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "language" not in st.session_state:
            st.session_state.language = "en"

        self.__messages = st.session_state.messages
        self.__language = st.session_state.language

    # ======================================================
    # GETTERS
    # ======================================================

    def get_language(self):
        return self.__language

    def get_messages(self):
        return self.__messages

    # ======================================================
    # SETTER
    # ======================================================

    def set_language(self, language):
        self.__language = language
        st.session_state.language = language

    # ======================================================
    # ADD MESSAGE
    # ======================================================

    def __add_message(self, role, content):

        message = {
            "role": role,
            "content": content
        }

        self.__messages.append(message)

        st.session_state.messages = self.__messages

    # ======================================================
    # CLEAR CHAT
    # ======================================================

    def clear_chat(self):

        self.__messages = []

        st.session_state.messages = []

    # ======================================================
    # PAGE CONFIGURATION
    # ======================================================

    def setup_page(self):

        st.set_page_config(
            page_title="MWU AI Chatbot",
            page_icon="🤖",
            layout="centered"
        )

    # ======================================================
    # SIDEBAR
    # ======================================================

    def show_sidebar(self):

        st.sidebar.title("⚙️ Settings")

        language = st.sidebar.selectbox(
            "Choose Language / Afaan filadhu / ቋንቋ ይምረጡ",
            options=["English", "Afaan Oromoo", "Amharic"],
            index=self.__get_language_index()
        )

        language_codes = {
            "English": "en",
            "Afaan Oromoo": "om",
            "Amharic": "am"
        }

        self.set_language(
            language_codes[language]
        )

        if st.sidebar.button("🗑️ Clear Chat"):

            self.clear_chat()

            st.rerun()

    # ======================================================
    # LANGUAGE INDEX
    # ======================================================

    def __get_language_index(self):

        language_map = {
            "en": 0,
            "om": 1,
            "am": 2
        }

        return language_map.get(
            self.__language,
            0
        )

    # ======================================================
    # DISPLAY CHAT HISTORY
    # ======================================================

    def show_chat_history(self):

        for message in self.__messages:

            with st.chat_message(
                message["role"]
            ):

                st.write(
                    message["content"]
                )

    # ======================================================
    # PROCESS USER MESSAGE
    # ======================================================

    def process_message(self, user_message):

        # Save user message
        self.__add_message(
            "user",
            user_message
        )

        # Get chatbot response
        result = get_response(
            user_message,
            self.__language
        )

        # Extract answer
        answer = result.get(
            "answer",
            "Dhiifama, deebii hin arganne."
        )

        # Save assistant response
        self.__add_message(
            "assistant",
            answer
        )

        return answer

    # ======================================================
    # MAIN APP
    # ======================================================

    def run(self):

        self.setup_page()

        # Header
        st.title("🤖 MWU AI Chatbot")

        st.write(
            "Welcome to MWU AI Chatbot"
        )

        st.write(
            "Ask me anything about "
            "Madda Walabu University."
        )

        # Sidebar
        self.show_sidebar()

        # Previous messages
        self.show_chat_history()

        # User input
        user_message = st.chat_input(
            "Ask your question..."
        )

        if user_message:

            answer = self.process_message(
                user_message
            )

            # Display response immediately
            with st.chat_message("assistant"):

                st.write(answer)


# ==========================================================
# CREATE APP OBJECT
# ==========================================================

app = MWUChatbotApp()

# ==========================================================
# RUN APP
# ==========================================================


