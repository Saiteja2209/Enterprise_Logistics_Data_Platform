import snowflake.connector
import config.config as config

def get_connection():
    return snowflake.connector.connect(
        user=config.USER,
        password=config.PASSWORD,
        account=config.ACCOUNT,
        warehouse=config.WAREHOUSE,
        database=config.DATABASE,
        schema=config.SCHEMA
    )