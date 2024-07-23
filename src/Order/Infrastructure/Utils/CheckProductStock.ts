import { connectRabbitMQ } from "../Config/RabbitMQConfig";

export const checkProductStock = async (
    product_uuid: string
): Promise<number> => {
    console.log(`Verificando stock para el producto: ${product_uuid}`);
    const connection = await connectRabbitMQ();
    const channel = await connection.createChannel();
    await channel.assertQueue("inventory");
    console.log("Conectado a la cola de inventario");

    return new Promise((resolve, reject) => {
        const timeout = setTimeout(() => {
            console.error(
                "Tiempo de espera agotado al verificar el stock del producto"
            );
            channel
                .close()
                .catch((err) => console.error("Error cerrando el canal:", err));
            connection
                .close()
                .catch((err) =>
                    console.error("Error cerrando la conexión:", err)
                );
            reject(
                new Error(
                    "Tiempo de espera agotado al verificar el stock del producto"
                )
            );
        }, 5000);

        channel.consume("inventory", (msg) => {
            if (msg !== null) {
                const message = JSON.parse(msg.content.toString());
                console.log(`Mensaje recibido: ${JSON.stringify(message)}`);
                if (
                    message.data &&
                    message.data.productData.product_uuid === product_uuid
                ) {
                    clearTimeout(timeout);
                    resolve(message.data.productData.quantity);
                    channel.ack(msg);
                    channel
                        .close()
                        .catch((err) =>
                            console.error("Error cerrando el canal:", err)
                        );
                    connection
                        .close()
                        .catch((err) =>
                            console.error("Error cerrando la conexión:", err)
                        );
                } else {
                    channel.nack(msg);
                }
            } else {
                clearTimeout(timeout);
                reject(new Error("No message received"));
                channel
                    .close()
                    .catch((err) =>
                        console.error("Error cerrando el canal:", err)
                    );
                connection
                    .close()
                    .catch((err) =>
                        console.error("Error cerrando la conexión:", err)
                    );
            }
        });
    });
};
