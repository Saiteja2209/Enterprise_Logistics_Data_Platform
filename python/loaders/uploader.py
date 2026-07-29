from database.connect_snowflake import get_connection
from logger.logger import logger
from utils.file_manager import move_to_archive, move_to_failed


def upload_file(file):

    conn = get_connection()
    cur = conn.cursor()

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
        raise

    finally:
        cur.close()
        conn.close()
