import { Entity, PrimaryGeneratedColumn, Column, OneToMany } from "typeorm";
import { OrderItemModel } from "./OrderItemsModel";

@Entity("orders")
export class OrderModel {
    @PrimaryGeneratedColumn("uuid")
    orderUuid!: string;

    @Column()
    user_uuid!: string;

    @Column()
    store_uuid!: string;

    @Column()
    status!: string;

    @Column("decimal")
    total_price!: number;

    @Column({ type: "timestamp", default: () => "CURRENT_TIMESTAMP" })
    created_at!: Date;

    @Column({
        type: "timestamp",
        default: () => "CURRENT_TIMESTAMP",
        onUpdate: "CURRENT_TIMESTAMP",
    })
    updated_at!: Date;

    @OneToMany(() => OrderItemModel, (item) => item.order, { cascade: true })
    items!: OrderItemModel[];
}
