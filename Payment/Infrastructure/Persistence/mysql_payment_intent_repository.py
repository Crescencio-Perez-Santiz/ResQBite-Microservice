from Payment.Domain.Entities.payment_intent import PaymentIntent
from Payment.Domain.Repositories.payment_intent_repository import PaymentIntentRepository

from Payment.Infrastructure.Config.mysql_connection import DBConnection, PaymentModel

class MySQLPaymentIntentRepository(PaymentIntentRepository):
    def __init__(self):
        self.conn = DBConnection()
        self.session = self.conn.Session()

    def save(self, PaymentIntentDomain):
       payment = PaymentModel(
            name_uuid = PaymentIntentDomain.name_uuid,
            amount = PaymentIntentDomain.amount,
            description = PaymentIntentDomain.description,
       )
       self.session.add( payment )
       self.session.commit()
       return payment

    def get_all(self):
        payment = self.session.query(PaymentModel).all()
        return payment

    def get_by_id(self, payment_id):
        return self.db_session.query(PaymentModel).filter(PaymentModel .payment_id == payment_id).first()
    