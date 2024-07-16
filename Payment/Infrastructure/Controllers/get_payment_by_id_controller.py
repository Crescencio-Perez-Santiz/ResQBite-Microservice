from flask import jsonify
from Payment.Application.UseCases.get_payment_by_id_use_case import GetPaymentByIdUseCase
from Payment.Infrastructure.Persistence.mysql_payment_intent_repository import MySQLPaymentIntentRepository

class GetPaymentByIdController:
    def __init__(self):
        self.payment_intent_repository = MySQLPaymentIntentRepository()
        self.get_payment_by_id_use_case = GetPaymentByIdUseCase(self.payment_intent_repository)

    def get_payment_by_id(self, payment_id: str):
        try:
            payment_intent = self.get_payment_by_id_use_case.execute(payment_id)
            if payment_intent:
                return jsonify(payment_intent.to_dict())
            else:
                return jsonify(error='Payment not found'), 404
        except Exception as e:
            return jsonify(error='An error occurred while processing the request'), 500
