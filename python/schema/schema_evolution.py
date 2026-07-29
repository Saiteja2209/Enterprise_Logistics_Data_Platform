import pandas as pd

from database.connect_snowflake import get_connection
from schema.datatype_mapper import map_dtype
from logger.logger import logger


def get_table_columns(table_name):

    conn = get_connection()
    cur = conn.cursor()

    try:

        cur.execute(f'DESC TABLE RAW."{table_name.upper()}"')

        return {
            row[0].upper(): row[1]
            for row in cur.fetchall()
        }

    finally:

        cur.close()
        conn.close()

def get_csv_columns(file):

    df = pd.read_csv(file, nrows=100)

    return {
        col.upper(): map_dtype(df[col].dtype)
        for col in df.columns
    }

def detect_new_columns(csv_cols, table_cols):

    new_columns = {}

    for column, datatype in csv_cols.items():

        if column not in table_cols:

            new_columns[column] = datatype

    return new_columns

def add_new_columns(table_name, new_columns):

    if not new_columns:
        return

    conn = get_connection()
    cur = conn.cursor()

    try:

        for column, datatype in new_columns.items():

            sql = f'''
            ALTER TABLE RAW."{table_name.upper()}"
            ADD COLUMN "{column}" {datatype}
            '''

            logger.info(f"Adding column {column}")

            cur.execute(sql)

        conn.commit()

    finally:

        cur.close()
        conn.close()

def evolve_schema(file):

    table = file.stem.lower()

    csv_columns = get_csv_columns(file)

    table_columns = get_table_columns(table)

    new_columns = detect_new_columns(
        csv_columns,
        table_columns
    )

    add_new_columns(table, new_columns)
