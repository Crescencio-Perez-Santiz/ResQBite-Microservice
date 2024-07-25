import { createConnection, Connection } from "typeorm";
import { config } from "dotenv";
import { OrderModel } from "../Order/Infrastructure/Repositories/Models/OrderModel";
import { OrderItemModel } from "../Order/Infrastructure/Repositories/Models/OrderItemsModel";
import { ProductModel } from "../Order/Infrastructure/Repositories/Models/ProductModel";
import mysql from "mysql2/promise";

config();

export const connectDB = async (): Promise<Connection | null> => {
    const host = process.env.DB_HOST_MYSQL_STORE;
    const port = Number(process.env.DB_PORT_MYSQL_STORE);
    const username = process.env.DB_USER_MYSQL_STORE;
    const password = process.env.DB_PASSWORD_MYSQL_STORE;
    const database = process.env.DB_DATABASE_MYSQL_STORE;

    try {
        const connection = await mysql.createConnection({
            host,
            port,
            user: username,
            password,
        });
        await connection.query(
            `CREATE DATABASE IF NOT EXISTS \`${database}\`;`
        );
        await connection.end();

        const dbConnection = await createConnection({
            type: "mysql",
            host,
            port,
            username,
            password,
            database,
            entities: [OrderModel, OrderItemModel, ProductModel],
            synchronize: true,
        });

        console.log("Conexión exitosa a la base de datos con MySQL LISTA!");
        return dbConnection;
    } catch (error) {
        console.error("Error al conectar a la base de datos:", error);
        return null;
    }
};
