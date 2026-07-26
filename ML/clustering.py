import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Read logs
df = pd.read_csv("../data/logs.csv")

questions = df["question"]

# Convert text to vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Create clusters
model = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

model.fit(X)

df["cluster"] = model.labels_

print(df[["question", "cluster"]])

df.to_csv("../data/clustered_logs.csv", index=False)

print("Clusters saved successfully!")