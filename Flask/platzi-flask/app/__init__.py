from flask import  Flask
from flask_bootstrap import  Bootstrap

from .config import Config

from auth import auth

def create_app():
    # __name__ indica que el nombre de la aplicación será el nombre del archivo

    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)

    app.register_blueprint(auth)

    return app
