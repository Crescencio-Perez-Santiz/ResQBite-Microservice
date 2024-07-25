from Application.UseCases.UpdateUserTypeSuscriberUseCase import UpdateUserTypeSuscriberUseCase
from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required

update_user_type_suscriber_controller = Blueprint(
    "update_user_type_suscriber_controller", __name__)


def create_update_user_type_suscriber_controller(user_repository):

    @update_user_type_suscriber_controller.route("", methods=["PUT"])
    @jwt_required()
    def update_user_type_suscriber():
        data = request.get_json()
        user_type = data["user_type_suscriber"].upper()
        if user_type != "COMUN" and user_type != "PREMIUM":
            return make_response(
                jsonify(
                    {
                        "status": "User Type Suscriber must be COMUN or PREMIUM",
                    }
                ),
                400,
            )
        user_updated, status = UpdateUserTypeSuscriberUseCase(
            user_repository).execute(user_type)
        return make_response(
            jsonify(
                {
                    "user": user_updated.to_dict(),
                    "status": "User Type Updated Successfully",
                }
            ),
            200 if status else 400,
        )

    return update_user_type_suscriber_controller
