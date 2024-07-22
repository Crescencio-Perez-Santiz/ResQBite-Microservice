import { getRepository } from "typeorm";
import { OrderModel } from "./Models/OrderModel";
import { OrderItemModel } from "./Models/OrderItemsModel";
import { Order } from "../../Domain/Entities/Order";
import { OrderItem } from "../../Domain/Entities/OrderItem";

export class OrderRepository {
    private orderRepository = getRepository(OrderModel);
    private orderItemRepository = getRepository(OrderItemModel);

    async createOrder(order: Order): Promise<Order> {
        const orderModel = this.orderRepository.create({
            orderUuid: order.id,
            user_uuid: order.user_uuid,
            store_uuid: order.store_uuid,
            status: order.status,
            total_price: order.total_price,
            created_at: order.created_at,
            updated_at: order.updated_at,
            items: order.items.map((item) => ({
                orderItemUuid: item.id,
                product_uuid: item.product_uuid,
                quantity: item.quantity,
                price: item.price,
                order: { orderUuid: order.id },
            })),
        });

        await this.orderRepository.save(orderModel);
        return order;
    }

    async getOrderById(orderUuid: string): Promise<Order | null> {
        const orderModel = await this.orderRepository.findOne({
            where: { orderUuid },
            relations: ["items"],
        });

        if (!orderModel) {
            return null;
        }

        const order = new Order(
            orderModel.orderUuid,
            orderModel.user_uuid,
            orderModel.store_uuid,
            orderModel.status,
            orderModel.total_price,
            orderModel.created_at,
            orderModel.updated_at,
            orderModel.items.map(
                (item) =>
                    new OrderItem(
                        item.orderItemUuid,
                        item.product_uuid,
                        item.quantity,
                        item.price
                    )
            )
        );

        return order;
    }
}
