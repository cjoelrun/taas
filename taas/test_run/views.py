from flask import Blueprint, jsonify

from taas.test_run.models import TestRun

blueprint = Blueprint('test_run', __name__, url_prefix='/test_runs')


@blueprint.route('/')
def test_runs():
    return jsonify(TestRun.query.all())
