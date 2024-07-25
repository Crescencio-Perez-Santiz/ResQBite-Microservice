import dotenv from "dotenv";

dotenv.config();

export const config = {
    db: {
        host: process.env.DB_HOST_MYSQL_STORE,
        port: process.env.DB_PORT_MYSQL_STORE,
        user: process.env.DB_USER_MYSQL_STORE,
        password: process.env.DB_PASSWORD_MYSQL_STORE,
        database: process.env.DB_DATABASE_MYSQL_STORE,
    },
    jwt: {
        secretKey: process.env.JWT_SECRET_KEY,
    },
    rabbitmq: {
        host: process.env.RABBITMQ_HOST,
        protocol: process.env.RABBITMQ_PROTOCOL,
        user: process.env.RABBITMQ_USER,
        password: process.env.RABBITMQ_PASS,
        port: process.env.RABBITMQ_PORT,
    },
};
