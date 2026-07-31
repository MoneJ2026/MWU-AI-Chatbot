import json
import os
from rapidfuzz import fuzz

DATA_FOLDER = "data"


# ==========================
# LOAD ALL DATA
# ==========================
def load_all_data():
    knowledge = []

    if not os.path.exists(DATA_FOLDER):
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

    return knowledge


# ==========================
# LOAD ONE TOPIC
# ==========================
def load_topic_data(topic):

    path = os.path.join(DATA_FOLDER, f"{topic}.json")

    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:

        return json.load(f)


# ==========================
# SEARCH
# ==========================
def search_question(question, language="en", topic=None):

    question = question.lower().strip()

    if topic:

        data = load_topic_data(topic)

        if not data:
            data = load_all_data()

    else:
        data = load_all_data()

    best_score = 0
    best_item = None

    # ====================================
    # 1. EXACT MATCH
    # ====================================

    for item in data:

        questions = item.get("question", {})

        if isinstance(questions, dict):

            for lang in ["om", "en", "am"]:

                if lang in questions:

                    if question == questions[lang].lower().strip():

                        answer = item.get("answer", {})

                        return {
                            "answer": answer.get(language, answer.get("om")),
                            "topic": item.get("topic", ""),
                            "found": True,
                            "score": 100
                        }

    # ====================================
    # 2. FUZZY MATCH
    # ====================================

    for item in data:

        # Keywords
        for keyword in item.get("keywords", []):

            keyword = keyword.lower()

            score = max(

                fuzz.ratio(question, keyword),
                fuzz.partial_ratio(question, keyword),
                fuzz.token_sort_ratio(question, keyword),
                fuzz.token_set_ratio(question, keyword)

            )

            if score > best_score:

                best_score = score
                best_item = item

        # Questions
        questions = item.get("question", {})

        if isinstance(questions, dict):

            for lang in ["om", "en", "am"]:

                if lang in questions:

                    q = questions[lang].lower()

                    score = max(

                        fuzz.ratio(question, q),
                        fuzz.partial_ratio(question, q),
                        fuzz.token_sort_ratio(question, q),
                        fuzz.token_set_ratio(question, q)

                    )

                    if score > best_score:

                        best_score = score
                        best_item = item

    print("BEST SCORE:", best_score)

    # ====================================
    # FOUND
    # ====================================

    if best_item and best_score >= 80:

        answer = best_item.get("answer", {})

        return {
            "answer": answer.get(language, answer.get("om")),
            "topic": best_item.get("topic", ""),
            "found": True,
            "score": best_score
        }

    # ====================================
    # NOT FOUND
    # ====================================

    messages = {
        "om": "Dhiifama, gaaffii kanaaf odeeffannoo hin arganne.",
        "en": "Sorry, I couldn't find information related to your question.",
        "am": "ይቅርታ፣ ከጥያቄዎ ጋር የተያያዘ መረጃ አላገኘሁም።"
    }

    return {
        "answer": messages.get(language, messages["om"]),
        "topic": "",
        "found": False,
        "score": best_score
    }