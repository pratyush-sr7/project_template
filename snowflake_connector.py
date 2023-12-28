import os
from dotenv import load_dotenv
import snowflake.connector

load_dotenv()

class Snowflake:
  con = snowflake.connector.connect(host=SNOWFLAKE_HOST,account=SNOWFLAKE_ACCOUNT,user=SNOWFLAKE_USER,password=SNOWFLAKE_PASSWORD,role=SNOWFLAKE_ROLE,warehouse=SNOWFLAKE_WAREHOUSE)
  cur = con.cursor()
