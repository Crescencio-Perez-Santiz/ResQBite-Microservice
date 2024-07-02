from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required
from Application.UseCases.GetUserByEmailUseCase import GetUserByEmailUseCase

get_user_by_email_blueprint = Blueprint("get_user_by_email", __name__)


def get_user_by_email_controller(user_repository):
    @get_user_by_email_blueprint.route("", methods=["GET"])
    @jwt_required()
    def get_user_by_email():
        email = request.args.get("email")
        status, user_saved = GetUserByEmailUseCase(user_repository).execute(email)
        if user_saved is None:
            return make_response(
                jsonify(
                    {
                        "error": "User not found",
                        "status": "User Not Found",
                    }
                ),
                404,
            )
        else:
            return make_response(
                jsonify(
                    {
                        "user": user_saved.to_dict(),
                        "status": "User Found" if status else "User Not Found",
                    }
                ),
                200,
            )

    return get_user_by_email_blueprint
