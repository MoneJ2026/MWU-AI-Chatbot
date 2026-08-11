
import os
import pandas as pd
from datetime import datetime


LOG_FILE = "data/logs.csv"


def save_unknown_question(question, confidence):

    # ==========================================
    # CREATE DATAFRAME IF FILE DOES NOT EXIST
    # ==========================================

    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:

        df = pd.DataFrame(
            columns=[
                "question",
                "time",
                "confidence"
            ]
        )

    else:

        df = pd.read_csv(LOG_FILE)

        # ------------------------------------------
        # Yoo logs.csv duraan confidence hin qabne
        # ta'e, column itti dabali
        # ------------------------------------------

        if "confidence" not in df.columns:
            df["confidence"] = None

    # ==========================================
    # DUPLICATE CHECK
    # ==========================================

    if question.lower() not in df["question"].astype(str).str.lower().values:

        df.loc[len(df)] = [
            question,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            confidence
        ]

    # ==========================================
    # SAVE CSV
    # ==========================================

    df.to_csv(
        LOG_FILE,
        index=False
    )
