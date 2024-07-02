from sqlalchemy import Column, String
from DataBase.MySQLConnection import Base


class Store(Base):
    __tablename__ = 'stores'

    uuid = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    rfc = Column(String(13), unique=True, nullable=False)
    image = Column(String(255), nullable=True)
    phone_number = Column(String(20), unique=True, nullable=False)
    opening_hours = Column(String(10), nullable=False)
    closing_hours = Column(String(10), nullable=False)
    street = Column(String(50), nullable=False)
    number = Column(String(10), nullable=False)
    neighborhood = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    reference = Column(String(255), nullable=True)

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "name": self.name,
            "rfc": self.rfc,
            "image": self.image,
            "phone_number": self.phone_number,
            "opening_hours": self.opening_hours,
            "closing_hours": self.closing_hours,
            "street": self.street,
            "number": self.number,
            "neighborhood": self.neighborhood,
            "city": self.city,
            "reference": self.reference
        }
