
class PaymentIntent:
    def __init__(self, id: int, name: str, amount: int, description: str):
        self.id = id
        self.name = name
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "amount": self.amount,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            amount=data.get("amount"),
            description=data.get("description")
        )
