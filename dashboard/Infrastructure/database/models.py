from Infrastructure.database.db import db


class Order(db.Model):
    __tablename__ = 'orders'
    orderUuid = db.Column(db.String, primary_key=True)
    store_uuid = db.Column(db.String)
    user_uuid = db.Column(db.String)
    status = db.Column(db.String)
    total_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


class OrderItem(db.Model):
    __tablename__ = 'order_items'
    orderItemUuid = db.Column(db.String, primary_key=True)
    product_uuid = db.Column(db.String)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    category = db.Column(db.String)
    orderOrderUuid = db.Column(db.String, db.ForeignKey('orders.orderUuid'))
