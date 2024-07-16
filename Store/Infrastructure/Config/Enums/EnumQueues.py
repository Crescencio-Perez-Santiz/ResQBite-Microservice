from enum import Enum


class Queue(Enum):
    QUEUE_NEW_STORE = {
        'queue_name': 'StoreServiceSaga',
        'exchange_name': 'resqbite',
        'routing_key': 'new_store'
    }
