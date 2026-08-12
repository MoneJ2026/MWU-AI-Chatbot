import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ==========================================================
# LOAD DATA
# ==========================================================

df = pd.read_csv("data/intents.csv")

print("\n========== DATASET ==========")
print(df.head())

print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())


# ==========================================================
# DATA CLEANING
# ==========================================================

df = df.dropna(subset=["text", "intent"])

df["text"] = df["text"].astype(str).str.strip()
df["intent"] = df["intent"].astype(str).str.strip()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate questions:")
print(df.duplicated(subset=["text"]).sum())

df = df.drop_duplicates(subset=["text"])


# ==========================================================
# INTENT DISTRIBUTION
# ==========================================================

print("\n========== INTENT DISTRIBUTION ==========")
print(df["intent"].value_counts())


# ==========================================================
# FEATURES AND LABELS
# ==========================================================

X = df["text"]
y = df["intent"]


# ==========================================================
# LABEL ENCODER
# ==========================================================

encoder = LabelEncoder()

y = encoder.fit_transform(y)


# ==========================================================
# TRAIN / TEST SPLIT
# ==========================================================

X_train_text, X_test_text, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================================
# TF-IDF
# ==========================================================

vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=5000
)

X_train = vectorizer.fit_transform(X_train_text)

X_test = vectorizer.transform(X_test_text)


# ==========================================================
# MODEL
# ==========================================================

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train, y_train)


# ==========================================================
# TEST
# ==========================================================

prediction = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    prediction
)

print("\n========== RESULT ==========")
print("Accuracy:", accuracy)


# ==========================================================
# SAVE MODELS
# ==========================================================

joblib.dump(
    model,
    "models/model.pkl"
)

joblib.dump(
    vectorizer,
    "models/vectorizer.pkl"
)

joblib.dump(
    encoder,
    "models/encoder.pkl"
)

print("\nTraining Finished Successfully!")