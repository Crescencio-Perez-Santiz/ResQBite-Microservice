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
