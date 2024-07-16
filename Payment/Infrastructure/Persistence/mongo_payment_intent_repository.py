# Payment.Infrastructure.Persistence.mongo_payment_intent_repository.py
from bson.objectid import ObjectId
from Payment.Domain.Entities.payment_intent import PaymentIntent
from Payment.Domain.Repositories.payment_intent_repository import PaymentIntentRepository
from Payment.Infrastructure.Config.mongo_connection import mongo_connection

class MongoPaymentIntentRepository(PaymentIntentRepository):
    def __init__(self):
        self.db = mongo_connection()
        self.collection = self.db['payment_intents']

    def save(self, payment_intent: PaymentIntent):
        self.collection.insert_one(payment_intent.to_dict())

    def get_all(self):
        payment_intents = self.collection.find()
        # Ensure to handle None values properly
        return [PaymentIntent(**payment_intent) for payment_intent in payment_intents if payment_intent]

    def get_by_id(self, payment_id: str):
        payment_intent = self.collection.find_one({"_id": ObjectId(payment_id)})
        if payment_intent:
            return PaymentIntent(**payment_intent)
        else:
            return None
