import { OrderItem } from "./OrderItem";

export class Order {
    id: string;
    user_uuid: string;
    store_uuid: string;
    status: string;
    total_price: number;
    created_at: Date;
    updated_at: Date;
    items: OrderItem[];

    constructor(
        id: string,
        user_uuid: string,
        store_uuid: string,
        status: string,
        total_price: number,
        created_at: Date,
        updated_at: Date,
        items: OrderItem[]
    ) {
        this.id = id;
        this.user_uuid = user_uuid;
        this.store_uuid = store_uuid;
        this.status = status;
        this.total_price = total_price;
        this.created_at = created_at;
        this.updated_at = updated_at;
        this.items = items;
    }
}
