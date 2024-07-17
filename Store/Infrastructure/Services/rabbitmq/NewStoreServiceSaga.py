import json
from Infrastructure.Config.ConfigRabbitMQ import setup_rabbitmq
from Infrastructure.Config.Enums.EnumQueues import Queue


class NewStoreServiceSaga:
    def __init__(self):
        self.queue_name = Queue.QUEUE_NEW_STORE.value['queue_name']
        self.exchange_name = Queue.QUEUE_NEW_STORE.value['exchange_name']
        self.routing_key = Queue.QUEUE_NEW_STORE.value['routing_key']
        self.channel = setup_rabbitmq(
            self.queue_name, self.exchange_name, self.routing_key)

    # necestiamos crear un evento en el que cuando se cree tienda (la bd ya debe de estar llena con todos los datos necesarion es cuando se activa el evento para que en el microservicio de usuario aparezca la tienda creada)

    def send_store_info(self, store_info):

        store_info = self.store_to_dict(store_info)

        message = json.dumps(store_info)
        try:
            self.channel.basic_publish(
                exchange=self.exchange_name, routing_key=self.routing_key, body=message)
        except Exception as e:
            Exception("Error sending message to RabbitMQ")

    def store_to_dict(self, store):
        return {
            'uuid': str(store.uuid),
            'name': store.name,
            'rfc': store.rfc,
            'address': {
                'street': store.address.street,
                'number': store.address.number,
                'neighborhood': store.address.neighborhood,
                'city': store.address.city,
                'reference': store.address.reference,
            },
            'information': {
                'url_image': store.information.url_image,
                'phone_number': store.information.phone_number,
                'opening_hours': store.information.opening_hours,
                'closing_hours': store.information.closing_hours,
            }
        }
