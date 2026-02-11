from src.ingest import ingest_data
from src.transform import transform_data
from src.load import load_to_csv

RAW_PATH = "data/raw/online_retail.csv"
PROCESSED_PATH = "data/processed/retail_transformed.csv"

def run_pipeline():
    print("📥 Ingesting data...")
    df_raw = ingest_data(RAW_PATH)

    print("🔄 Transforming data...")
    df_transformed = transform_data(df_raw)

    print("📤 Loading data...")
    load_to_csv(df_transformed, PROCESSED_PATH)

    print("✅ Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()
