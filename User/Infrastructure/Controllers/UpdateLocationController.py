from Application.UseCases.UpdateLocationUseCase import UpdateLocationUseCase
from flask import Blueprint, jsonify , make_response, request
from flask_jwt_extended import jwt_required

update_location_controller = Blueprint("update_location_controller", __name__)

def create_update_location_controller(location_repository):
    @update_location_controller.route("", methods=["PUT"])
    @jwt_required()
    def update_location():
        data = request.get_json()
        location = data["location"].upper()
        user_updated, status = UpdateLocationUseCase(location_repository).execute(location)
        return make_response(
            jsonify(
                {
                    "user": user_updated.to_dict(),
                    "status": "Location Updated Successfully",
                }
            ),
            200 if status else 400,
        )

    return update_location_controller