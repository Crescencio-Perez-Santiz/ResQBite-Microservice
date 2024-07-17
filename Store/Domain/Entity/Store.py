from dataclasses import dataclass, field
from .Address import Address
from .InformationStore import InformationStore
import uuid


@dataclass
class Store:

    uuid: str = field(default_factory=uuid.uuid4, init=False)
    name: str
    rfc: str
    address: Address
    information: InformationStore

    def to_dict(self):
        return {
            'name': self.name,
            'rfc': self.rfc,
            'address': self.address.to_dict() if self.address else None,
            'information': self.information.to_dict() if self.information else None,
            'uuid': self.uuid
        }
