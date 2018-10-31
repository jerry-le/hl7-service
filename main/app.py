# -*- coding: utf-8 -*-
from flask import Flask

from main.config import ProdConfig
from main.extensions import db, bcrypt, migrate, cors
from main.views import message


def create_app(config_object=ProdConfig):
    """Application factory to produce application instance.

    Args:
        config_object (object): the configuration loaded from `main.config`

    """

    app = Flask(__name__)
    # Ignore trailing slash in flask route
    # https://stackoverflow.com/questions/40365390/trailing-slash-in-flask-route
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    register_commands(app)
    return app


def register_extensions(app):
    """Every extensions start with flask_* will be initialized here."""

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """Register endpoints here.  Also do allow CORS."""

    # Allow CORS
    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(message.blueprint, origins=origins)

    # TODO: Register all endpoints in `main.views`
    app.register_blueprint(message.blueprint)


def register_error_handlers(app):
    """The errors should be raised in the same format."""

    def error_handler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    # app.errorhandler(InvalidUsage)(error_handler)


def register_commands(app):
    """Register all the command used by CLI"""

    # app.cli.add_command(commands.test)
    pass

