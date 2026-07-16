from faq import search_question

from memory import remember, get_memory



def get_response(message, language="en"):

    print("CHATBOT RECEIVED:", message)


    message = message.lower().strip()



    # USER MEMORY
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


        return {

            "answer": f"Maqaan kee {name} dha.",

            "topic": ""

        }



    # FAQ SEARCH

    return search_question(

        message,

        language

    )