from Application.UseCases.GetUserUseCase import GetUserUseCase
from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import jwt_required

get_user_blueprint = Blueprint("get_user", __name__)


def get_user_controller(user_repository):
    @get_user_blueprint.route("", methods=["GET"])
    @jwt_required()
    def get_user():
        status, user_saved = GetUserUseCase(user_repository).execute()
        return make_response(
            jsonify(
                {
                    "user": user_saved.to_dict(),
                    "status": "User Found" if status else "User Not Found",
                }
            ),
            200 if status else 404,
        )

    return get_user_blueprint
