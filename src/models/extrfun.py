import pandas as pd

def extract(path):
    df = pd.read_csv(path)
    print("extraction done")
    return df

def transform(df):
    tdf = df[df["category"] == "Supplies"]
    print("transform done")
    return tdf

def load(df):
    print("loading data...")
    df.to_csv("supplies.csv")
    print("loaded data")