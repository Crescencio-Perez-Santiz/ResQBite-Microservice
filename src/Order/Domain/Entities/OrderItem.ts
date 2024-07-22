export class OrderItem {
    id: string;
    product_uuid: string;
    quantity: number;
    price: number;

    constructor(
        id: string,
        product_uuid: string,
        quantity: number,
        price: number
    ) {
        this.id = id;
        this.product_uuid = product_uuid;
        this.quantity = quantity;
        this.price = price;
    }
}
