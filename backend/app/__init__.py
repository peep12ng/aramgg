from flask import Flask
from flask_cors import CORS
from .extensions import db, migrate, aramgg_poro

from .views import get_blueprints
from . import config

import os
from dotenv import load_dotenv

__all__ = ["create_app"]

def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins":"*"}})
    configure_app(app, config)
    configure_extensions(app)
    blueprints = get_blueprints()
    configure_blueprints(app, blueprints)
    configure_env()

    return app

def configure_app(app, config):
    app.config.from_object(config)

def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_env():
    aramgg_poro.set_riot_api_key(os.getenv("RIOT_API_KEY"))