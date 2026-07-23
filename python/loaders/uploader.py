from database.connect_snowflake import get_connection
from logger.logger import logger
from utils.file_discovery import get_csv_files
from utils.file_manager import move_to_archive, move_to_failed


def upload_files():

    conn = get_connection()
    cur = conn.cursor()

    files = get_csv_files()

    logger.info(f"Found {len(files)} CSV files.")

    for file in files:

        try:

            sql = f"""
            PUT 'file://{file.as_posix()}'
            @UTIL.LOGISTICS_STAGE
            AUTO_COMPRESS=TRUE
            OVERWRITE=TRUE;
            """

            logger.info(f"Uploading {file.name}")

            cur.execute(sql)

            logger.info(f"{file.name} uploaded")

        except Exception as e:
            logger.error(e)

    cur.close()
    conn.close()
