import pandas as pd
from sqlalchemy import create_engine

from src.config import CLEANED_DATA_PATH, SQL_DATABASE, SQL_SERVER, SQL_TABLE


def main() -> None:
    if not CLEANED_DATA_PATH.exists():
        raise FileNotFoundError(f"Cleaned dataset not found: {CLEANED_DATA_PATH}. Run cleaner first.")

    df = pd.read_csv(CLEANED_DATA_PATH)

    connection_string = (
        f"mssql+pyodbc://{SQL_SERVER}/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )

    engine = create_engine(connection_string)
    df.to_sql(SQL_TABLE, con=engine, if_exists="replace", index=False)

    print(f"Data inserted into SQL Server table '{SQL_TABLE}' successfully.")


if __name__ == "__main__":
    main()
