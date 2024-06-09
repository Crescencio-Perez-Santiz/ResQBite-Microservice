from Application.Exceptions.UserValidationExists import UserValidationService
from Infrastructure.Security.JWTSecurity import get_hashed_password
from flask_jwt_extended import get_jwt_identity


class UpdateUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(
        self,
        password: str,
        full_name: str,
        address: str,
        phone_number: str,
    ):
        user_uuid = get_jwt_identity()
        user_phone_number_exist = UserValidationService(
            self.user_repository
        ).user_phone_number_exists(phone_number)
        if user_phone_number_exist:
            raise Exception("Phone Number already exists check your data")

        hashed_password = get_hashed_password(password)

        return self.user_repository.update_user(
            user_uuid, hashed_password, full_name, address, phone_number
        ),True
