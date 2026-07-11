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



def search_question(question, language):

    data = load_all_data()

    question = question.lower()


    for item in data:

        keywords = item.get("keywords", [])


        for keyword in keywords:

            if keyword.lower() in question:

                answer = item.get("answer", {})

                # Afaan filatame yoo jiraate
                if language in answer:
                    return answer[language]

                # Yoo hin jirre Afaan Oromoo deebisi
                return answer.get(
                    "om",
                    "Dhiifama, odeeffannoo kana hin arganne."
                )


    if language == "en":
        return "Sorry, I could not find this information."

    elif language == "am":
        return "ይቅርታ፣ ይህን መረጃ ማግኘት አልቻልኩም።"

    else:
        return "Dhiifama, odeeffannoo kana hin arganne."