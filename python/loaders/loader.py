from database.connect_snowflake import get_connection
from logger.logger import logger
from utils.file_discovery import get_csv_files

def load_tables():

    conn = get_connection()
    cur = conn.cursor()

    files = get_csv_files()

    for file in files:

        table = file.stem.upper()

        sql = f"""
        COPY INTO RAW.{table}
        FROM @UTIL.LOGISTICS_STAGE/{file.name}.gz
        FILE_FORMAT=(FORMAT_NAME='UTIL.CSV_FORMAT', ERROR_ON_COLUMN_COUNT_MISMATCH=FALSE)
        ON_ERROR = 'CONTINUE';
        """

        logger.info(f"Loading {table}")

        cur.execute(sql)

    cur.close()
    conn.close()