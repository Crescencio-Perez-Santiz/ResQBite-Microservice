import { getRepository } from "typeorm";
import { OrderModel } from "../../Infrastructure/Repositories/Models/OrderModel";
import { OrderItemModel } from "../../Infrastructure/Repositories/Models/OrderItemsModel";
import { ProductModel } from "../../Infrastructure/Repositories/Models/ProductModel";
import { Order } from "../../Domain/Entities/Order";
import { OrderItem } from "../../Domain/Entities/OrderItem";

export class OrderService {
    private orderRepository = getRepository(OrderModel);
    private orderItemRepository = getRepository(OrderItemModel);
    private productRepository = getRepository(ProductModel);

    async createOrder(order: Order): Promise<Order | null> {
        // Verificar stock
        for (const item of order.items) {
            const product = await this.productRepository.findOne({
                where: { product_uuid: item.product_uuid },
            });
            if (!product || product.quantity < item.quantity) {
                console.error(
                    `Stock insuficiente para el producto ${item.product_uuid}`
                );
                return null;
            }
        }

        // Reducir el stock
        for (const item of order.items) {
            const product = await this.productRepository.findOne({
                where: { product_uuid: item.product_uuid },
            });
            if (product) {
                product.quantity -= item.quantity;
                await this.productRepository.save(product);
            }
        }

        // Calcular el precio total
        const totalPrice = order.items.reduce(
            (total, item) => total + item.price * item.quantity,
            0
        );

        // Crear la orden
        const orderModel = this.orderRepository.create({
            orderUuid: order.id,
            user_uuid: order.user_uuid,
            store_uuid: order.store_uuid,
            status: "CREADO",
            total_price: totalPrice,
            created_at: new Date(),
            updated_at: new Date(),
            items: order.items.map((item) => ({
                orderItemUuid: item.id,
                product_uuid: item.product_uuid,
                quantity: item.quantity,
                price: item.price,
                order: { orderUuid: order.id },
            })),
        });

        await this.orderRepository.save(orderModel);

        // Enviar la orden a RabbitMQ

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
