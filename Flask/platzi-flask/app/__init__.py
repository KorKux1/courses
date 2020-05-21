from flask import  Flask
from flask_bootstrap import  Bootstrap
from flask_login import LoginManager

from .config import Config
from .models import UserModel

from auth import auth

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)


def create_app():
    # __name__ indica que el nombre de la aplicación será el nombre del archivo

    app = Flask(__name__)
    bootstrap = Bootstrap(app)


    app.config.from_object(Config)

    #a Antes de registrar los bluesprints se le dice que inicialice la aplicación
    login_manager.init_app(app)

    app.register_blueprint(auth)

    return app


