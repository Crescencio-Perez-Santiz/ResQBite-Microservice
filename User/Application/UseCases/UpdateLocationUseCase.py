from flask_jwt_extended import get_jwt_identity

class UpdateLocationUseCase:
    def __init__(self, location_repository):
        self.location_repository = location_repository

    def execute(self,location):
        user_uuid = get_jwt_identity()
        return self.location_repository.update_location(user_uuid, location), True