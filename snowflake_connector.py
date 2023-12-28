import os
from dotenv import load_dotenv
import snowflake.connector

load_dotenv()

SNOWFLAKE_HOST = os.getenv("SNOWFLAKE_HOST")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ROLE = os.getenv("SNOWFLAKE_ROLE")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")

class Snowflake:
  con = snowflake.connector.connect(host=SNOWFLAKE_HOST,account=SNOWFLAKE_ACCOUNT,user=SNOWFLAKE_USER,password=SNOWFLAKE_PASSWORD,role=SNOWFLAKE_ROLE,warehouse=SNOWFLAKE_WAREHOUSE)
  cur = con.cursor()
