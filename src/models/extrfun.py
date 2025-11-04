import pandas as pd

def e_t(path):
    df = pd.read_csv(path)
    df = df[df["category"] == "Supplies"]
    print("extraction and transformation done")
    return df

def load(df):
    print("loading data...")
    df.to_csv("supplies.csv")
    print("loaded data")