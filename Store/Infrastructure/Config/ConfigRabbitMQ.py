import pika
import os
from dotenv import load_dotenv
import logging

# Configuración de logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

# Parámetros de conexión
hostname = os.getenv('RABBITMQ_HOST')
user = os.getenv('RABBITMQ_USER')
password = os.getenv('RABBITMQ_PASS')
port = int(os.getenv('RABBITMQ_PORT'))


def setup_rabbitmq(queue_name, exchange_name, routing_key):
    try:
        credentials = pika.PlainCredentials(user, password)
        parameters = pika.ConnectionParameters(
            hostname, port, '/', credentials)
        logger.debug(f'Connection parameters: {parameters}')

        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        channel.exchange_declare(
            exchange=exchange_name, exchange_type='direct', durable=True)

        channel.queue_declare(queue=queue_name, durable=True)
        channel.queue_bind(exchange=exchange_name,
                           queue=queue_name, routing_key=routing_key)
        return channel
    except Exception as e:
        logger.error(f"Error al conectar a RabbitMQ: {e}", exc_info=True)
        raise
