import pandas as pd

def preprocess_data(path):
    """
    Load CSV, drop rows with missing values, return clean DataFrame
    """
    df = pd.read_csv(path)
    df = df.dropna()
    return df
