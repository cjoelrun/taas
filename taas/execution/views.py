from flask import Blueprint, jsonify, request

from taas.database import db
from taas.execution.models import Execution

blueprint = Blueprint('execution', __name__, url_prefix='/executions')


@blueprint.route('', methods=['GET', 'POST'])
def executions():
    if request.method == 'GET':
        return jsonify([e.serialize() for e in Execution.query.all()])

    if request.method == 'POST':
        execution = Execution()
        _set_fields(execution, request.json)
        db.session.add(execution)
        db.session.commit()

        return jsonify(execution.serialize()), 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def executions(db_id):
    execution = Execution.query.get(db_id)

    if request.method == 'GET':
        if execution is None:
            return '{} not found.'.format(db_id), 404
        return jsonify(execution.serialize())

    if request.method == 'PUT':
        _set_fields(execution, request.json)
        db.session.commit()
        return jsonify(execution.serialize()), 200

    if request.method == 'DELETE':
        if execution is not None:
            db.session.delete(execution)
            db.session.commit()
        return '', 204


def _set_fields(execution, json):
    execution.data = json.get('data', None)
    execution.description = json.get('description', None)
    execution.strategy = json.get('strategy', None)
    execution.type = json.get('type', None)
