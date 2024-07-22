import { getRepository } from "typeorm";
import { OrderModel } from "../../Infrastructure/Repositories/Models/OrderModel";
import { OrderItemModel } from "../../Infrastructure/Repositories/Models/OrderItemsModel";
import { checkProductStock } from "../../Infrastructure/Utils/CheckProductStock";
import { publishOrderCreatedEvent } from "../../Infrastructure//Events/Publishers";
import { Order } from "../../Domain/Entities/Order";
import { OrderItem } from "../../Domain/Entities/OrderItem";
import jwt from "jsonwebtoken";
import { config } from "../../Infrastructure/Config/Config";

export const createOrder = async (decoded: any, orderData: any) => {
    console.log("Ejecutando caso de uso de creación de órdenes");
    const orderRepository = getRepository(OrderModel);
    const orderItemRepository = getRepository(OrderItemModel);

    const user_uuid = decoded.sub;

    const order = new OrderModel();
    order.user_uuid = user_uuid;
    order.status = orderData.status;
    order.total_price = 0; // Inicializamos el precio total en 0
    order.items = [];

    console.log("Iniciando la creación de ítems de la orden");
    for (const store of orderData.stores) {
        for (const item of store.item_list) {
            console.log(`Procesando item: ${JSON.stringify(item)}`);
            const stock = await checkProductStock(item.product_uuid);
            if (stock < item.quantity) {
                throw new Error(
                    `Not enough stock for product ${item.product_uuid}`
                );
            }

            const orderItem = new OrderItemModel();
            orderItem.product_uuid = item.product_uuid;
            orderItem.quantity = item.quantity;
            orderItem.price = item.price;
            order.total_price += item.price * item.quantity;

            await orderItemRepository.save(orderItem);
            console.log(`Item guardado: ${JSON.stringify(orderItem)}`);
            order.items.push(orderItem);
        }
    }

    console.log("Guardando la orden en la base de datos");
    await orderRepository.save(order);
    console.log("Orden guardada en la base de datos");

    const domainOrder = new Order(
        order.orderUuid,
        order.user_uuid,
        order.store_uuid,
        order.status,
        order.total_price,
        order.created_at,
        order.updated_at,
        order.items.map(
            (item) =>
                new OrderItem(
                    item.orderItemUuid,
                    item.product_uuid,
                    item.quantity,
                    item.price
                )
        )
    );

    console.log("Publicando evento de creación de orden");
    await publishOrderCreatedEvent(domainOrder);

    return order.orderUuid;
};
