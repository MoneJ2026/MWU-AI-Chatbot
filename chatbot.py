from database import search_question
from responses import GREETINGS, THANKS, GOODBYE


def get_response(message, language):

    message = message.lower().strip()

    # Greeting
    if message in GREETINGS:
        return {
            "answer": GREETINGS[message].get(language, GREETINGS[message]["om"]),
            "topic": ""
        }

    # Thanks
    if message in THANKS:
        return {
            "answer": THANKS[message].get(language, THANKS[message]["om"]),
            "topic": ""
        }

    # Goodbye
    if message in GOODBYE:
        return {
            "answer": GOODBYE[message].get(language, GOODBYE[message]["om"]),
            "topic": ""
        }

    # Search Knowledge Base
    return search_question(message, language)