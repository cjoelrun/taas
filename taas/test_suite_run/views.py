from flask import Blueprint, jsonify, request
from taas.test_suite_run.models import TestSuiteRun
from taas.database import db

blueprint = Blueprint('test_suite_run', __name__, url_prefix='/test_suite_runs')


@blueprint.route('', methods=['GET', 'POST'])
def test_suite_runs():
    if request.method == 'GET':
        return jsonify([e.serialize() for e in TestSuiteRun.query.all()])

    if request.method == 'POST':
        test_suite_run = TestSuiteRun()
        test_suite_run.update_fields(request.json)
        db.session.add(test_suite_run)
        db.session.commit()

        return jsonify(test_suite_run.serialize()), 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def test_suite_runs_by_id(db_id):
    test_suite_run = TestSuiteRun.query.get(db_id)

    if request.method == 'GET':
        if test_suite_run is None:
            return '{} not found.'.format(db_id), 404
        return jsonify(test_suite_run.serialize())

    if request.method == 'DELETE':
        if test_suite_run is not None:
            db.session.delete(test_suite_run)
            db.session.commit()
        return '', 204
