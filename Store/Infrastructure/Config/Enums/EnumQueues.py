from enum import Enum


class Queue(Enum):
    QUEUE_NEW_STORE = {
        'queue_name': 'new_store_by_user',
        'exchange_name': 'resqbite',
        'routing_key': 'new_store'
    }
