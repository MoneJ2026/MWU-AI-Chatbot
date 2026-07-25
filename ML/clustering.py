import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Read questions
df = pd.read_csv("../data/intents.csv")

questions = df["text"]

# Convert text to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Create clusters
model = KMeans(
    n_clusters=5,
    random_state=42
)

model.fit(X)

df["cluster"] = model.labels_

print(df[["text", "cluster"]])