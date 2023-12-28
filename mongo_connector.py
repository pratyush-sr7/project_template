import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_CLIENT = os.getenv("MONGO_CLIENT")

class Mongo:
  client = MongoClient(MONGO_CLIENT)
