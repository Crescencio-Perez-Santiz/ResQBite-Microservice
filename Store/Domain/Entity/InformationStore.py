from dataclasses import dataclass


@dataclass
class InformationStore:
    url_image: str
    phone_number: str
    opening_hours: str
    closing_hours: str

    def to_dict(self):
        return {
            'url_image': self.url_image,
            'phone_number': self.phone_number,
            'opening_hours': self.opening_hours,
            'closing_hours': self.closing_hours
        }
