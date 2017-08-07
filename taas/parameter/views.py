from flask import Blueprint, jsonify, request

from taas.parameter.models import Parameter
from taas.database import db

blueprint = Blueprint('parameter', __name__, url_prefix='/parameters')


@blueprint.route('', methods=['GET', 'POST'])
def parameters():
    if request.method == 'GET':
        return jsonify([p.serialize() for p in Parameter.query.all()])

    if request.method == 'POST':
        parameter = Parameter()
        parameter.update_fields(request.json)
        db.session.add(parameter)
        db.session.commit()

        return jsonify(parameter.serialize()), 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def parameters(db_id):
    parameter = Parameter.query.get(db_id)

    if request.method == 'GET':
        if parameter is None:
            return '{} not found.'.format(db_id), 404
        return jsonify(parameter.serialize())

    if request.method == 'PUT':
        parameter.update_fields(request.json)
        db.session.commit()
        return jsonify(parameter.serialize()), 200

    if request.method == 'DELETE':
        if parameter is not None:
            db.session.delete(parameter)
            db.session.commit()
        return '', 204
