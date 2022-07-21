from flask import Flask
from flask_mongoengine import MongoEngine
from flask.app import Flask
from .config import config_by_name
from flask_request_params import bind_request_params
# from flask_bcrypt import Bcrypt

db = MongoEngine()
# flask_bcrypt = Bcrypt()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.before_request(bind_request_params)
    db.init_app(app)
    # flask_bcrypt.init_app(app)

    return app