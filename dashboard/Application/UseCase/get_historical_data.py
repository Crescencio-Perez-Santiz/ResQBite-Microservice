from Infrastructure.repositories.sales_repository import get_orders_by_store


def get_historical_data(store_uuid):
    orders = get_orders_by_store(store_uuid)
    data = [{'date': order.created_at, 'total_price': order.total_price}
            for order in orders]
    return data
