from datetime import datetime

from database.connect_snowflake import get_connection


def start_pipeline(pipeline_name):

    conn = get_connection()
    cur = conn.cursor()

    start_time = datetime.now()

    cur.execute(
        """
        INSERT INTO METADATA.PIPELINE_AUDIT
        (
            PIPELINE_NAME,
            START_TIME,
            STATUS,
            FILES_PROCESSED,
            FILES_FAILED
        )
        VALUES
        (%s,%s,'RUNNING',0,0)
        """,
        (pipeline_name, start_time)
    )

    cur.execute("SELECT MAX(RUN_ID) FROM METADATA.PIPELINE_AUDIT")

    run_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return run_id


def finish_pipeline(
    run_id,
    status,
    processed,
    failed,
    error_message=None
):

    conn = get_connection()
    cur = conn.cursor()

    end_time = datetime.now()

    cur.execute(
        """
        UPDATE METADATA.PIPELINE_AUDIT
        SET
            END_TIME=%s,
            STATUS=%s,
            FILES_PROCESSED=%s,
            FILES_FAILED=%s,
            DURATION_SECONDS=
                DATEDIFF(
                    SECOND,
                    START_TIME,
                    %s
                ),
            ERROR_MESSAGE=%s
        WHERE RUN_ID=%s
        """,
        (
            end_time,
            status,
            processed,
            failed,
            end_time,
            error_message,
            run_id
        )
    )

    conn.commit()

    cur.close()
    conn.close()