from database import search_question


def get_response(user_message):

    response = search_question(user_message)

    return response