from flask import request, jsonify
from Payment.Application.UseCases.save_payment_use_case import SavePaymentUseCase
from Payment.Infrastructure.Persistence.mysql_payment_intent_repository import MySQLPaymentIntentRepository
from Payment.Application.Validator.input_validators import validate_save_payment
import logging

class SavePaymentController:
    def __init__(self):
        self.payment_intent_repository = MySQLPaymentIntentRepository()
        self.save_payment_use_case = SavePaymentUseCase(self.payment_intent_repository)

    def save_payment(self):
        try:
            data = request.json

            # Validar los datos de entrada
            validate_save_payment(data)

            self.save_payment_use_case.execute(
                name=data['name'],
                amount=data['amount'],
                description=data['description']
            )
            return jsonify({'message': 'Payment saved successfully'})
        except ValueError as ve:
            return jsonify(error=str(ve)), 400  # para errores de validación
        except Exception as e:
            logging.error(f'Error saving payment: {e}', exc_info=True)  # Registra el error con detalles
            return jsonify(error='An error occurred while processing the request'), 500
