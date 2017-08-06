from flask import Blueprint, jsonify
from taas.test_suite.models import TestSuite

blueprint = Blueprint('test_suite', __name__, url_prefix='/test_suites')


@blueprint.route('/')
def test_suites():
    return jsonify(TestSuite.query.all())
