import json

with open("university_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def get_answer(question):
    question = question.lower()

    for key in data:
        if key in question:
            return data[key]

    return "Dhiifama, gaaffii kanaaf deebii hin qabu."