from database import search_question


def get_response(message, language):

    response = search_question(
        message,
        language
    )

    return response