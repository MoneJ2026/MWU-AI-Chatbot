from database import search_question
from logger import save_unknown_question
from ML.predict import predict_intent
from memory import remember, get_memory


class MWUChatbot:
    """
    MWU AI Chatbot

    Encapsulation:
    - __language -> language chatbot
    - __last_message -> user's latest message
    - __last_intent -> predicted intent
    """

    def __init__(self, language="en"):
        self.__language = language
        self.__last_message = ""
        self.__last_intent = ""

    # ==========================
    # GETTER
    # ==========================

    def get_language(self):
        return self.__language

    def get_last_message(self):
        return self.__last_message

    def get_last_intent(self):
        return self.__last_intent

    # ==========================
    # SETTER
    # ==========================

    def set_language(self, language):
        self.__language = language

    # ==========================
    # MAIN RESPONSE METHOD
    # ==========================

    def get_response(self, message):

        print("🔥 GET_RESPONSE STARTED")
        print("CHATBOT RECEIVED:", message)

        # ==========================
        # SAVE MESSAGE
        # ==========================

        self.__last_message = message

        message = message.lower().strip()

        # ==========================
        # USER MEMORY
        # ==========================

        if message.startswith("maqaan koo"):

            name = message.replace(
                "maqaan koo",
                ""
            ).strip()

            remember("name", name)

            return {
                "answer": f"Galatoomi {name}, si yaadadha.",
                "topic": ""
            }

        if message == "maqaan kiyya maal":

            name = get_memory("name")

            if name:
                return {
                    "answer": f"Maqaan kee {name} dha.",
                    "topic": ""
                }

            return {
                "answer": "Maqaa kee amma hin yaadadhu.",
                "topic": ""
            }

        # ==========================
        # MACHINE LEARNING
        # ==========================

        intent = predict_intent(message)

        self.__last_intent = intent

        print("PREDICTED INTENT:", intent)

        # ==========================
        # DATABASE SEARCH
        # ==========================

        result = search_question(
            message,
            self.__language,
            intent
        )

        # ==========================
        # UNKNOWN QUESTION LOGGER
        # ==========================

        print("RESULT:", result)

        if not result["found"]:

            print("UNKNOWN QUESTION:", message)

            save_unknown_question(message)

        return result


# ==================================
# BACKWARD COMPATIBILITY FUNCTION
# ==================================

_bot = MWUChatbot()


def get_response(message, language="en"):
    """
    Old function interface.

    This keeps app.py working if it already uses:

        get_response(message, language)
    """

    _bot.set_language(language)

    return _bot.get_response(message)