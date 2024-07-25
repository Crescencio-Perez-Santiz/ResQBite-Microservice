from Infrastructure.repositories.sales_repository import get_sales_by_category_last_month


def get_sales_by_category_usecase(store_uuid):
    sales_by_category = get_sales_by_category_last_month(store_uuid)
    return sales_by_category
