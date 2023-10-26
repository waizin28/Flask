from flask import Flask
from flask_smorest import Api
from resources.transaction import blp as BudgetBlueprint
from resources.budget import blp as TransactionBlueprint
from db import db
from dotenv import load_dotenv 
import os

def create_app(db_url=None):
    app = Flask(__name__)

    # will find env file and load the content
    load_dotenv()

    # flask configuration, error at flask extension -> propagate to main
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Capital Two REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    # start of root of API
    app.config["OPENAPI_URL_PREFIX"] = "/" 
    # tell flask-smorest, swagger for api documentation
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    # location of where code live 
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


    # Confiuring database
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)

    # connect flask-smorest extension to flask app
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(BudgetBlueprint)
    api.register_blueprint(TransactionBlueprint)

    return app