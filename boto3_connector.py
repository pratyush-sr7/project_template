import os
from dotenv import load_dotenv
import boto3

load_dotenv()

AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY_ID = os.getenv("AWS_SECRET_KEY_ID")

class Boto3:
  client = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_key_id=AWS_SECRET_KEY_ID)
