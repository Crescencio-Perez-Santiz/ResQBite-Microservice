from flask import jsonify
from Payment.Application.UseCases.get_all_payments_use_case import GetAllPaymentsUseCase
from Payment.Infrastructure.Persistence.mysql_payment_intent_repository import MySQLPaymentIntentRepository

class GetAllPaymentsController:
    def __init__(self):
        self.payment_intent_repository = MySQLPaymentIntentRepository()
        self.get_all_payments_use_case = GetAllPaymentsUseCase(self.payment_intent_repository)

    def get_all_payments(self):
        try:
            payments = self.get_all_payments_use_case.execute()
            payments_list = [payment.to_dict() for payment in payments]
            return jsonify(payments_list)
        except Exception as e:
            return jsonify(error='An error occurred while processing the request'), 500
