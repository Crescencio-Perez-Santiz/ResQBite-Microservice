from Application.UseCases.UpdateUserUseCase import UpdateUserUseCase
from flask import Blueprint, jsonify , make_response, request 
from flask_jwt_extended import jwt_required


update_user_controller = Blueprint("update_user_controller", __name__)

def create_update_user_controller(user_repository):
    @update_user_controller.route("", methods=["PUT"])
    @jwt_required()
    def update_user():
        data = request.get_json()
        password = data["password"]
        name = data["name"]
        last_name = data["last_name"]
        address = data["address"]
        phone_number = data["phone_number"]
        user_updated, status = UpdateUserUseCase(user_repository).execute(
            password, name, last_name, address, phone_number
        )
        return make_response(
            jsonify(
                {
                    "user": user_updated.to_dict(),
                    "status": "User Updated Successfully",
                }
            ),
            200 if status else 400,
        )

    return update_user_controller