import "reflect-metadata";
import express from "express";
import morgan from "morgan";
import { connectDB } from "./Database/MYSQLConnection";
import orderRoutes from "./Order/Infrastructure/Routes/Router";
import { consumeInventoryUpdates } from "./Order/Infrastructure/Services/InventoryConsumer";
import dotenv from "dotenv";

dotenv.config();

const app = express();

app.use(morgan("dev"));

app.use(express.json());
app.use("/api", orderRoutes);

const startServer = async () => {
    const dbConnection = await connectDB();
    if (dbConnection) {
        await consumeInventoryUpdates();
        app.listen(5003, () => {
            console.log("Server is running on port 5003");
        });
    } else {
        console.error(
            "No se pudo conectar a la base de datos. El servidor no se iniciará."
        );
    }
};

startServer();
