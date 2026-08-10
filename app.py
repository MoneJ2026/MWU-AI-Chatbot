
import sys
import streamlit as st

from chatbot import get_response


# ==========================================================
# MWU CHATBOT APP
# ==========================================================

class MWUChatbotApp:

    def __init__(self):
        self.__language = "en"
        self.__messages = []

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
            "Choose Language / Afaan filadhu",
            ["English", "Afaan Oromoo", "አማርኛ"],
            index=self.__get_language_index()
        )

        language_map = {
            "English": "en",
            "Afaan Oromoo": "om",
            "አማርኛ": "am"
        }

        self.set_language(
            language_map[language]
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

        self.__add_message(
            "user",
            user_message
        )

        result = get_response(
            user_message,
            self.__language
        )

        answer = result.get(
            "answer",
            "Dhiifama, deebii hin arganne."
        )

        self.__add_message(
            "assistant",
            answer
        )

        return answer

    # ======================================================
    # MAIN STREAMLIT APP
    # ======================================================

    def run(self):

        self.setup_page()

        st.title("🤖 MWU AI Chatbot")

        st.write(
            "Welcome to MWU AI Chatbot"
        )

        st.write(
            "Ask me anything about "
            "Madda Walabu University."
        )

        self.show_sidebar()

        self.show_chat_history()

        user_message = st.chat_input(
            "Ask your question..."
        )

        if user_message:

            answer = self.process_message(
                user_message
            )

            with st.chat_message("assistant"):

                st.write(answer)


# ==========================================================
# TERMINAL CHATBOT
# ==========================================================

def run_terminal():

    print("=" * 50)
    print("          MWU AI CHATBOT")
    print("=" * 50)
    print("Type 'exit' to stop the chatbot.")
    print()

    language = "en"

    while True:

        question = input("You: ")

        if question.lower().strip() == "exit":

            print("Bot: Goodbye!")
            break

        if not question.strip():
            continue

        result = get_response(
            question,
            language
        )

        intent = result.get(
            "topic",
            ""
        )

        answer = result.get(
            "answer",
            "Dhiifama, deebii hin arganne."
        )

        print("Intent:", intent)
        print("Bot:", answer)
        print()


# ==========================================================
# START APPLICATION
# ==========================================================

if __name__ == "__main__":

    # python app.py terminal
    if len(sys.argv) > 1 and sys.argv[1].lower() == "terminal":

        run_terminal()

    else:

        app = MWUChatbotApp()
        app.run()

