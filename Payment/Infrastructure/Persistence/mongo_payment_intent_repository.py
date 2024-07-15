from Payment.Domain.Entities.payment_intent import PaymentIntent
from Payment.Domain.Repositories.payment_intent_repository import PaymentIntentRepository
from Payment.Infrastructure.Config.mongo_connection import mongo_connection


class MongoPaymentIntentRepository(PaymentIntentRepository):
    def __init__(self):
        self.db = mongo_connection()
        self.collection = self.db['payment_intents']

    def save(self, payment_intent: PaymentIntent):
        self.collection.insert_one(payment_intent.to_dict())
