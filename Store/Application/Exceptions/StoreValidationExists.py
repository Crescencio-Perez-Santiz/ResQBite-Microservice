from Infrastructure.Respositories.StoreRepository import StoreRepository

class StoreValidationExists:
    def __init__(self, storeRepository: StoreRepository):
        self.storeRepository = storeRepository

    def validate_store_by_rfc(self, rfc: str):
        store = self.storeRepository.get_store_by_rfc(rfc)
        if store is not None:
            return True
        return False

    def validate_store_by_phone_number(self, phone_number: str, store_uuid: str = None):
        store = self.storeRepository.get_store_by_phone_number(phone_number)
        if store is None:
            return False
        if store_uuid and store.uuid == store_uuid:
            return False
        return True
