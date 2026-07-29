import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==========================
# LOAD DATA
# ==========================

df = pd.read_csv("data/intents.csv")

X = df["text"]
y = df["intent"]

# ==========================
# LABEL ENCODER
# ==========================

encoder = LabelEncoder()
y = encoder.fit_transform(y)

# ==========================
# TF-IDF
# ==========================

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# MODEL
# ==========================

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# ==========================
# TEST
# ==========================

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)

# ==========================
# SAVE
# ==========================

joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(encoder, "models/encoder.pkl")

print("Training Finished Successfully")