from database.connect_snowflake import get_connection
from config.config_loader import get_table_config
from logger.logger import logger


def validate_table(file):

    conn = get_connection()
    cur = conn.cursor()

    table = file.stem.lower()

    config = get_table_config(table)

    if not config["active"]:
        raise ValueError(f"Table {table} is marked as INACTIVE.")

    stage_table = f"{table.upper()}_STAGE"
    primary_key = config["primary_key"]

    try:
        # Check row count
        cur.execute(f'SELECT COUNT(*) FROM RAW."{stage_table}"')
        row_count = cur.fetchone()[0]

        if row_count == 0:
            raise ValueError(f"{stage_table} contains 0 rows.")

        logger.info(f"{stage_table} contains {row_count} rows.")

        # Check NULL primary keys
        cur.execute(
            f'''
            SELECT COUNT(*)
            FROM RAW."{stage_table}"
            WHERE "{primary_key}" IS NULL
            '''
        )

        null_count = cur.fetchone()[0]

        if null_count > 0:
            raise ValueError(
                f"{stage_table} contains {null_count} NULL primary keys."
            )

        logger.info(f"{stage_table} has no NULL primary keys.")

        # Check duplicate primary keys
        cur.execute(
            f'''
            SELECT COUNT(*)
            FROM (
                SELECT "{primary_key}"
                FROM RAW."{stage_table}"
                GROUP BY "{primary_key}"
                HAVING COUNT(*) > 1
            )
            '''
        )

        duplicate_count = cur.fetchone()[0]

        if duplicate_count > 0:
            raise ValueError(
                f"{stage_table} contains {duplicate_count} duplicate primary keys."
            )

        logger.info(f"{stage_table} has no duplicate primary keys.")

    except Exception as e:
        logger.error(str(e))
        raise

    finally:
        cur.close()
        conn.close()