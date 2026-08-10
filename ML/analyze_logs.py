import pandas as pd
import numpy as np

LOG_FILE = "../data/logs.csv"

df = pd.read_csv(LOG_FILE)

print("Columns:", df.columns.tolist())
print(df)