def get_response(message, language):

    print("CHATBOT RECEIVED:", message)

    message = message.lower().strip()


    # USER MEMORY
    if message.startswith("maqaan koo"):

        name = message.replace(
            "maqaan koo",
            ""
        ).strip()

        print("SAVING NAME:", name)

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

        return {
            "answer": f"Maqaan kee {name} dha.",
            "topic": ""
        }


    # Database dhuma irratti
    return search_question(
        message,
        language
    )