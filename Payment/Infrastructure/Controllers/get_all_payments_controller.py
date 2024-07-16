# Payment.Infrastructure.Controllers.get_all_payments_controller.py
import logging
from flask import jsonify
from Payment.Application.UseCases.get_all_payments_use_case import GetAllPaymentsUseCase
from Payment.Infrastructure.Persistence.mongo_payment_intent_repository import MongoPaymentIntentRepository

class GetAllPaymentsController:
    def __init__(self):
        self.payment_intent_repository = MongoPaymentIntentRepository()
        self.get_all_payments_use_case = GetAllPaymentsUseCase(self.payment_intent_repository)

    def get_all_payments(self):
        try:
            logging.info("Fetching all payments from repository")
            payments = self.get_all_payments_use_case.execute()
            logging.info(f"Fetched {len(payments)} payments")
            payments_list = [payment.to_dict() for payment in payments]
            return jsonify(payments_list)
        except Exception as e:
            logging.error(f"Error occurred: {e}", exc_info=True)
            return jsonify(error='An error occurred while processing the request'), 500
