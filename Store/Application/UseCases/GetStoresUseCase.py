class GetStoresUseCase:
    def __init__(self, store_repository):
        self.store_repository = store_repository

    def execute(self):
        return self.store_repository.list_stores()
