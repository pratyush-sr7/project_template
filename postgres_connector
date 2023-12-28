import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")

class Postgres:
  con = psycopg2.connect(host=POSTGRES_HOST,port=SNOWFLAKE_PORT,user=SNOWFLAKE_USER,password=SNOWFLAKE_PASSWORD,database=SNOWFLAKE_DATABASE)
  cur = con.cursor()
