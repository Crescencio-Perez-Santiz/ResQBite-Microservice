class GetUserByEmailUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, email):
        user = self.user_repository.get_user_by_email(email)
        if user is None:
            return False, None
        return True, user
