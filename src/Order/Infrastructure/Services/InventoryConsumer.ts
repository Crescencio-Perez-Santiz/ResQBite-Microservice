import { connectRabbitMQ } from "../Config/RabbitMQConfig";
import {
    handleProductCreationOrUpdate,
    deleteProduct,
} from "../../Domain/Services/ProductService";

export const consumeInventoryUpdates = async () => {
    const connection = await connectRabbitMQ();
    const channel = await connection.createChannel();
    await channel.assertQueue("productService");

    channel.consume("productService", async (msg) => {
        if (msg !== null) {
            try {
                const message = JSON.parse(msg.content.toString());
                console.log(`Mensaje recibido: ${JSON.stringify(message)}`);

                if (message.data && message.data.action) {
                    const action = message.data.action;
                    const productData = message.data.productData;

                    console.log(`Acción recibida: ${action}`);

                    switch (action) {
                        case "createProduct":
                        case "updateProduct":
                            console.log(
                                "Llamando a handleProductCreationOrUpdate"
                            );
                            await handleProductCreationOrUpdate(productData);
                            break;
                        default:
                            console.log(`Acción desconocida: ${action}`);
                    }
                } else if (message.action && message.action === "delete") {
                    const productId = message.productId;
                    console.log(
                        `Llamando a deleteProduct para el UUID: ${productId}`
                    );
                    await deleteProduct(productId);
                } else {
                    console.log("Mensaje sin acción válida o datos");
                }

                // Acknowledge the message
                channel.ack(msg);
            } catch (error) {
                console.error("Error procesando mensaje:", error);
                // If there is an error processing the message, we can nack the message
                channel.nack(msg, false, false);
            }
        }
    });

    console.log("Consumidor de actualizaciones de inventario iniciado");
};
