from Infrastructure.database.models import Order as OrderModel, OrderItem as OrderItemModel
from Domain.entities.order import Order
from Domain.entities.order_item import OrderItem
from Infrastructure.database import db
from datetime import datetime, timedelta


def record_saga_event(event_type, data):
    db.session.execute(
        "INSERT INTO saga_events (event_type, data) VALUES (:event_type, :data)",
        {"event_type": event_type, "data": data},
    )
    db.session.commit()


def get_orders_by_store(store_uuid):
    print(f"Fetching orders for store_uuid: {store_uuid}")
    orders = OrderModel.query.filter_by(store_uuid=store_uuid).all()
    print(f"Orders fetched: {orders}")
    return [Order(order.orderUuid, order.store_uuid, order.user_uuid, order.status, order.total_price, order.created_at, order.updated_at) for order in orders]


def get_orders_by_store_last_month(store_uuid):
    one_month_ago = datetime.now() - timedelta(days=30)
    print(f"Fetching orders for store_uuid: {
        store_uuid} from date: {one_month_ago}")
    orders = OrderModel.query.filter_by(store_uuid=store_uuid).filter(
        OrderModel.created_at >= one_month_ago).all()
    print(f"Orders fetched: {orders}")
    return [Order(order.orderUuid, order.store_uuid, order.user_uuid, order.status, order.total_price, order.created_at, order.updated_at) for order in orders]


def get_finalized_orders_by_store(store_uuid):
    print(f"Fetching finalized orders for store_uuid: {store_uuid}")
    orders = OrderModel.query.filter_by(
        store_uuid=store_uuid, status='FINALIZADO').all()
    print(f"Orders fetched: {orders}")
    return [Order(order.orderUuid, order.store_uuid, order.user_uuid, order.status, order.total_price, order.created_at, order.updated_at) for order in orders]


def get_order_items_by_order(orderUuid):
    order_items = OrderItemModel.query.filter_by(
        orderOrderUuid=orderUuid).all()
    return [OrderItem(item.orderItemUuid, item.product_uuid, item.quantity, item.price, item.category, item.orderOrderUuid) for item in order_items]


def get_orders_by_status(store_uuid, status):
    print(f"Fetching orders for store_uuid: {
          store_uuid} with status: {status}")
    orders = OrderModel.query.filter_by(
        store_uuid=store_uuid, status=status).all()
    print(f"Orders fetched: {orders}")
    return [Order(order.orderUuid, order.store_uuid, order.user_uuid, order.status, order.total_price, order.created_at, order.updated_at) for order in orders]


def get_sales_by_category(store_uuid):
    print(f"Fetching sales by category for store_uuid: {store_uuid}")
    orders = OrderModel.query.filter_by(store_uuid=store_uuid).all()
    categories = {}
    for order in orders:
        items = get_order_items_by_order(order.orderUuid)
        for item in items:
            category = item.category
            if category in categories:
                categories[category] += item.quantity
            else:
                categories[category] = item.quantity
    print(f"Sales by category: {categories}")
    return categories


def get_sales_by_category_last_month(store_uuid):
    one_month_ago = datetime.now() - timedelta(days=30)
    print(f"Fetching sales by category for store_uuid: {
          store_uuid} from date: {one_month_ago}")
    orders = OrderModel.query.filter_by(store_uuid=store_uuid).filter(
        OrderModel.created_at >= one_month_ago).all()
    categories = {
        'Comida': {'quantity': 0, 'total_price': 0.0},
        'Lacteos': {'quantity': 0, 'total_price': 0.0},
        'Panaderia': {'quantity': 0, 'total_price': 0.0},
        'Pasteleria': {'quantity': 0, 'total_price': 0.0}
    }

    for order in orders:
        items = get_order_items_by_order(order.orderUuid)
        for item in items:
            category = item.category
            if category in categories:
                categories[category]['quantity'] += item.quantity
                categories[category]['total_price'] += item.price * \
                    item.quantity
            else:
                categories[category] = {
                    'quantity': item.quantity, 'total_price': item.price * item.quantity}
    print(f"Sales by category: {categories}")
    return categories


def get_best_selling_product(store_uuid):
    # Calcular la fecha de un mes atrás
    one_month_ago = datetime.now() - timedelta(days=30)

    # Filtrar órdenes del último mes
    orders = OrderModel.query.filter_by(store_uuid=store_uuid).filter(
        OrderModel.created_at >= one_month_ago).all()
    product_sales = {}
    for order in orders:
        items = get_order_items_by_order(order.orderUuid)
        for item in items:
            product = item.product_uuid
            if product in product_sales:
                product_sales[product] += item.quantity
            else:
                product_sales[product] = item.quantity
    best_selling_product = max(
        product_sales, key=product_sales.get) if product_sales else None
    return best_selling_product, product_sales.get(best_selling_product, 0) if best_selling_product else 0

# Funciones adicionales para manejo de transacciones con Saga


def begin_saga(event_type, data):
    record_saga_event(f"BEGIN_{event_type}", data)


def complete_saga(event_type, data):
    record_saga_event(f"COMPLETE_{event_type}", data)


def compensate_saga(event_type, data):
    record_saga_event(f"COMPENSATE_{event_type}", data)

# Ejemplo de cómo usar el patrón Saga en una transacción de ventas


def create_order_with_saga(order_data, order_items_data):
    try:
        begin_saga("CREATE_ORDER", order_data)

        # Crear el pedido
        order = OrderModel(**order_data)
        db.session.add(order)
        db.session.commit()

        # Crear los items del pedido
        for item_data in order_items_data:
            item_data["orderOrderUuid"] = order.orderUuid
            order_item = OrderItemModel(**item_data)
            db.session.add(order_item)

        db.session.commit()

        complete_saga("CREATE_ORDER", {"orderUuid": order.orderUuid})

        return order, order_items_data

    except Exception as e:
        db.session.rollback()
        compensate_saga("CREATE_ORDER", order_data)
        print(f"Error creating order: {e}")
        raise
