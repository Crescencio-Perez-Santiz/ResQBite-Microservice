import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def init_db(app):
    db_uri = (
        f"mysql+pymysql://{os.getenv('DB_USER_MYSQL_STORE')}:"
        f"{os.getenv('DB_PASSWORD_MYSQL_STORE')}@"
        f"{os.getenv('DB_HOST_MYSQL_STORE')}:"
        f"{os.getenv('DB_PORT_MYSQL_STORE')}/"
        f"{os.getenv('DB_DATABASE_MYSQL_STORE')}"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        try:
            db.create_all()
            print("Conexión a la base de datos establecida exitosamente.")
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
