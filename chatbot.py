from database import search_question
from responses import GREETINGS, THANKS, GOODBYE


def get_response(message, language):

    message = message.lower().strip()

    print("USER:", message)
    print("LANG:", language)


    # Greeting
    if message in GREETINGS:

        print("GREETING FOUND")

        return GREETINGS[message].get(
            language,
            GREETINGS[message]["om"]
        )


    # Thanks
    if message in THANKS:

        return THANKS[message].get(
            language,
            THANKS[message]["om"]
        )


    # Goodbye
    if message in GOODBYE:

        return GOODBYE[message].get(
            language,
            GOODBYE[message]["om"]
        )


    # University information
    return search_question(
        message,
        language
    )