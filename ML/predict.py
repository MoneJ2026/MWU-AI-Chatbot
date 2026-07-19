import joblib
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


model = joblib.load(
    os.path.join(BASE_DIR, "models", "model.pkl")
)

vectorizer = joblib.load(
    os.path.join(BASE_DIR, "models", "vectorizer.pkl")
)

encoder = joblib.load(
    os.path.join(BASE_DIR, "models", "encoder.pkl")
)


def predict_intent(message):

    vector = vectorizer.transform(
        [message]
    )

    result = model.predict(vector)

    intent = encoder.inverse_transform(
        result
    )

    return intent[0]


# Test
if __name__ == "__main__":

    while True:

        user = input("You: ")

        if user.lower() == "exit":
            break

        print(
            "Intent:",
            predict_intent(user)
        )