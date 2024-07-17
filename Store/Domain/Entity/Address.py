from dataclasses import dataclass
from enum import Enum


class City(Enum):
    TUXTLA = "TUXTLA",
    SUCHIAPA = "SUCHIAPA",


@dataclass
class Address:
    street: str
    number: str
    neighborhood: str
    city: City
    reference: str

    def to_dict(self):
        return {
            'street': self.street,
            'number': self.number,
            'neighborhood': self.neighborhood,
            'city': self.city,
            'reference': self.reference
        }
