from flask import Blueprint, make_response, request, jsonify
from Application.UseCases.SignUpUseCase import SignUpUseCase
from Domain.Entity import User, Contact

signup_blueprint = Blueprint("signup", __name__)


def create_signup_controller(user_repository):
    @signup_blueprint.route("", methods=["POST"])
    def signup():
        data = request.get_json()
        user = User.User(
            email=data["email"],
            password=data["password"],
            location=data["location"],
            user_type_suscriber=data["user_type_suscriber"],
            contact=Contact.Contact(
                name=data["contact"]["name"],
                last_name=data["contact"]["last_name"],
                address=data["contact"]["address"],
                phone_number=data["contact"]["phone_number"],
            ),
        )
        user_saved, status = SignUpUseCase(user_repository).execute(user)
        return make_response(
            jsonify(
                {
                    "user": user_saved.to_dict(),
                    "status": (
                        "User Created Successfully" if status else "User Not Created"
                    ),
                }
            ),
            201 if status else 400,
        )

    return signup_blueprint
