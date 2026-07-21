# Script to upload data files to Snowflake stage
import os
from connect_snowflake import get_connection

# Change this to your project path
DATA_FOLDER = r"D:\Sai Teja Project\Enterprise_Logistics_Data_Platform\data"

conn = get_connection()
cur = conn.cursor()

file_path = os.path.join(DATA_FOLDER, "customers.csv")

sql = f"""
PUT file://{file_path}
@UTIL.LOGISTICS_STAGE
AUTO_COMPRESS=TRUE
OVERWRITE=TRUE;
"""

cur.execute(sql)

print("customers.csv uploaded successfully!")

cur.close()
conn.close()