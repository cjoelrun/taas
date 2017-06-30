from flask import Blueprint, jsonify

from taas.execution_run.models import ExecutionRun

blueprint = Blueprint('execution_run', __name__, url_prefix='/execution_runs')


@blueprint.route('/')
def execution_runs():
    return jsonify(ExecutionRun.query.all())
