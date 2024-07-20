import { getChannel } from '../../Infrastructure/Config/rabbitMQConfig';

const QUEUE_NAME = process.env.RABBITMQ_QUEUE;

if (!QUEUE_NAME) {
  throw new Error('RABBITMQ_QUEUE environment variable is not defined');
}

export const publishToQueue = async (message: any) => {
  const channel = getChannel();
  if (channel) {
    await channel.assertQueue(QUEUE_NAME, { durable: true });
    channel.sendToQueue(QUEUE_NAME, Buffer.from(JSON.stringify(message)), { persistent: true });
    console.log('Message sent to queue:', message);
  } else {
    console.error('Channel is not available');
  }
};
