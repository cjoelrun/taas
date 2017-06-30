from flask import Flask

from taas import collection, test_case, execution, execution_run, \
    parameter, step, test_run
from taas.settings import DevConfig


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def register_blueprints(app):
    app.register_blueprints(test_case.views.blueprint)
    app.register_blueprints(collection.views.blueprint)
    app.register_blueprints(execution.views.blueprint)
    app.register_blueprints(execution_run.views.blueprint)
    app.register_blueprints(parameter.views.blueprint)
    app.register_blueprints(step.views.blueprint)
    app.register_blueprints(test_run.views.blueprint)


app = create_app()
