from flask import Blueprint, jsonify

from taas.test_case.models import TestCase

blueprint = Blueprint('test_case', __name__, url_prefix='/test_cases')


@blueprint.route('/')
def test_cases():
    return jsonify(TestCase.query.all())
