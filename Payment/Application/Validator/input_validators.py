def validate_create_payment_intent(data):
    # Verificar que todos los campos 
    required_fields = ['amount', 'currency', 'description', 'name', 'city', 'state', 'country']
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')

    # Tipos de datos esperados
    # if not isinstance(data['amount'], int):
    if not isinstance(data['amount'], str):
        raise ValueError('Amount must be an integer')
    if not isinstance(data['currency'], str):
        raise ValueError('Currency must be a string')

def validate_save_payment(data):
    required_fields = ['name', 'amount', 'description']
    for field in required_fields:
        if field not in data:
            raise ValueError(f'Missing required field: {field}')

    if not isinstance(data['amount'], int):
        raise ValueError('Amount must be an integer')
    if not isinstance(data['name'], str):
        raise ValueError('Name must be a string')
    if not isinstance(data['description'], str):
        raise ValueError('Description must be a string')
