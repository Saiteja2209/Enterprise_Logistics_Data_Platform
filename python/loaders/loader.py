from database.connect_snowflake import get_connection
from logger.logger import logger


def load_table(file):

    conn = get_connection()
    cur = conn.cursor()

    table_name = f"{file.stem.upper()}_STAGE"

    target_table = file.stem.upper()

    try:
        cur.execute(f"""
            CREATE TABLE IF NOT EXISTS RAW.{table_name}
            LIKE RAW.{target_table}
        """)

        sql = f"""
        COPY INTO RAW.{table_name}
        FROM @UTIL.LOGISTICS_STAGE/{file.name}.gz
        FILE_FORMAT=(
            FORMAT_NAME='UTIL.CSV_FORMAT',
            SKIP_HEADER=0,
            PARSE_HEADER=TRUE,
            ERROR_ON_COLUMN_COUNT_MISMATCH=FALSE
        )
        MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;
        """

        logger.info(f"Loading {table_name}")

        cur.execute(f"TRUNCATE TABLE RAW.{table_name}")
        cur.execute(sql)

    except Exception as e:
        logger.error(e)
        raise          # <-- Important

    finally:
        cur.close()
        conn.close()