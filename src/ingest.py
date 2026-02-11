import pandas as pd

def ingest_data(path: str) -> pd.DataFrame:
    """
    Read raw data from CSV file
    """

    df = pd.read_csv(path)
    return df

#     """
#     Read raw data from API (REST/JSON)
#     """
# import requests
# def ingest_api(url: str, params: dict = None) -> pd.DataFrame:
    
#     response = requests.get(url, params=params)
#     response.raise_for_status()

#     data = response.json()
#     return pd.DataFrame(data)

#     """
#     Read TỪ DATABASE (Postgres / MySQL)
#     ✅ Khi nào dùng?
#     - Source là OLTP
#     - Data warehouse sync
#     - Incremental load
#     """

# import pandas as pd
# from sqlalchemy import create_engine

# def ingest_db(connection_string: str, query: str) -> pd.DataFrame:
#     """
#     Ingest data from database using SQL query
#     """
#     engine = create_engine(connection_string)
#     df = pd.read_sql(query, engine)
#     return df


#     """📌 
#     Incremental ingest (rất quan trọng)
#     """
# def ingest_db_incremental(conn_str: str, table: str, last_updated: str):
#     query = f"""
#     SELECT *
#     FROM {table}
#     WHERE updated_at > '{last_updated}'
#     """
#     engine = create_engine(conn_str)
#     return pd.read_sql(query, engine)