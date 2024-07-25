from flask_jwt_extended import get_jwt_identity


class GetStoreByUserUuidUseCase:
	def __init__(self, store_repository):
		self.store_repository = store_repository

	def execute(self):
		user_uuid = get_jwt_identity()
		return self.store_repository.get_store_by_user_uuid(user_uuid)
