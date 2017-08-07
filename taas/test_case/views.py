from flask import Blueprint, jsonify, request

from taas.test_case.models import TestCase
from taas.database import db

blueprint = Blueprint('test_case', __name__, url_prefix='/test_cases')


@blueprint.route('', methods=['GET', 'POST'])
def test_cases():
    if request.method == 'GET':
        return jsonify([tc.serialize() for tc in TestCase.query.all()])

    if request.method == 'POST':
        test_case = TestCase()
        test_case.update_fields(request.json)
        db.session.add(test_case)
        db.session.commit()

        return jsonify(test_case.serialize()), 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def test_cases(db_id):
    test_case = TestCase.query.get(db_id)

    if request.method == 'GET':
        if test_case is None:
            return '{} not found.'.format(db_id), 404
        return jsonify(test_case.serialize())

    if request.method == 'PUT':
        test_case.update_fields(request.json)
        db.session.commit()
        return jsonify(test_case.serialize()), 200

    if request.method == 'DELETE':
        if test_case is not None:
            db.session.delete(test_case)
            db.session.commit()
        return '', 204
