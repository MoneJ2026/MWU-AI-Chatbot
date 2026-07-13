def get_response(message, language):

    message = message.lower().strip()

    print("MESSAGE:", message)
    print("LANGUAGE:", language)

    # Greeting
    if message in GREETINGS:

        result = {
            "answer": GREETINGS[message].get(language, GREETINGS[message]["om"]),
            "topic": ""
        }

        print("GREETING RESULT:", result)

        return result


    result = search_question(message, language)

    print("DATABASE RESULT:", result)

    return result