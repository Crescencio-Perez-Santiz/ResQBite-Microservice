from flask import Flask
from dotenv import load_dotenv

from Payment.Interfaces.delivery.routes import create_routes

load_dotenv()

app = Flask(__name__)
app = create_routes(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4242, debug=True)
