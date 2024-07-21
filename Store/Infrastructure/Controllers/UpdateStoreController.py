from Application.UseCases.UpdateStoreUseCase import UpdateStoreUseCase
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import traceback


update_store_controller = Blueprint('update_store_controller', __name__)


def update_store(store_repository):
    @update_store_controller.route('', methods=['PUT'])
    @jwt_required()
    def update():
        try:
            store_data = request.form.to_dict()
            image_file = request.files.get('image')

            update_store_use_case = UpdateStoreUseCase(store_repository)
            updated_store = update_store_use_case.execute(
                store_data, image_file)

            return jsonify(updated_store.to_dict()), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            traceback.print_exc()
            return jsonify({"error": "An error occurred"}), 500

    return update_store_controller
