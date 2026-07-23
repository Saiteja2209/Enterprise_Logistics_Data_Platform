from database.connect_snowflake import get_connection
from logger.logger import logger

TABLES = [
    "CUSTOMERS",
    "PRODUCTS",
    "WAREHOUSES",
    "DELIVERY_PARTNERS",
    "ORDERS",
    "ORDER_ITEMS",
    "GPS_TRACKING"
]


def validate():

    conn = get_connection()
    cur = conn.cursor()

    print("\n========== ROW COUNTS ==========\n")

    for table in TABLES:

        cur.execute(f"SELECT COUNT(*) FROM RAW.{table}")

        count = cur.fetchone()[0]

        

        logger.info(f"{table} contains {count} rows")

    cur.close()
    conn.close()