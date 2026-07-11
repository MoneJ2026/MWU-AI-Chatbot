import json
import os


DATA_FOLDER = "data"


def load_all_data():
    knowledge = []

    for file in os.listdir(DATA_FOLDER):
        if file.endswith(".json"):
            path = os.path.join(DATA_FOLDER, file)

            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                knowledge.extend(data)

    return knowledge



def search_question(question):

    data = load_all_data()

    question = question.lower()

    for item in data:

        keywords = item.get("keywords", [])

        for keyword in keywords:

            if keyword.lower() in question:

                return item["answer"]["om"]

    return "Dhiifama, odeeffannoo kana hin arganne."