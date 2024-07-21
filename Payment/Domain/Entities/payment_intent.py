class PaymentIntent:
    def __init__(self, name: str, amount: int, description: str):
        self.name = name
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name"),
            amount=data.get("amount"),
            description=data.get("description")
        )
