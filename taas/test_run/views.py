from flask import Blueprint, jsonify, request

from taas.test_run.models import TestRun
from taas.database import db

blueprint = Blueprint('test_run', __name__, url_prefix='/test_runs')


@blueprint.route('', methods=['GET'])
def test_runs():
    if request.method == 'GET':
        return jsonify([tr.serialize() for tr in TestRun.query.all()])


@blueprint.route('/<db_id>', methods=['GET', 'DELETE'])
def test_runs(db_id):
    test_run = TestRun.query.get(db_id)

    if request.method == 'GET':
        if test_run is None:
            return '{} not found.'.format(db_id), 404
        return jsonify(test_run.serialize())

    if request.method == 'DELETE':
        if test_run is not None:
            db.session.delete(test_run)
            db.session.commit()
        return '', 204
