print("LOGGER WORKING")
import os
import pandas as pd
from datetime import datetime

LOG_FILE = "data/logs.csv"

def save_unknown_question(question):
    if not os.path.exists(LOG_FILE):
        pd.DataFrame(
            columns=["question", "time"]
        ).to_csv(LOG_FILE, index=False)

    df = pd.read_csv(LOG_FILE)

    # Duplicate hin kuusin
    if question.lower() not in df["question"].str.lower().values:
        df.loc[len(df)] = [
            question,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ]

    df.to_csv(LOG_FILE, index=False)