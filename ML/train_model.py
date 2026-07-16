import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import joblib


# Load dataset
data = pd.read_csv("../data/intents.csv")


# Separate features and labels
X = data["text"]
y = data["intent"]


# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)


# Convert text to numbers
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = LogisticRegression()


# Train model
model.fit(X_train, y_train)


# Test model
prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)
joblib.dump(model, "../models/model.pkl")
joblib.dump(vectorizer, "../models/vectorizer.pkl")
joblib.dump(encoder, "../models/encoder.pkl")

print("Model saved successfully")