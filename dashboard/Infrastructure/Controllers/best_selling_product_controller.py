# dashboard/Infrastructure/Controllers/best_selling_product_controller.py
from flask import Blueprint, request, jsonify
from Application.UseCase.get_best_selling_product import get_best_selling_product

best_selling_product_bp = Blueprint('best_selling_product', __name__)


@best_selling_product_bp.route('', methods=['GET'])
def best_selling_product():
    store_uuid = request.args.get('store_uuid')
    if not store_uuid:
        return jsonify({"error": "store_uuid is required"}), 400

    # Asegúrate de que esta función no esté realizando operaciones costosas
    result = get_best_selling_product(store_uuid)
    return jsonify(result)
