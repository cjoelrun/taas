from flask import Blueprint, jsonify

from taas.test_parameter.models import TestParameter

blueprint = Blueprint('test_parameter', __name__, url_prefix='/test_parameter')


@blueprint.route('/')
def test_cases():
    return jsonify(TestParameter.query.all())
