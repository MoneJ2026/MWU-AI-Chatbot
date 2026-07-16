import joblib


model = joblib.load("../models/model.pkl")
vectorizer = joblib.load("../models/vectorizer.pkl")
encoder = joblib.load("../models/encoder.pkl")


def predict_intent(message):

    vector = vectorizer.transform(
        [message]
    )

    result = model.predict(vector)

    intent = encoder.inverse_transform(
        result
    )

    return intent[0]