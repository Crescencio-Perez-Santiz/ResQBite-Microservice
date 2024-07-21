from Infrastructure.Controllers import (
    CreateStoreController, GetStoresController, GetStoreByUuidController, UpdateStoreController, GetStoreController)
from Infrastructure.Security.AuthStore import configure_jwt


def initialize_routes(app, storeRepository):
    configure_jwt(app)
    app.register_blueprint(
        CreateStoreController.create_store(storeRepository), url_prefix='/create-store')
    app.register_blueprint(GetStoresController.get_stores(
        storeRepository), url_prefix='/stores')
    app.register_blueprint(GetStoreByUuidController.get_store_by_uuid(
        storeRepository), url_prefix='/store')
    app.register_blueprint(UpdateStoreController.update_store(
        storeRepository), url_prefix='/update-store')
    app.register_blueprint(GetStoreController.get_store_by_user_uuid(
        storeRepository), url_prefix='/get-store')
