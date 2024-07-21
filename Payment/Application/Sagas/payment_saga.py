# Payment/Application/Sagas/payment_saga.py
from Payment.Application.UseCases.create_payment_intent_use_case import CreatePaymentIntentUseCase
from Payment.Application.UseCases.save_payment_use_case import SavePaymentUseCase

class PaymentSaga:
    def __init__(self, create_payment_intent_use_case: CreatePaymentIntentUseCase, save_payment_use_case: SavePaymentUseCase):
        self.create_payment_intent_use_case = create_payment_intent_use_case
        self.save_payment_use_case = save_payment_use_case

    def execute(self, payment_data: dict):
        try:
            # Paso 1: Crear PaymentIntent en Stripe
            client_secret = self.create_payment_intent_use_case.execute(
                amount=int(payment_data['amount']),
                currency=payment_data['currency'],
                description=payment_data['description'],
                shipping={
                    'name': payment_data['name'],
                    'address': {
                        'city': payment_data['city'],
                        'state': payment_data['state'],
                        'country': payment_data['country']
                    }
                }
            )
            # Paso 2: Guardar PaymentIntent en la base de datos
            self.save_payment_use_case.execute(
                name=payment_data['name'],
                amount=int(payment_data['amount']),
                description=payment_data['description']
            )
            return client_secret
        except Exception as e:
            # Aquí podríamos agregar lógica de compensación si alguno de los pasos falla
            # Por ejemplo, revertir la creación del PaymentIntent en Stripe si la base de datos falla
            raise e
