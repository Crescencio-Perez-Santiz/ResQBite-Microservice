from flask import Flask
from Infrastructure.Routes.Router import initialize_routes
from Infrastructure.Respositories.StoreRepository import StoreRepository
import ssl

app = Flask(__name__)

initialize_routes(app, StoreRepository())

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(certfile='fullchain.pem', keyfile='privkey.pem')
    app.run(host='0.0.0.0', port=5001, ssl_context=context,
            debug=True, load_dotenv=True)
