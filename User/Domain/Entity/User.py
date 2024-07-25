from dataclasses import dataclass, field
from enum import Enum
import uuid
from .Contact import Contact


class Location(Enum):
    TUXTLA = "TUXTLA"
    SUCHIAPA = "SUCHIAPA"


class user_type_suscriber(Enum):
    COMUN = "COMUN"
    PREMIUM = "PREMIUM"

@dataclass
class User:
    uuid: str = field(default_factory=uuid.uuid4, init=False)
    email: str
    password: str
    location: Location
    user_type_suscriber: user_type_suscriber
    contact: Contact