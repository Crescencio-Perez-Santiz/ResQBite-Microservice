import { Request, Response } from "express";
import { createOrder } from "../../Application/UseCases/CreateOrderUseCase";
import jwt from "jsonwebtoken";
import dotenv from "dotenv";

dotenv.config();

export const createOrderController = async (req: Request, res: Response) => {
    console.log("Entrando al controlador de creación de órdenes");
    try {
        const token = req.headers.authorization?.split(" ")[1];
        if (!token) {
            return res.status(401).json({ error: "Token required" });
        }

        const secret = process.env.JWT_SECRET_KEY;
        if (!secret) {
            throw new Error("JWT secret key is not defined");
        }

        const decoded = jwt.verify(token, secret);
        console.log("Token verificado:", decoded);

        if (!req.body) {
            return res.status(400).json({ error: "Request body is required" });
        }

        const orderData = req.body.orderData;
        console.log("Datos de la orden recibidos:", orderData);

        const order_id = await createOrder(decoded, orderData);
        console.log("Orden creada con ID:", order_id);

        return res.status(201).json({ order_uuid: order_id });
    } catch (error: any) {
        console.error(
            "Error en el controlador de creación de órdenes:",
            error.message
        );
        return res.status(400).json({ error: error.message });
    }
};
