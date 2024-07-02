from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    last_name: str
    address: str
    phone_number: str
