import joblib


# Load trained files

model = joblib.load("../models/model.pkl")

vectorizer = joblib.load("../models/vectorizer.pkl")

encoder = joblib.load("../models/encoder.pkl")



def predict_intent(message):

    # text gara number jijjiiri

    text_vector = vectorizer.transform(
        [message]
    )


    # predict

    prediction = model.predict(
        text_vector
    )


    # number gara intent deebisi

    intent = encoder.inverse_transform(
        prediction
    )


    return intent[0]
if __name__ == "__main__":

    while True:

        user = input("You: ")

        result = predict_intent(user)

        print("Intent:", result)