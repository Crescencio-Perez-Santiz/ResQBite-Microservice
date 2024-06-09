from dataclasses import dataclass


@dataclass
class Contact:
    full_name: str
    address: str
    phone_number: str
