from flask import Flask

from taas import collection, test_case, execution, execution_run, \
    parameter, step, test_run
from taas.database import db
from taas.settings import DevConfig


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    register_blueprints(app)
    from taas.test_case.models import TestCase
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprints(app):
    app.register_blueprint(test_case.views.blueprint)
    app.register_blueprint(collection.views.blueprint)
    app.register_blueprint(execution.views.blueprint)
    app.register_blueprint(execution_run.views.blueprint)
    app.register_blueprint(parameter.views.blueprint)
    app.register_blueprint(step.views.blueprint)
    app.register_blueprint(test_run.views.blueprint)

app = create_app()
