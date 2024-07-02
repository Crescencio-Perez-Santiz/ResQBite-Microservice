from dataclasses import dataclass, field
from enum import Enum
import uuid
from .Contact import Contact


class Location(Enum):
    TUXTLA = "TUXTLA"
    SUCHIAPA = "SUCHIAPA"


@dataclass
class User:
    uuid: str = field(default_factory=uuid.uuid4, init=False)
    email: str
    password: str
    location: Location
    contact: Contact