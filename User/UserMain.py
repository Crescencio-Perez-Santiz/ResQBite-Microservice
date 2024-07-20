from flask import Flask
from Infrastructure.Routes.Router import initialize_user_router
from Infrastructure.Repositories.UserRepository import UserRepository
from Infrastructure.Services.Dependecies import init_rabbitmq

app = Flask(__name__)

init_rabbitmq()
initialize_user_router(app, UserRepository())

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True, load_dotenv=True)
