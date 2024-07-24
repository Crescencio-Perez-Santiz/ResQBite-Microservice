from flask import Blueprint, request, jsonify
from Application.UseCase.get_historical_data import get_historical_data

historical_data_bp = Blueprint('historical_data', __name__)


@historical_data_bp.route('', methods=['GET'])
def historical_data():
    store_uuid = request.args.get('store_uuid')
    if not store_uuid:
        return jsonify({"error": "store_uuid is required"}), 400
    print(f"Received request for historical data with store_uuid: {
          store_uuid}")
    data = get_historical_data(store_uuid)
    print(f"Returning historical data: {data}")
    return jsonify(data)
