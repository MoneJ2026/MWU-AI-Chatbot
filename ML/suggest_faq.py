import pandas as pd

df = pd.read_csv("../data/clustered_logs.csv")

for cluster in df["cluster"].unique():

    questions = df[
        df["cluster"] == cluster
    ]["question"]

    print("================")
    print("Cluster:", cluster)

    for q in questions:
        print("-", q)