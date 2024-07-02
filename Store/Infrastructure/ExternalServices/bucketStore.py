import boto3
from botocore.client import Config
import dotenv
import os
dotenv.load_dotenv()

# Initialize a session using DigitalOcean Spaces.
session = boto3.session.Session()
client = session.client('s3',
                        region_name=os.getenv('S3_REGION'),
                        endpoint_url=os.getenv('S3_ENDPOINT_URL'),
                        aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
                        aws_secret_access_key=os.getenv('S3_SECRET_KEY'),
                        )


def send_file(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_name
    try:
        response = client.upload_file(
            file_name, bucket_name, object_name, ExtraArgs={'ACL': 'public-read'})
    except Exception as e:
        print(e)
        return False
