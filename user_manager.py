import json
import os


USER_FILE = "users.json"


def load_users():

    if not os.path.exists(USER_FILE):
        return {}

    with open(
        USER_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_users(users):

    with open(
        USER_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            users,
            f,
            indent=4,
            ensure_ascii=False
        )



def create_user(name):

    users = load_users()

    users[name] = {
        "name": name,
        "questions": []
    }

    save_users(users)



def add_question(name, question):

    users = load_users()

    if name in users:

        users[name]["questions"].append(question)

        save_users(users)