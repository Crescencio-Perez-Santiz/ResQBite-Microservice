from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import pymysql

Base = declarative_base()


class MySQLConnection:
    def __init__(self):
        load_dotenv()

        host = os.getenv('DB.HOST_MYSQL_STORE')
        port = os.getenv('DB.PORT_MYSQL_STORE')
        user = os.getenv('DB.USER_MYSQL_STORE')
        password = os.getenv('DB.PASSWORD_MYSQL_STORE')
        database = os.getenv('DB.DATABASE_MYSQL_STORE')

        try:
            conn = pymysql.connect(host=host, port=int(
                port), user=user, password=password)
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            conn.commit()
            conn.close()

            self.engine = create_engine(
                f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)
            print("Connection to MySQL database successful")
        except Exception as e:
            print("Error connecting to MySQL database")
            print(e)
            self.Session = None
