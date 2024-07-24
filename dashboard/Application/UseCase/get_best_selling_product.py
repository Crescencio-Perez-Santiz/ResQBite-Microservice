from Infrastructure.repositories.sales_repository import get_best_selling_product


def get_best_selling_product_usecase(store_uuid):
    product, sales = get_best_selling_product(store_uuid)
    return {'best_selling_product': product, 'sales': sales}
