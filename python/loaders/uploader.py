from database.connect_snowflake import get_connection
from logger.logger import logger
from utils.file_discovery import get_csv_files


def upload_files():

    conn = get_connection()
    cur = conn.cursor()

    files = get_csv_files()

    logger.info(f"Found {len(files)} CSV files.")

    for file in files:

        sql = f"""
        PUT 'file://{file.as_posix()}'
        @UTIL.LOGISTICS_STAGE
        AUTO_COMPRESS=TRUE
        OVERWRITE=TRUE;
        """

        logger.info(f"Uploading {file.name}")

        cur.execute(sql)

    cur.close()
    conn.close()