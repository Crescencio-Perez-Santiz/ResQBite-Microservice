from flask import request, jsonify
from Payment.Application.UseCases.save_payment_use_case import SavePaymentUseCase
from Payment.Infrastructure.Persistence.mongo_payment_intent_repository import MongoPaymentIntentRepository
from Payment.Application.Validator.input_validators import validate_save_payment  

class SavePaymentController:
    def __init__(self):
        self.payment_intent_repository = MongoPaymentIntentRepository()
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
            return jsonify(error='An error occurred while processing the request'), 500
