from flask import Blueprint, request, jsonify
from Application.UseCase.get_sales_by_category import get_sales_by_category_usecase

sales_by_category_bp = Blueprint('sales_by_category', __name__)


@sales_by_category_bp.route('', methods=['GET'])
def sales_by_category():
    store_uuid = request.args.get('store_uuid')
    if not store_uuid:
        return jsonify({"error": "store_uuid is required"}), 400
    data = get_sales_by_category_usecase(store_uuid)
    return jsonify(data)
