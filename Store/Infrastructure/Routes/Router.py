from Infrastructure.Controllers import (CreateStoreController)
from Infrastructure.Security.AuthStore import configure_jwt


def initialize_routes(app, storeRepository):
    configure_jwt(app)
    app.register_blueprint(
        CreateStoreController.create_store(storeRepository), url_prefix='/create-store')
