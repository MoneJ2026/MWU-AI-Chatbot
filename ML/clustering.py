import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

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

plt.figure(figsize=(6,4))
plt.plot(range(1, max_k + 1), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.grid(True)
plt.show()

# ==========================
# SILHOUETTE SCORE
# ==========================

print("\n===== Silhouette Scores =====")

best_score = -1
best_k = 2

for k in range(2, max_k + 1):

    km = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = km.fit_predict(X)

    score = silhouette_score(X, labels)

    print(f"K = {k}   Score = {score:.3f}")

    if score > best_score:
        best_score = score
        best_k = k

print(f"\nBest K = {best_k}")
print(f"Best Score = {best_score:.3f}")

# ==========================
# CREATE CLUSTERS
# ==========================

model = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

model.fit(X)

df["cluster"] = model.labels_

# ==========================
# SHOW RESULT
# ==========================

print("\nCluster Results")

print(df[["question", "cluster"]])

# ==========================
# SAVE RESULT
# ==========================

df.to_csv("../data/clustered_logs.csv", index=False)

print("\nClusters saved successfully!")