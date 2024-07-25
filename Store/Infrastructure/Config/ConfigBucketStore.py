import boto3
import dotenv
import os
dotenv.load_dotenv()

session = boto3.session.Session()
client = session.client('s3',
                        region_name=os.getenv('S3_REGION'),
                        endpoint_url=os.getenv('S3_ENDPOINT_URL'),
                        aws_access_key_id=os.getenv('S3_ACCESS_KEY'),
                        aws_secret_access_key=os.getenv('S3_SECRET_KEY'),
                        )
