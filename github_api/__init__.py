from flask import Flask

from . import models
from .extensions import config, assets
from .views.github import github_blueprint
from .views.myrepos import myrepos


DEBUG = True
SECRET_KEY = 'development-key'


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    config.init_app(app)
    assets.init_app(app)

    app.register_blueprint(github_blueprint, url_prefix="/login")
    app.register_blueprint(myrepos)

    return app