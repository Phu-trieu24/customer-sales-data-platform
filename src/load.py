# import pandas as pd

# #load_to_CSV file local
# def load_to_csv(df: pd.DataFrame, path: str):
#     """
#     Save transformed data to CSV
#     """
#     df.to_csv(path, index=False)

# load_to_postgres
from sqlalchemy import create_engine
import pandas as pd

def load_to_postgres(
    df: pd.DataFrame,
    table_name: str,
    conn_str: str,
    if_exists: str = "append"
):
    """
    Load DataFrame to Postgres table
    """
    engine = create_engine(conn_str)

    df.to_sql(
        table_name,
        engine,
        if_exists=if_exists,
        index=False,
        method="multi"
    )
