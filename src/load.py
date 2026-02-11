import pandas as pd

def load_to_csv(df: pd.DataFrame, path: str):
    """
    Save transformed data to CSV
    """
    df.to_csv(path, index=False)
