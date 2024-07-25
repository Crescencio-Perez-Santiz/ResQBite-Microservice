from abc import ABC, abstractmethod
from Domain.Entity.Store import Store


class StoreInterface(ABC):
    @abstractmethod
    def create(self, store: Store) -> Store:
        pass

    @abstractmethod
    def getStore(self, uuid: str) -> Store:
        pass

    @abstractmethod
    def update(self, store: Store) -> Store:
        pass

    @abstractmethod
    def list_stores(self) -> list:
        pass
