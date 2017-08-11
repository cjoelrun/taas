from flask import Blueprint, jsonify, request

from taas.parameter.models import Parameter
from taas.database import db

blueprint = Blueprint('parameter', __name__, url_prefix='/parameters')


@blueprint.route('', methods=['GET', 'POST'])
def parameters():
    from taas.parameter.schemas import parameter_schema

    if request.method == 'GET':
        all_params = Parameter.query.all()
        return parameter_schema.dumps(all_params, many=True)

    if request.method == 'POST':
        parameter = parameter_schema.load(request.json, db.session).data
        db.session.add(parameter)
        db.session.commit()

        return parameter_schema.dumps(parameter).data, 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def parameters_by_id(db_id):
    from taas.parameter.schemas import parameter_schema

    parameter = Parameter.query.get(db_id)

    if request.method == 'GET':
        if parameter is None:
            return '{} not found.'.format(db_id), 404
        return parameter_schema.dumps(parameter).data

    if request.method == 'PUT':
        parameter_schema.load(request.json, db.session, parameter)
        db.session.commit()
        return parameter_schema.dumps(parameter).data, 200

    if request.method == 'DELETE':
        if parameter is not None:
            db.session.delete(parameter)
            db.session.commit()
        return '', 204
