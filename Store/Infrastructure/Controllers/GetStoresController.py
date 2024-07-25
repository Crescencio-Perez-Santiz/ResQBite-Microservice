from flask import Blueprint, jsonify
# from flask_jwt_extended import jwt_required
from Application.UseCases.GetStoresUseCase import GetStoresUseCase

get_stores_controller = Blueprint('get_stores_controller', __name__)


def get_stores(store_repository):
    @get_stores_controller.route('', methods=['GET'])
    # @jwt_required()
    def get():
        try:
            get_stores_use_case = GetStoresUseCase(store_repository)
            stores = get_stores_use_case.execute()
            return jsonify([store.to_dict() for store in stores]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return get_stores_controller
