from flask import Blueprint, jsonify

from taas.execution.models import Execution

blueprint = Blueprint('execution', __name__, url_prefix='/executions')


@blueprint.route('/')
def executions():
    return jsonify(Execution.query.all())
