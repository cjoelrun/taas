from flask import Flask

from taas import collection, test_case, execution, execution_run, \
    parameter, step, test_run, test_suite, test_suite_run
from taas.database import db
from taas.serialization import ma
from taas.settings import DevConfig


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    db.create_all(app=app)
    ma.init_app(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(test_case.views.blueprint)
    app.register_blueprint(collection.views.blueprint)
    app.register_blueprint(execution.views.blueprint)
    app.register_blueprint(execution_run.views.blueprint)
    app.register_blueprint(parameter.views.blueprint)
    app.register_blueprint(step.views.blueprint)
    app.register_blueprint(test_run.views.blueprint)
    app.register_blueprint(test_suite.views.blueprint)
    app.register_blueprint(test_suite_run.views.blueprint)

app = create_app()
