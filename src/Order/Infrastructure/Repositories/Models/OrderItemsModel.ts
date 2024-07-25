import { Entity, PrimaryGeneratedColumn, Column, ManyToOne } from "typeorm";
import { OrderModel } from "./OrderModel";

@Entity("order_items")
export class OrderItemModel {
    @PrimaryGeneratedColumn("uuid")
    orderItemUuid!: string;

    @Column()
    product_uuid!: string;

    @Column("int")
    quantity!: number;

    @Column("decimal")
    price!: number;

    @Column()
    category!: string;

    @ManyToOne(() => OrderModel, (order) => order.items)
    order!: OrderModel;
}
