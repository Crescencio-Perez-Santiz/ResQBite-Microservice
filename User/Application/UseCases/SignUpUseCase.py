from Domain.Entity.User import User
from Application.Exceptions.UserValidationExists import UserValidationService
from Infrastructure.Security.JWTSecurity import get_hashed_password


class SignUpUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user: User):
        user_email_exist = UserValidationService(
            self.user_repository
        ).user_email_exists(user.email)
        user_phone_number_exist = UserValidationService(
            self.user_repository
        ).user_phone_number_exists(user.contact.phone_number)

        if user_email_exist and user_phone_number_exist:
            raise Exception("Email or Phone Number already exists")
        user.password = get_hashed_password(user.password)
        return self.user_repository.save_user(user), True
