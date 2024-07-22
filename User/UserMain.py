from flask import Flask
from Infrastructure.Routes.Router import initialize_user_router
from Infrastructure.Repositories.UserRepository import UserRepository
from Infrastructure.Services.Dependecies import init_rabbitmq
import ssl

app = Flask(__name__)

init_rabbitmq()
initialize_user_router(app, UserRepository())

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(certfile='fullchain.pem', keyfile='privkey.pem')

    app.run("0.0.0.0", 5000, debug=True, load_dotenv=True)
