from flask import Blueprint, jsonify, request
from taas.test_suite.models import TestSuite

from taas.database import db

blueprint = Blueprint('test_suite', __name__, url_prefix='/test-suites')


@blueprint.route('', methods=['GET', 'POST'])
def test_suites():
    from taas.test_suite.schemas import test_suite_schema

    if request.method == 'GET':
        all_test_suites = TestSuite.query.all()
        return test_suite_schema.dumps(all_test_suites, many=True)

    if request.method == 'POST':
        test_suite = test_suite_schema.load(request.json, db.session).data
        db.session.add(test_suite)
        db.session.commit()

        return test_suite_schema.dumps(test_suite).data, 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def test_suites_by_id(db_id):
    from taas.test_suite.schemas import test_suite_schema

    test_suite = TestSuite.query.get(db_id)

    if request.method == 'GET':
        if test_suite is None:
            return '{} not found.'.format(db_id), 404
        return test_suite_schema.dumps(test_suite).data

    if request.method == 'PUT':
        test_suite_schema.load(request.json, db.session, test_suite)
        db.session.commit()
        return test_suite_schema.dumps(test_suite).data, 200

    if request.method == 'DELETE':
        if test_suite is not None:
            db.session.delete(test_suite)
            db.session.commit()
        return '', 204
