import { connectRabbitMQ } from "../Config/RabbitMQConfig";
import { Order } from "../../Domain/Entities/Order";

export const publishOrderCreatedEvent = async (order: Order) => {
    try {
        const connection = await connectRabbitMQ();
        const channel = await connection.createChannel();
        await channel.assertExchange("orders", "topic", { durable: true });
        await channel.assertQueue("orders", { durable: true }); // Asegurando la creación de la cola
        await channel.bindQueue("orders", "orders", "order.created"); // Vinculando la cola al intercambio

        const orderData = {
            order_uuid: order.id,
            user_uuid: order.user_uuid,
            store_uuid: order.store_uuid,
            status: order.status,
            total_price: order.total_price,
            created_at: order.created_at,
            updated_at: order.updated_at,
            items: order.items.map((item: any) => ({
                product_uuid: item.product_uuid,
                quantity: item.quantity,
                price: item.price,
            })),
        };

        console.log("Publicando mensaje en RabbitMQ:", orderData);
        channel.publish(
            "orders",
            "order.created",
            Buffer.from(JSON.stringify(orderData))
        );
        console.log("Order created event published");

        // Enviar a inventoryUpdates
        await channel.assertQueue("inventoryUpdates");
        channel.sendToQueue(
            "inventoryUpdates",
            Buffer.from(JSON.stringify(orderData))
        );
        console.log("Mensaje enviado a inventoryUpdates:", orderData);

        await channel.close();
        await connection.close();
    } catch (error) {
        console.error(
            "Error publicando el evento de creación de la orden:",
            error
        );
    }
};
