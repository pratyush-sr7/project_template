import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

ELASTICSEARCH_IP = os.getenv("ELASTICSEARCH_IP")
ELASTICSEARCH_PORT = os.getenv("ELASTICSEARCH_PORT")

class Elasticsearch:
  client = Elasticsearch(ELASTICSEARCH_IP,ELASTICSEARCH_PORT)
