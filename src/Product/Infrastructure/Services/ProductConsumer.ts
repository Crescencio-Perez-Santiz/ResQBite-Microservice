import { getChannel } from '../../Infrastructure/Config/rabbitMQConfig';
// import { CreateProductUseCase } from '../UseCases/CreateProductUseCase';
import { MySQLProductRepository } from '../../Infrastructure/Persistence/MysqlProductRepository';

const QUEUE_NAME = process.env.RABBITMQ_QUEUE;

if (!QUEUE_NAME) {
  throw new Error('RABBITMQ_QUEUE environment variable is not defined');
}

export const consumeQueue = async () => {
  const channel = getChannel();
  const repository = new MySQLProductRepository();
  // const createProductUseCase = new CreateProductUseCase(repository);

  if (channel) {
    await channel.assertQueue(QUEUE_NAME, { durable: true });
    channel.consume(QUEUE_NAME, async (message) => {
      if (message) {
        try {
          const { action, productData } = JSON.parse(message.content.toString());

          if (action !== 'create') {
            console.error('Failed to process message: No action specified', JSON.stringify(message.content.toString()));
            channel.nack(message, false, false); // Descartar el mensaje si no tiene acción
            return;
          }

          // const result = await createProductUseCase.execute(productData);
          // if (!('error' in result)) {
          //   channel.ack(message);
          //   console.log('Message processed and acknowledged:', productData);
          // } else {
          //   console.error('Failed to create product:', result.error);
          // }
        } catch (error) {
          console.error('Failed to process message:', error);
          channel.nack(message, false, false); // Descartar el mensaje si hubo un error en el procesamiento
        }
      }
    });
  } else {
    console.error('Channel is not available');
  }
};
