from flask import Blueprint, request

from taas.execution_run.models import ExecutionRun
from taas.database import db

blueprint = Blueprint('execution_run', __name__, url_prefix='/execution-runs')


@blueprint.route('', methods=['GET'])
def execution_runs():
    from taas.execution_run.schemas import execution_run_schema
    if request.method == 'GET':
        all_runs = ExecutionRun.query.all()
        return execution_run_schema.dumps(all_runs, many=True)


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def test_runs_by_id(db_id):
    from taas.execution_run.schemas import execution_run_schema
    execution_run = ExecutionRun.query.get(db_id)

    if request.method == 'GET':
        if execution_run is None:
            return '{} not found.'.format(db_id), 404
        return execution_run_schema.dumps(execution_run).data

    if request.method == 'PUT':
        execution_run_schema.load(request.json, db.session, execution_run)
        db.session.commit()
        return execution_run_schema.dumps(execution_run).data, 200

    if request.method == 'DELETE':
        if execution_run is not None:
            db.session.delete(execution_run)
            db.session.commit()
        return '', 204
