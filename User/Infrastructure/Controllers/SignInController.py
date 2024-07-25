from flask import Blueprint, make_response, request, jsonify
from Application.UseCases.SignInUseCase import SignInUseCase

signup_blueprint = Blueprint("signin", __name__)


def user_signin_controller(user_repository):
    @signup_blueprint.route("", methods=["POST"])
    def signin():
        data = request.get_json()
        status, token = SignInUseCase(user_repository).execute(
            email=data["email"], password=data["password"]
        )
        return make_response(
            jsonify(
                {"status": "User Logged In Successfully", "token": token}
                if status
                else {"status": "User Not Logged In"}
            ),
            200 if status else 401,
        )

    return signup_blueprint
