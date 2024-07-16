from Payment.Domain.Repositories.payment_intent_repository import PaymentIntentRepository

class GetPaymentByIdUseCase:
    def __init__(self, payment_intent_repository: PaymentIntentRepository):
        self.payment_intent_repository = payment_intent_repository

    def execute(self, payment_id: str):
        return self.payment_intent_repository.get_by_id(payment_id)
