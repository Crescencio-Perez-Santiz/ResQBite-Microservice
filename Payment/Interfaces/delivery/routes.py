from flask import Flask
from Payment.Infrastructure.Controllers.create_payment_intent_controller import CreatePaymentIntentController
from Payment.Infrastructure.Controllers.save_payment_controller import SavePaymentController
from Payment.Infrastructure.Controllers.get_all_payments_controller import GetAllPaymentsController
from Payment.Infrastructure.Controllers.get_payment_by_id_controller import GetPaymentByIdController

def create_routes(app: Flask):
    create_payment_intent_controller = CreatePaymentIntentController()
    save_payment_controller = SavePaymentController()
    get_all_payments_controller = GetAllPaymentsController()
    get_payment_by_id_controller = GetPaymentByIdController()

    @app.route('/create-payment-intent', methods=['POST'])
    def create_payment_intent():
        return create_payment_intent_controller.create_payment_intent()

    @app.route('/save-payment', methods=['POST'])
    def save_payment():
        return save_payment_controller.save_payment()

    @app.route('/payments', methods=['GET'])
    def get_all_payments():
        return get_all_payments_controller.get_all_payments()

    @app.route('/payments/<payment_id>', methods=['GET'])
    def get_payment_by_id(payment_id):
        return get_payment_by_id_controller.get_payment_by_id(payment_id)

    return app
