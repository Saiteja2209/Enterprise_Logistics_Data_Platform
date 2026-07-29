from database.connect_snowflake import get_connection
from logger.logger import logger
from datetime import datetime


def is_file_loaded(file):

    conn = get_connection()
    cur = conn.cursor()

    sql = """
    SELECT COUNT(*)
    FROM METADATA.LOAD_HISTORY
    WHERE "FILE_NAME" = %s
      AND "LAST_MODIFIED" = %s
      AND STATUS = 'SUCCESS'
    """

    try:
        last_modified = datetime.fromtimestamp(file.stat().st_mtime)
    except FileNotFoundError:
        last_modified = datetime.now()

    cur.execute(
        sql,
        (
            file.name,
            last_modified
        )
    )

    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return count > 0


def log_success(file, table_name, row_count):

    conn = get_connection()
    cur = conn.cursor()

    try:
        last_modified = datetime.fromtimestamp(file.stat().st_mtime)
    except FileNotFoundError:
        last_modified = datetime.now()

    sql = """
    INSERT INTO METADATA.LOAD_HISTORY
    (
        FILE_NAME,
        TABLE_NAME,
        LOAD_TIME,
        STATUS,
        ROW_COUNT,
        LAST_MODIFIED
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cur.execute(
        sql,
        (
            file.name,
            table_name,
            datetime.now(),
            "SUCCESS",
            row_count,
            last_modified
        )
    )

    conn.commit()

    logger.info(f"{file.name} logged successfully.")

    cur.close()
    conn.close()

def log_failure(file, table_name):

    conn = get_connection()
    cur = conn.cursor()

    try:
        last_modified = datetime.fromtimestamp(file.stat().st_mtime)
    except FileNotFoundError:
        last_modified = datetime.now()

    sql = """
    INSERT INTO METADATA.LOAD_HISTORY
    (
        FILE_NAME,
        TABLE_NAME,
        LOAD_TIME,
        STATUS,
        ROW_COUNT,
        LAST_MODIFIED
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    cur.execute(
        sql,
        (
            file.name,
            table_name,
            datetime.now(),
            "FAILED",
            0,
            last_modified
        )
    )

    conn.commit()

    logger.info(f"{file.name} logged as failed.")

    cur.close()
    conn.close()

