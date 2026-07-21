# Script to validate loaded data in Snowflake
from connect_snowflake import get_connection

conn = get_connection()

cur = conn.cursor()

cur.execute("SELECT CURRENT_DATABASE(), CURRENT_SCHEMA(), CURRENT_WAREHOUSE();")

print(cur.fetchone())

cur.close()
conn.close()