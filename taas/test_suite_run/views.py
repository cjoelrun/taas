from flask import Blueprint, request
from taas.test_suite_run.models import TestSuiteRun
from taas.database import db

blueprint = Blueprint('test_suite_run', __name__, url_prefix='/test-suite-runs')


@blueprint.route('', methods=['GET'])
def test_suite_runs():
    from taas.test_suite_run.schemas import test_suite_run_schema

    if request.method == 'GET':
        all_test_runs = TestSuiteRun.query.all()
        return test_suite_run_schema.dumps(all_test_runs, many=True)


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def test_suite_runs_by_id(db_id):
    from taas.test_suite_run.schemas import test_suite_run_schema

    test_suite_run = TestSuiteRun.query.get(db_id)

    if request.method == 'GET':
        if test_suite_run is None:
            return '{} not found.'.format(db_id), 404
        return test_suite_run_schema.dumps(test_suite_run).data

    if request.method == 'PUT':
        test_suite_run_schema.load(request.json, db.session, test_suite_run)
        db.session.commit()
        return test_suite_run_schema.dumps(test_suite_run).data, 200

    if request.method == 'DELETE':
        if test_suite_run is not None:
            db.session.delete(test_suite_run)
            db.session.commit()
        return '', 204
