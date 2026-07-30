import json
import os
from rapidfuzz import fuzz

DATA_FOLDER = "data"


# ==========================
# LOAD ALL JSON FILES
# ==========================
def load_all_data():
    knowledge = []

    if not os.path.exists(DATA_FOLDER):
        print("DATA FOLDER NOT FOUND")
        return knowledge

    for file in os.listdir(DATA_FOLDER):

        if file.endswith(".json"):

            path = os.path.join(DATA_FOLDER, file)

            try:
                with open(path, "r", encoding="utf-8") as f:

                    data = json.load(f)

                    if isinstance(data, list):
                        knowledge.extend(data)

            except Exception as e:
                print("ERROR:", file, e)

    print("TOTAL RECORDS:", len(knowledge))

    return knowledge


# ==========================
# LOAD ONE TOPIC
# ==========================
def load_topic_data(topic):

    path = os.path.join(DATA_FOLDER, f"{topic}.json")

    print("LOADING:", path)

    if not os.path.exists(path):

        print("FILE NOT FOUND")

        return []

    with open(path, "r", encoding="utf-8") as f:

        data = json.load(f)

    print("LOADED:", len(data), "records")

    return data


# ==========================
# SEARCH
# ==========================
def search_question(question, language="en", topic=None):

    question = question.lower().strip()

    print("\n==============================")
    print("SEARCH:", question)
    print("LANGUAGE:", language)
    print("TOPIC:", topic)

    if topic:

        data = load_topic_data(topic)

        if not data:

            print("Topic file empty -> Loading all data")

            data = load_all_data()

    else:

        data = load_all_data()

    best_score = 0
    best_item = None

    for item in data:

        # ----------------------
        # Keywords
        # ----------------------
        for keyword in item.get("keywords", []):

            score = fuzz.partial_ratio(
                question,
                keyword.lower()
            )

            if score > best_score:

                best_score = score
                best_item = item

        # ----------------------
        # Questions
        # ----------------------
        questions = item.get("question", {})

        if isinstance(questions, dict):

            for lang in ["en", "om", "am"]:

                if lang in questions:

                    score = fuzz.partial_ratio(
                        question,
                        questions[lang].lower()
                    )

                    if score > best_score:

                        best_score = score
                        best_item = item

    print("BEST SCORE:", best_score)

    # ==========================
    # FOUND
    # ==========================

    if best_item and best_score >= 70:

        answer = best_item.get("answer", {})

        if language == "en":
            response = answer.get("en", "")

        elif language == "am":
            response = answer.get("am", "")

        else:
            response = answer.get("om", "")

        print("FOUND TOPIC:", best_item.get("topic"))

        return {
            "answer": response,
            "topic": best_item.get("topic", ""),
            "found": True,
            "score": best_score
        }

    # ==========================
    # NOT FOUND
    # ==========================

    print("NOT FOUND")

    messages = {
        "en": "Sorry, I couldn't find information related to your question.",
        "om": "Dhiifama, gaaffii kanaaf odeeffannoo hin arganne.",
        "am": "ይቅርታ፣ ከጥያቄዎ ጋር የተያያዘ መረጃ አላገኘሁም።"
    }

    return {
        "answer": messages.get(language, messages["om"]),
        "topic": "",
        "found": False,
        "score": best_score
    }