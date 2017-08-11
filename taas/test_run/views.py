from flask import Blueprint, request

from taas.test_run.models import TestRun
from taas.database import db

blueprint = Blueprint('test_run', __name__, url_prefix='/test-runs')


@blueprint.route('', methods=['GET'])
def test_runs():
    from taas.test_run.schemas import test_run_schema

    if request.method == 'GET':
        all_test_runs = TestRun.query.all()
        return test_run_schema.dumps(all_test_runs, many=True)


@blueprint.route('/<db_id>', methods=['GET', 'DELETE'])
def test_runs_by_id(db_id):
    from taas.test_run.schemas import test_run_schema

    test_run = TestRun.query.get(db_id)

    if request.method == 'GET':
        if test_run is None:
            return '{} not found.'.format(db_id), 404
        return test_run_schema.dumps(test_run).data

    if request.method == 'DELETE':
        if test_run is not None:
            db.session.delete(test_run)
            db.session.commit()
        return '', 204
