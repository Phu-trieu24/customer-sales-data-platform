import pandas as pd

# 1️⃣ CLEANING
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]
    return df


# 2️⃣ ENRICHMENT
def enrich_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["IsCancelled"] = df["InvoiceNo"].astype(str).str.startswith("C")
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    return df


# 3️⃣ FEATURE ENGINEERING
def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["Day"] = df["InvoiceDate"].dt.day
    df["Hour"] = df["InvoiceDate"].dt.hour
    return df


# 4️⃣ PIPELINE FUNCTION
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_data(df)
    df = enrich_data(df)
    df = add_time_features(df)
    return df
