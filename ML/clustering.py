import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# ==========================
# READ LOGS
# ==========================

df = pd.read_csv("../data/logs.csv")

questions = df["question"]

# ==========================
# CONVERT TEXT TO VECTORS
# ==========================

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(questions)

# ==========================
# ELBOW METHOD
# ==========================

wcss = []

max_k = min(10, len(df))

for k in range(1, max_k + 1):

    km = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    km.fit(X)

    wcss.append(km.inertia_)

plt.figure(figsize=(6, 4))

plt.plot(range(1, max_k + 1), wcss, marker="o")

plt.title("Elbow Method")

plt.xlabel("Number of Clusters (K)")

plt.ylabel("WCSS")

plt.grid(True)

plt.show()

# ==========================
# CREATE CLUSTERS
# ==========================

model = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

model.fit(X)

df["cluster"] = model.labels_

# ==========================
# SHOW RESULT
# ==========================

print(df[["question", "cluster"]])

# ==========================
# SAVE RESULT
# ==========================

df.to_csv("../data/clustered_logs.csv", index=False)

print("\nClusters saved successfully!")