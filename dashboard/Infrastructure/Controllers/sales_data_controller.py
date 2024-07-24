from flask import Blueprint, request, jsonify
from Application.UseCase.get_sales_data import get_sales_data

sales_data_bp = Blueprint('sales_data', __name__)


@sales_data_bp.route('', methods=['GET'])
def sales_data():
    store_uuid = request.args.get('store_uuid')
    if not store_uuid:
        return jsonify({"error": "store_uuid is required"}), 400
    data = get_sales_data(store_uuid)
    return jsonify(data)
