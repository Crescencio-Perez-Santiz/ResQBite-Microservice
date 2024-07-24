class OrderItem:
    def __init__(self, orderItemUuid, product_uuid, quantity, price, category, orderOrderUuid):
        self.orderItemUuid = orderItemUuid
        self.product_uuid = product_uuid
        self.quantity = quantity
        self.price = price
        self.category = category
        self.orderOrderUuid = orderOrderUuid
