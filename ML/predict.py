import joblib
import os
import numpy as np


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

    probabilities = model.predict_proba(
        vector
    )

    confidence = np.max(
        probabilities
    )

    intent = encoder.inverse_transform(
        result
    )

    return intent[0], confidence


# Test

if __name__ == "__main__":

    while True:

        user = input("You: ")

        if user.lower() == "exit":
            break

        intent, confidence = predict_intent(
            user
        )

        print("Intent:", intent)
        print("Confidence:", confidence)