from flask import Blueprint, jsonify
# from flask_jwt_extended import jwt_required
from Application.UseCases.GetStoreByUuidUseCase import GetStoreByUuidUseCase

get_store_by_uuid_controller = Blueprint(
    'get_store_by_uuid_controller', __name__)


def get_store_by_uuid(store_repository):
    @get_store_by_uuid_controller.route('/<uuid>', methods=['GET'])
    # @jwt_required()
    def get(uuid):
        try:
            get_store_by_uuid_use_case = GetStoreByUuidUseCase(
                store_repository)
            store = get_store_by_uuid_use_case.execute(uuid)
            if store is None:
                return jsonify({"error": "Store not found"}), 404
            return jsonify(store.to_dict()), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return get_store_by_uuid_controller
