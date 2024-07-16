
class PaymentIntent:
    def __init__(self, name: str, amount: int, description: str, **kwargs):
        self.name = name
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "description": self.description
        }
