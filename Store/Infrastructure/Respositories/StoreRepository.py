from Domain.Entity.Store import Store as StoreDomain
from Domain.Port.StoreInterface import StoreInterface
from DataBase.MySQLConnection import MySQLConnection
from .ModelStore import Store


class StoreRepository(StoreInterface):
    def __init__(self):
        self.session = MySQLConnection().Session()

    def create(self, store: StoreDomain) -> Store:
        store = Store(
            uuid=store.uuid,
            name=store.name,
            rfc=store.rfc,
            street=store.address.street,
            number=store.address.number,
            neighborhood=store.address.neighborhood,
            city=store.address.city,
            reference=store.address.reference,
            image=store.information.url_image,
            phone_number=store.information.phone_number,
            opening_hours=store.information.opening_hours,
            closing_hours=store.information.closing_hours,
            user_uuid=store.user_uuid
        )

        self.session.add(store)
        self.session.commit()
        return store

    def getStore(self, uuid: str):
        return self.session.query(Store).filter_by(uuid=uuid).first()

    def update(self, store: Store) -> Store:
        self.session.add(store)
        self.session.commit()
        return store

    def list_stores(self) -> list:
        return self.session.query(Store).all()

    def get_store_by_rfc(self, rfc: str):
        return self.session.query(Store).filter_by(rfc=rfc).first()

    def get_store_by_phone_number(self, phone_number: str):
        return self.session.query(Store).filter_by(phone_number=phone_number).first()
