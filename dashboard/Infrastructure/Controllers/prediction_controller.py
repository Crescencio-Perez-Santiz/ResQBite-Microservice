from flask import Blueprint, request, jsonify
from Application.UseCase.get_sales_predictions import get_sales_predictions

prediction_bp = Blueprint('prediction', __name__)


@prediction_bp.route('', methods=['GET'])
def prediction():
    store_uuid = request.args.get('store_uuid')
    if not store_uuid:
        return jsonify({"error": "store_uuid is required"}), 400
    data = get_sales_predictions(store_uuid)
    return jsonify(data)
