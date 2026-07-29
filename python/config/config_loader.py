from database.connect_snowflake import get_connection


def get_table_config(table_name):

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            SELECT PRIMARY_KEY,
                   LOAD_TYPE,
                   ACTIVE
            FROM METADATA.TABLE_CONFIG
            WHERE LOWER(TABLE_NAME) = LOWER(%s)
            """,
            (table_name,)
        )

        row = cur.fetchone()
        if row is None:
            raise ValueError(
                f"No configuration found for table {table_name}"
            )

        return {
            "primary_key": row[0],
            "load_type": row[1],
            "active": row[2]
        }

    finally:
        cur.close()
        conn.close()