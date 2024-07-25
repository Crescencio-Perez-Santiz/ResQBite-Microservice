from flask_jwt_extended import get_jwt_identity


class UpdateUserTypeSuscriberUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_type):
        user_uuid = get_jwt_identity()
        return self.user_repository.update_user_type(user_uuid, user_type), True
