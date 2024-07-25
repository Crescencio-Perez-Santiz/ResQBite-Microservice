import amqp from "amqplib";
import dotenv from "dotenv";

dotenv.config();

const {
    RABBITMQ_HOST,
    RABBITMQ_PROTOCOL,
    RABBITMQ_USER,
    RABBITMQ_PASS,
    RABBITMQ_PORT = "5672",
} = process.env;

export const connectRabbitMQ = async () => {
    console.log("Conectando a RabbitMQ...");
    const connection = await amqp.connect({
        protocol: RABBITMQ_PROTOCOL,
        hostname: RABBITMQ_HOST,
        port: parseInt(RABBITMQ_PORT, 10),
        username: RABBITMQ_USER,
        password: RABBITMQ_PASS,
    });
    console.log("Conexión a RabbitMQ exitosa");
    return connection;
};
