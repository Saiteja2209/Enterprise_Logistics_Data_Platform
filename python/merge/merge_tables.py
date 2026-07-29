from database.connect_snowflake import get_connection
from config.config_loader import get_table_config
from config.table_config import TABLE_CONFIG
from logger.logger import logger


def get_columns(table_name):

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(f'DESC TABLE RAW."{table_name.upper()}"')
        columns = [row[0] for row in cur.fetchall()]
        return columns
    finally:
        cur.close()
        conn.close()




def build_update_clause(columns, primary_key):

    updates = []

    for col in columns:
        if col != primary_key:
            updates.append(f"T.{col}=S.{col}")

    return ", ".join(updates)


def build_insert_clause(columns):

    column_list = ", ".join(columns)

    values = ", ".join([f"S.{c}" for c in columns])

    return column_list, values


def merge_table(file):
    table_name = file.stem.lower()

    # Validate that the table has a configuration entry
    if table_name not in TABLE_CONFIG:
        raise ValueError(f"No configuration found for table: {table_name}")

    # Quote identifiers to protect against reserved words or special characters
    target_table = f'RAW."{table_name.upper()}"'
    stage_table = f'RAW."{table_name.upper()}_STAGE"'

    config = get_table_config(table_name)
    primary_key = config["primary_key"]

    columns = get_columns(table_name)
    if not columns:
        raise ValueError(f"No columns found for RAW.{table_name.upper()}")

    update_clause = build_update_clause(columns, primary_key)
    insert_columns, insert_values = build_insert_clause(columns)

    merge_sql = f"""
    MERGE INTO {target_table} T
    USING {stage_table} S
    ON T.{primary_key}=S.{primary_key}

    WHEN MATCHED THEN
        UPDATE SET
            {update_clause}

    WHEN NOT MATCHED THEN
        INSERT ({insert_columns})
        VALUES ({insert_values})
    """

    conn = get_connection()
    cur = conn.cursor()

    try:
        logger.info(f"Merging {table_name}...")
        logger.debug(f"Generated MERGE SQL:\n{merge_sql}")
        cur.execute(merge_sql)
        conn.commit()
        logger.info(f"{table_name} merged successfully.")
    except Exception as e:
        logger.error(f"Merge failed for {table_name}")
        logger.error(str(e))
        raise
    finally:
        cur.close()
        conn.close()

    