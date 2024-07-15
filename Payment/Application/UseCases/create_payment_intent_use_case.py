import stripe
import os
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

class CreatePaymentIntentUseCase:
    def execute(self, amount: int, currency: str, description: str, shipping: dict):
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency.lower(),
            automatic_payment_methods={'enabled': True},
            description=description,
            shipping=shipping
        )
        return intent.client_secret
