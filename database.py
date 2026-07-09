import json


def load_data():

    with open("university_data.json", "r") as file:
        data = json.load(file)

    return data


def search_question(question):

    data = load_data()

    question = question.lower()

    for item in data:
        if item["question"] in question:
            return item["answer"]

    return "Sorry, information hin argamne."