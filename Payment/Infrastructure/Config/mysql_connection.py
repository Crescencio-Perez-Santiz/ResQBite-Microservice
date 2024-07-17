from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()

class PaymentModel(Base):
    __tablename__ = 'Payment'

    id = Column(Integer, primary_key=True)
    name_uuid = Column(String(36), unique=True)
    amount = Column(Integer, nullable=False)
    description = Column(String(50), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name_uuid': self.name_uuid,
            'amount': self.amount,
            'description': self.description,
        }

class DBConnection:
    def __init__(self):
        load_dotenv()

        host = os.getenv('MYSQL_HOST')
        port = os.getenv('MYSQL_PORT')
        user = os.getenv('MYSQL_USER')
        password = os.getenv('MYSQL_PASSWORD')
        database = os.getenv('MYSQL_DATABASE')

        try:
            self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)
            print("Conexión exitosa a la base de datos con MySQL LISTA!")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")



