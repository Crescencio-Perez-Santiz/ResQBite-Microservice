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

    def send_store_info(self, store_info):
        message = json.dumps(store_info)
        self.channel.basic_publish(
            exchange=self.exchange_name, routing_key=self.routing_key, body=message)
        print(f" [x] Sent {message}")
