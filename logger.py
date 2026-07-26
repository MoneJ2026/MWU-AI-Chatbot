import os
import pandas as pd
from datetime import datetime

LOG_FILE = "data/logs.csv"


def save_unknown_question(question):

    # Yoo file hin jirre ykn duwwaa ta'e
    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        df = pd.DataFrame(columns=["question", "time"])
    else:
        df = pd.read_csv(LOG_FILE)

    # Duplicate hin kuusin
    if question.lower() not in df["question"].astype(str).str.lower().values:
        df.loc[len(df)] = [
            question,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ]

    df.to_csv(LOG_FILE, index=False)