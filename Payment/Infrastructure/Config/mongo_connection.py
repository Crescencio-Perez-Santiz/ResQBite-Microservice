import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def mongo_connection():
    client = MongoClient(
        host=os.getenv('DB_HOST_MONGODB'),
        port=int(os.getenv('DB_PORT_MONGODB')),
        username=os.getenv('DB_USER_MONGODB'),
        password=os.getenv('DB_PASSWORD_MONGODB'),
        authSource='admin'
    )
    db = client[os.getenv('DB_DATABASE_MONGODB')]
    return db
