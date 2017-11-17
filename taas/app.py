from flask import Flask
from sqlalchemy_utils import database_exists, create_database

from taas import test_case, execution, execution_run, \
    parameter, step, test_run, test_suite, test_suite_run, runner, parameter_group
from taas.database import db
from taas.serialization import ma
from taas.settings import DevConfig


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    create_db(config)
    db.create_all(app=app)
    ma.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(test_case.views.blueprint)
    app.register_blueprint(execution.views.blueprint)
    app.register_blueprint(execution_run.views.blueprint)
    app.register_blueprint(parameter_group.views.blueprint)
    app.register_blueprint(parameter.views.blueprint)
    app.register_blueprint(step.views.blueprint)
    app.register_blueprint(test_run.views.blueprint)
    app.register_blueprint(test_suite.views.blueprint)
    app.register_blueprint(test_suite_run.views.blueprint)
    app.register_blueprint(runner.views.blueprint)


def create_db(config):
    if not database_exists(config.SQLALCHEMY_DATABASE_URI):
        create_database(config.SQLALCHEMY_DATABASE_URI)
