import pandas as pd
import json

def prepare_input(data: dict, columns_path):
    df = pd.DataFrame([data])
    df = pd.get_dummies(df)

    with open(columns_path, "r") as f:
        train_cols = json.load(f)

    df = df.reindex(columns=train_cols, fill_value=0)
    return df
