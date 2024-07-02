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
