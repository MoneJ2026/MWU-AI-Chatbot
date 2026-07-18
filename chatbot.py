from database import search_question
from ML.predict import predict_intent
from memory import remember, get_memory
def get_response(message, language="en"):

    print("CHATBOT RECEIVED:", message)

    message = message.lower().strip()

    # ==========================
    # USER MEMORY
    # ==========================

    if message.startswith("maqaan koo"):

        name = message.replace(
            "maqaan koo",
            ""
        ).strip()

        remember(
            "name",
            name
        )

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

    print("PREDICTED INTENT:", intent)

    # ==========================
    # DATABASE SEARCH
    # ==========================

    result = search_question(
        message,
        language,
        intent
    )

    return result