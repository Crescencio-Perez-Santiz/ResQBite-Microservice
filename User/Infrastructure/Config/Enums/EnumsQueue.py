from enum import Enum


class EnumQueues (Enum):

    QUEUE_NEW_STORE_BY_USER = {
        "queue": "new_store_by_user",
        "exchange": "resqbite",
        "routing_key": "new_store"
    }
