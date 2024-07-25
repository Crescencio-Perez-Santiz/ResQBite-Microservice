from flask_jwt_extended import get_jwt_identity


class GetUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self):
        user_uuid = get_jwt_identity()
        user = self.user_repository.get_user_by_uuid(user_uuid)
        if user is None:
            return False, {"error": "User not found"}
        return True, user
