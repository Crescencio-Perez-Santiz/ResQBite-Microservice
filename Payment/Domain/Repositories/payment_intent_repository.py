from abc import ABC, abstractmethod
from Payment.Domain.Entities.payment_intent import PaymentIntent


class PaymentIntentRepository(ABC):
    @abstractmethod
    def save(self, payment_intent: PaymentIntent):
        pass