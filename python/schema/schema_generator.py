import pandas as pd

from database.connect_snowflake import get_connection
from logger.logger import logger
from schema.datatype_mapper import map_dtype


def create_table_if_not_exists(file):

    table_name = file.stem.upper()

    conn = get_connection()
    cur = conn.cursor()

    try:
        # Check whether the RAW table already exists
        cur.execute(f"""
            SHOW TABLES LIKE '{table_name}' IN SCHEMA RAW
        """)

        if cur.fetchone():
            logger.info(f"RAW.{table_name} already exists.")
            return

        logger.info(f"Creating RAW.{table_name}...")

        # Read only a sample of the CSV to infer schema
        df = pd.read_csv(file, nrows=100)

        columns = []

        for column in df.columns:
            snowflake_type = map_dtype(df[column].dtype)
            columns.append(f'"{column.upper()}" {snowflake_type}')

        column_sql = ",\n".join(columns)

        create_table_sql = f"""
        CREATE TABLE RAW."{table_name}"
        (
            {column_sql}
        )
        """

        cur.execute(create_table_sql)

        logger.info(f"RAW.{table_name} created successfully.")

        create_stage_sql = f"""
        CREATE TABLE RAW."{table_name}_STAGE"
        LIKE RAW."{table_name}"
        """

        cur.execute(create_stage_sql)

        logger.info(f"RAW.{table_name}_STAGE created successfully.")

        conn.commit()

    except Exception as e:
        logger.error(str(e))
        raise

    finally:
        cur.close()
        conn.close()