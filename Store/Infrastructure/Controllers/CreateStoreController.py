from Application.UseCases.CreateStoreUseCase import CreateStoreUseCase
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

create_store_controller = Blueprint('create_store_controller', __name__)


def create_store(store_repository):
    @create_store_controller.route('', methods=['POST'])
    @jwt_required()
    def create():
        try:
            user_uuid = request.jwt_identity()
            image_file = request.files['url_image']
            store_data = request.form.to_dict()

            create_store_use_case = CreateStoreUseCase(store_repository)
            result_store = create_store_use_case.execute(
                store_data, image_file, user_uuid)

            return jsonify(result_store), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return create_store_controller
