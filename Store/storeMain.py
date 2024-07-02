from flask import Flask
from Infrastructure.Routes.Router import initialize_routes
from Infrastructure.Respositories.StoreRepository import StoreRepository


app = Flask(__name__)

initialize_routes(app, StoreRepository())

if __name__ == '__main__':
    app.run(port=5000, debug=True, load_dotenv=True)
