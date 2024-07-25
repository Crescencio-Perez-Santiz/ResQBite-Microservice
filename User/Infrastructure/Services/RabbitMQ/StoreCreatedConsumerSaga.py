import json
import logging
from Infrastructure.Config.RabbitMQSetup import setup_rabbitmq
from Infrastructure.Config.Enums.EnumsQueue import EnumQueues
from Infrastructure.Repositories.UserRepository import UserRepository

class StoreCreatedConsumerSaga:
    def __init__(self):
        self.channel = setup_rabbitmq(
            EnumQueues.QUEUE_NEW_STORE_BY_USER.value['queue'],
            EnumQueues.QUEUE_NEW_STORE_BY_USER.value['exchange'],
            EnumQueues.QUEUE_NEW_STORE_BY_USER.value['routing_key']
        )
        self.user_repository = UserRepository()

    def execute(self):
        try:
            self.channel.basic_consume(queue=EnumQueues.QUEUE_NEW_STORE_BY_USER.value['queue'],
                                       on_message_callback=self.callback,
                                       auto_ack=False)
            self.channel.start_consuming()
        except Exception as e:
            logging.error(f"Error on consume queue: {e}")

    def callback(self, ch, method, properties, body):
        store = json.loads(body)
        logging.info(f"Store received: {store}")

        user_uuid = store.get('user_uuid')
        store_uuid = store.get('uuid')

        if not user_uuid or not store_uuid:
            logging.error(
                "Invalid message format: 'user_uuid' or 'uuid' is missing")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            return

        user = self.user_repository.find_by_uuid(user_uuid)
        if user:
            self.update_user_with_store_uuid(user_uuid, store_uuid)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            logging.error(f"User {user_uuid} not found in the database")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def update_user_with_store_uuid(self, user_uuid, store_uuid):
        user = self.user_repository.find_by_uuid(user_uuid)
        if user:
            user.store_uuid = store_uuid
            self.user_repository.update_uuid(user_uuid, store_uuid)
            logging.info(
                f"User {user_uuid} updated with store UUID {store_uuid}")
        else:
            logging.error(f"User {user_uuid} not found")
