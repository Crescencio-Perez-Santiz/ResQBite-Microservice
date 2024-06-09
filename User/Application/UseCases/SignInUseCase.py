from Infrastructure.Security.JWTSecurity import (
    check_password,
    create_custom_access_token,
)


class SignInUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, email, password):
        user = self.user_repository.get_user_by_email(email)
        if user is None:
            return False, {"error": "User not found"}
        if not check_password(password, user.password):
            return False, {"error": "Invalid password"}
        acces_token = create_custom_access_token(subject=user.uuid)
        return True, acces_token
