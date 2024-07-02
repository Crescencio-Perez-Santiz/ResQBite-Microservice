from dataclasses import dataclass


@dataclass
class InformationStore:
    url_image: str
    phone_number: str
    opening_hours: str
    closing_hours: str
