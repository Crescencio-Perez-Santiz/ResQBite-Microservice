class Order:
    def __init__(self, orderUuid, store_uuid, user_uuid, status, total_price, created_at, updated_at):
        self.orderUuid = orderUuid
        self.store_uuid = store_uuid
        self.user_uuid = user_uuid
        self.status = status
        self.total_price = total_price
        self.created_at = created_at
        self.updated_at = updated_at
