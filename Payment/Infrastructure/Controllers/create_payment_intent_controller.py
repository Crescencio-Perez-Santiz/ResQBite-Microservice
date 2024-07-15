from flask import request, jsonify
from Payment.Application.UseCases.create_payment_intent_use_case import CreatePaymentIntentUseCase
from Payment.Application.Validator.input_validators import validate_create_payment_intent  

class CreatePaymentIntentController:
    def __init__(self):
        self.create_payment_intent_use_case = CreatePaymentIntentUseCase()

    def create_payment_intent(self):
        try:
            data = request.json

            # Validar los datos de entrada
            validate_create_payment_intent(data)

            client_secret = self.create_payment_intent_use_case.execute(
                amount=int(data['amount']),
                currency=data['currency'],
                description=data['description'],
                shipping={
                    'name': data['name'],
                    'address': {
                        'city': data['city'],
                        'state': data['state'],
                        'country': data['country']
                    }
                }
            )
            return jsonify({'client_secret': client_secret})
        except ValueError as ve:
            return jsonify(error=str(ve)), 400  # Devolver un error 400 Bad Request para errores de validación
        except Exception as e:
            # Manejar otros errores de manera segura sin revelar información sensible
            return jsonify(error='An error occurred while processing the request'), 500
