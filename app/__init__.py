# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from flask_login import LoginManager


from arcgis.gis import GIS


db = MongoEngine()
lm = LoginManager()


def create_app():
    app = Flask(__name__)
    gis = GIS("https://www.arcgis.com")

    #Configuration of application, see configuration.py, choose one and uncomment.
    app.config.from_pyfile('config.cfg')

    Bootstrap(app)  # flask-bootstrap
    db.init_app(app)  # flask-mongoengine

    lm.init_app(app)
    lm.login_view = 'login'

    from app import models

    from app.routers.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
