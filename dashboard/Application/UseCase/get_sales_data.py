from Infrastructure.repositories.sales_repository import get_orders_by_store_last_month, get_order_items_by_order


def get_sales_data(store_uuid):
    orders = get_orders_by_store_last_month(store_uuid)
    total_products_sold = 0

    for order in orders:
        items = get_order_items_by_order(order.orderUuid)
        total_products_sold += sum(item.quantity for item in items)

    return {'total_products_sold': total_products_sold}
