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


def search_question(question, language):

    data = load_all_data()

    question = question.lower().strip()

    best_score = 0
    best_answer = None

    for item in data:

        # Search using keywords
        for keyword in item.get("keywords", []):

            score = fuzz.partial_ratio(
                question,
                keyword.lower()
            )

            if score > best_score:

                best_score = score
                best_answer = item.get("answer", {})

        # Search using questions (Afaan 3)
        questions = item.get("question", {})

        for lang in ["om", "en", "am"]:

            if lang in questions:

                score = fuzz.partial_ratio(
                    question,
                    questions[lang].lower()
                )

                if score > best_score:

                    best_score = score
                    best_answer = item.get("answer", {})

    # If similarity is good enough
    if best_score >= 70 and best_answer:

        if language in best_answer:
            return best_answer[language]

        return best_answer.get("om")

    # Default messages
    if language == "en":
        return (
            "Sorry, I couldn't find information "
            "related to your question."
        )

    elif language == "am":
        return (
            "ይቅርታ፣ ከጥያቄዎ ጋር የተያያዘ "
            "መረጃ አላገኘሁም።"
        )

    return "Dhiifama, gaaffii kanaaf odeeffannoo hin arganne."