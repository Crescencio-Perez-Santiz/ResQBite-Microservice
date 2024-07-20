import amqp from 'amqplib';
import { config } from 'dotenv';

config();

const RABBITMQ_URL = `amqps://${process.env.RABBITMQ_USER}:${process.env.RABBITMQ_PASSWORD}@${process.env.RABBITMQ_HOST}:${process.env.RABBITMQ_PORT}`;

let channel: amqp.Channel;

const connect = async () => {
  try {
    const connection = await amqp.connect(RABBITMQ_URL, {
      // Configuración adicional para SSL/TLS si es necesario
      // cert: fs.readFileSync('path/to/cert.pem'),
      // key: fs.readFileSync('path/to/key.pem'),
      // ca: [fs.readFileSync('path/to/ca.pem')]
    });
    channel = await connection.createChannel();
    console.log('Connected to RabbitMQ');
  } catch (error) {
    console.error('Failed to connect to RabbitMQ:', error);
    throw error;
  }
};

const getChannel = () => channel;

export { connect, getChannel };
