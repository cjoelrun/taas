from flask import Blueprint, jsonify, request

from taas.execution_run.models import ExecutionRun
from taas.database import db

blueprint = Blueprint('execution_run', __name__, url_prefix='/execution_runs')


@blueprint.route('', methods=['GET'])
def execution_runs():
    if request.method == 'GET':
        return jsonify([er.serialize() for er in ExecutionRun.query.all()])


@blueprint.route('/<db_id>', methods=['GET', 'DELETE'])
def test_runs(db_id):
    execution_run = ExecutionRun.query.get(db_id)

    if request.method == 'GET':
        if execution_run is None:
            return '{} not found.'.format(db_id), 404
        return jsonify(execution_run.serialize())

    if request.method == 'DELETE':
        if execution_run is not None:
            db.session.delete(execution_run)
            db.session.commit()
        return '', 204
