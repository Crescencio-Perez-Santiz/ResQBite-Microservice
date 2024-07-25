import threading
from Infrastructure.Services.RabbitMQ.StoreCreatedConsumerSaga import StoreCreatedConsumerSaga

create_store_by_user = StoreCreatedConsumerSaga()


def init_rabbitmq():
    threading.Thread(target=create_store_by_user.execute, args=()).start()
