from flask import Flask
from Infrastructure.Routes.Router import initialize_user_router
from Infrastructure.Repositories.UserRepository import UserRepository

app = Flask(__name__)

initialize_user_router(app, UserRepository())

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True, load_dotenv=True)
