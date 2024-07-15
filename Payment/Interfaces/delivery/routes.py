from flask import Flask
from Payment.Infrastructure.Controllers.create_payment_intent_controller import CreatePaymentIntentController

from Payment.Infrastructure.Controllers.save_payment_controller import SavePaymentController

def create_routes(app: Flask):
    create_payment_intent_controller = CreatePaymentIntentController()
    save_payment_controller = SavePaymentController()

    @app.route('/create-payment-intent', methods=['POST'])
    def create_payment_intent():
        return create_payment_intent_controller.create_payment_intent()

    @app.route('/save-payment', methods=['POST'])
    def save_payment():
        return save_payment_controller.save_payment()

    return app
