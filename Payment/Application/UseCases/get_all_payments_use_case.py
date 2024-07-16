from Payment.Domain.Repositories.payment_intent_repository import PaymentIntentRepository

class GetAllPaymentsUseCase:
    def __init__(self, payment_intent_repository: PaymentIntentRepository):
        self.payment_intent_repository = payment_intent_repository

    def execute(self):
        return self.payment_intent_repository.get_all()
