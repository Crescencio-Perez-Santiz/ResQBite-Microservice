from Infrastructure.Repositories.UserRepository import UserRepository

class UserValidationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def user_email_exists(self, email):
        return self.user_repository.get_user_by_email(email) is not None
    
    def user_phone_number_exists(self, phone_number):
        return self.user_repository.get_user_by_phone_number(phone_number) is not None