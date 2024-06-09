from DataBase.MySQLConnection import Base
from sqlalchemy import Column, String


class User(Base):
    __tablename__ = "users"

    uuid = Column(String(255), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    location = Column(String(50), nullable=True)
    full_name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "email": self.email,
            "location": self.location,
            "full_name": self.full_name,
            "address": self.address,
            "phone_number": self.phone_number,
        }
