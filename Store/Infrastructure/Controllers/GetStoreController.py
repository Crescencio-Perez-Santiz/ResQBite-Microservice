from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from Application.UseCases.GetStoreUseCase import GetStoreByUserUuidUseCase
from Infrastructure.Respositories.StoreRepository import StoreRepository

get_store_by_user_uuid_controller = Blueprint(
	'get_store_by_user_uuid_controller', __name__)


def get_store_by_user_uuid(store_repository):

    @get_store_by_user_uuid_controller.route('', methods=['GET'])
    @jwt_required()
    def get_store_by_user_uuid():
        store_repository = StoreRepository()
        use_case = GetStoreByUserUuidUseCase(store_repository)
        store = use_case.execute()
        return jsonify(store.to_dict())

    return get_store_by_user_uuid_controller
