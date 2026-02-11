from src.ingest import ingest_data
from src.transform import transform_data
# from src.load import load_to_csv
from src.load import load_to_postgres


RAW_PATH = "data/raw/online_retail.csv"
PROCESSED_PATH = "data/processed/online_retail_transformed.csv"
CONN_STR = "postgresql://analyst:mypassword123@localhost:5432/sales_analytics"
def run_pipeline():
    print("📥 Ingesting data...")
    df_raw = ingest_data(RAW_PATH)

    print("🔄 Transforming data...")
    df_transformed = transform_data(df_raw)

    print("📤 Loading data...")
    # load_to_csv(df_transformed, PROCESSED_PATH)

    load_to_postgres(
        df_transformed,
        table_name="retail_sales",
        conn_str=CONN_STR
    )

    print("✅ Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()
