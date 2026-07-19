import json
import os
from rapidfuzz import fuzz

DATA_FOLDER = "data"


def load_all_data():

    knowledge = []

    if not os.path.exists(DATA_FOLDER):
        return knowledge

    for file in os.listdir(DATA_FOLDER):

        if file.endswith(".json"):

            path = os.path.join(DATA_FOLDER, file)

            with open(path, "r", encoding="utf-8") as f:

                data = json.load(f)

                if isinstance(data, list):
                    knowledge.extend(data)

    return knowledge


def search_question(question, language, topic=None):

    question = question.lower().strip()


    if topic:

        data = load_topic_data(topic)

        if not data:
            data = load_all_data()

    else:

        data = load_all_data()


    best_score = 0
    best_item = None

    question = question.lower().strip()

    best_score = 0
    best_item = None

    for item in data:

        # Search using keywords
        for keyword in item.get("keywords", []):

            score = fuzz.partial_ratio(
                question,
                keyword.lower()
            )

            if score > best_score:

                best_score = score
                best_item = item

        # Search using multilingual questions
        questions = item.get("question", {})

        for lang in ["om", "en", "am"]:

            if lang in questions:

                score = fuzz.partial_ratio(
                    question,
                    questions[lang].lower()
                )

                if score > best_score:

                    best_score = score
                    best_item = item

    # Match found
    if best_score >= 70 and best_item:

        answer = best_item.get("answer", {})

        return {
            "answer": answer.get(language, answer.get("om")),
            "topic": best_item.get("topic", "")
        }

    # No match
    if language == "en":

        return {
            "answer": "Sorry, I couldn't find information related to your question.",
            "topic": ""
        }

    elif language == "am":

        return {
            "answer": "ይቅርታ፣ ከጥያቄዎ ጋር የተያያዘ መረጃ አላገኘሁም።",
            "topic": ""
        }

    return {
        "answer": "Dhiifama, gaaffii kanaaf odeeffannoo hin arganne.",
        "topic": ""
    }
def load_topic_data(topic):

    path = os.path.join(DATA_FOLDER, f"{topic}.json")

    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)