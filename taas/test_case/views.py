from flask import Blueprint, jsonify, request

from taas.test_case.models import TestCase
from taas.database import db

blueprint = Blueprint('test_case', __name__, url_prefix='/test-cases')


@blueprint.route('', methods=['GET', 'POST'])
def test_cases():
    from taas.test_case.schemas import test_case_schema

    if request.method == 'GET':
        all_test_cases = TestCase.query.all()
        return test_case_schema.dumps(all_test_cases, many=True)

    if request.method == 'POST':
        test_case = test_case_schema.load(request.json, db.session).data
        db.session.add(test_case)
        db.session.commit()

        return test_case_schema.dumps(test_case).data, 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def test_cases_by_id(db_id):
    from taas.test_case.schemas import test_case_schema

    test_case = TestCase.query.get(db_id)

    if request.method == 'GET':
        if test_case is None:
            return '{} not found.'.format(db_id), 404
        return test_case_schema.dumps(test_case).data

    if request.method == 'PUT':
        test_case_schema.load(request.json, db.session, test_case)
        db.session.commit()
        return test_case_schema.dumps(test_case).data, 200

    if request.method == 'DELETE':
        if test_case is not None:
            db.session.delete(test_case)
            db.session.commit()
        return '', 204
