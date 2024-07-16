# Payment.Domain.Repositories.payment_intent_repository.py
from abc import ABC, abstractmethod
from Payment.Domain.Entities.payment_intent import PaymentIntent

class PaymentIntentRepository(ABC):
    @abstractmethod
    def save(self, payment_intent: PaymentIntent):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, payment_id: str):
        pass
