from flask import Blueprint, jsonify
from taas.test_suite_run.models import TestSuiteRun

blueprint = Blueprint('test_suite_run', __name__, url_prefix='/test_suite_runs')


@blueprint.route('/')
def test_suite_runs():
    return jsonify(TestSuiteRun.query.all())
