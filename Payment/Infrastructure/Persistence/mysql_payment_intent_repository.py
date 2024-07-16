from Payment.Domain.Entities.payment_intent import PaymentIntent
from Payment.Domain.Repositories.payment_intent_repository import PaymentIntentRepository
from Payment.Infrastructure.Config.mysql_connection import mysql_connection

class MySQLPaymentIntentRepository(PaymentIntentRepository):
    def __init__(self):
        self.conn = mysql_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def save(self, payment_intent: PaymentIntent):
        query = "INSERT INTO payment_intents (name, amount, description) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (payment_intent.name, payment_intent.amount, payment_intent.description))
        self.conn.commit()

    def get_all(self):
        query = "SELECT * FROM payment_intents"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return [PaymentIntent(**row) for row in result]

    def get_by_id(self, payment_id: str):
        query = "SELECT * FROM payment_intents WHERE id = %s"
        self.cursor.execute(query, (payment_id,))
        result = self.cursor.fetchone()
        if result:
            return PaymentIntent(**result)
        else:
            return None
