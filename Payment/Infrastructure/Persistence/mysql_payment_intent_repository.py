from Payment.Domain.Entities.payment_intent import PaymentIntent
from Payment.Domain.Repositories.payment_intent_repository import PaymentIntentRepository
from Payment.Infrastructure.Config.mysql_connection import DBConnection, PaymentModel

class MySQLPaymentIntentRepository(PaymentIntentRepository):
    def __init__(self):
        self.conn = DBConnection()
        self.session = self.conn.Session()

    def save(self, payment_intent: PaymentIntent):
        payment = PaymentModel(
            name=payment_intent.name,
            amount=payment_intent.amount,
            description=payment_intent.description,
        )
        self.session.add(payment)
        self.session.commit()
        return payment

    def get_all(self):
        payments = self.session.query(PaymentModel).all()
        return payments

    def get_by_id(self, payment_id):
        return self.session.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
