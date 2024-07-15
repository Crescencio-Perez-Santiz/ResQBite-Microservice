from Payment.Domain.Entities.payment_intent import PaymentIntent
from Payment.Domain.Repositories.payment_intent_repository import PaymentIntentRepository

class SavePaymentUseCase:
    def __init__(self, payment_intent_repository: PaymentIntentRepository):
        self.payment_intent_repository = payment_intent_repository

    def execute(self, name: str, amount: int, description: str):
        payment_intent = PaymentIntent(name=name, amount=amount, description=description)
        self.payment_intent_repository.save(payment_intent)
