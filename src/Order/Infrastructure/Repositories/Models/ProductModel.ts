import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity("products")
export class ProductModel {
    @PrimaryGeneratedColumn("uuid")
    product_uuid!: string;

    @Column()
    store_uuid!: string;

    @Column()
    name!: string;

    @Column("decimal")
    price!: number;

    @Column("int")
    quantity!: number;

    @Column()
    description!: string;

    @Column()
    image_url!: string;

    @Column()
    category!: string;

    @Column({ type: "timestamp", default: () => "CURRENT_TIMESTAMP" })
    created_at!: Date;

    @Column({
        type: "timestamp",
        default: () => "CURRENT_TIMESTAMP",
        onUpdate: "CURRENT_TIMESTAMP",
    })
    updated_at!: Date;
}
