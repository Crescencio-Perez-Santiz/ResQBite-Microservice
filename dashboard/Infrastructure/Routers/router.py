from flask import Flask
from Infrastructure.Controllers.historical_data_controller import historical_data_bp
from Infrastructure.Controllers.sales_data_controller import sales_data_bp
from Infrastructure.Controllers.best_selling_product_controller import best_selling_product_bp
from Infrastructure.Controllers.sales_by_category_controller import sales_by_category_bp
from Infrastructure.Controllers.prediction_controller import prediction_bp
from Infrastructure.database.db import init_db


def create_app():
    app = Flask(__name__)
    init_db(app)
    app.register_blueprint(historical_data_bp, url_prefix='/historical_data')
    app.register_blueprint(sales_data_bp, url_prefix='/sales_data')
    app.register_blueprint(best_selling_product_bp,
                           url_prefix='/best_selling_product')
    app.register_blueprint(sales_by_category_bp,
                           url_prefix='/sales_by_category')
    app.register_blueprint(prediction_bp, url_prefix='/prediction')
    print("Aplicación creada y base de datos inicializada.")
    return app
