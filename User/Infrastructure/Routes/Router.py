from Infrastructure.Controllers import (
    SignUpController,
    SignInController,
    GetUserController,
    GetUserByEmailController,
    UpdateUserController,
    UpdateLocationController
)
from Infrastructure.Security.JWTSecurity import configure_jwt


def initialize_user_router(app, userRepository):
    configure_jwt(app)
    app.register_blueprint(SignUpController.create_signup_controller(userRepository),
                           url_prefix="/signup")
    app.register_blueprint(SignInController.user_signin_controller(userRepository),
                           url_prefix="/signin")
    app.register_blueprint(GetUserController.get_user_controller(userRepository),
                           url_prefix="/user")
    app.register_blueprint(GetUserByEmailController.get_user_by_email_controller(userRepository),
                           url_prefix="/user_by_email",)
    app.register_blueprint(UpdateUserController.create_update_user_controller(userRepository),
                           url_prefix="/update_user")
    app.register_blueprint(UpdateLocationController.create_update_location_controller
                           (userRepository), url_prefix="/update_location")
