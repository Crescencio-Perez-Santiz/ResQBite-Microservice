from Infrastructure.Controllers import (CreateStoreController)


def initialize_routes(app, storeRepository):
    app.register_blueprint(
        CreateStoreController.create_store(storeRepository), url_prefix='/create-store')
