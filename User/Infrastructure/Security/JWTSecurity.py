import os
from flask import jsonify
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


def configure_jwt(app):
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def my_expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"status": 401, "sub_status": 42, "msg": "El token ha expirado"}),
            401,
        )


def get_hashed_password(password: str) -> str:
    return generate_password_hash(password)


def check_password(password, hashed_password):
    return check_password_hash(hashed_password, password)


def create_custom_access_token(subject: str):
    expires_delta = timedelta(minutes=30)
    return create_access_token(identity=subject, expires_delta=expires_delta)
