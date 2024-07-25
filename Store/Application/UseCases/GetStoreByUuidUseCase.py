class GetStoreByUuidUseCase:
    def __init__(self, store_repository):
        self.store_repository = store_repository

    def execute(self, store_uuid: str):
        return self.store_repository.getStore(store_uuid)
