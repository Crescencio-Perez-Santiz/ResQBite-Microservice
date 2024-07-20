from DataBase.MySQLConnection import Base
from sqlalchemy import Column, String


class User(Base):
    __tablename__ = "users"

    uuid = Column(String(255), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    location = Column(String(50), nullable=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    store_uuid = Column(String(255), nullable=True, unique=True)

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "email": self.email,
            "location": self.location,
            "name": self.name,
            "last_name": self.last_name,
            "address": self.address,
            "phone_number": self.phone_number,
            "user_uuid": self.store_uuid
        }
