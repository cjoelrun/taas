from flask import Blueprint, request

from taas.parameter_group.models import ParameterGroup
from taas.database import db

blueprint = Blueprint('parameter_groups', __name__, url_prefix='/parameter-groups')


@blueprint.route('', methods=['GET', 'POST'])
def parameter_groups():
    from taas.parameter_group.schemas import parameter_group_schema

    if request.method == 'GET':
        all_param_groups = ParameterGroup.query.all()
        return parameter_group_schema.dumps(all_param_groups, many=True)

    if request.method == 'POST':
        parameter_group = parameter_group_schema.load(request.json, db.session).data
        db.session.add(parameter_group)
        db.session.commit()

        return parameter_group_schema.dumps(parameter_group).data, 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def parameter_groups_by_id(db_id):
    from taas.parameter_group.schemas import parameter_group_schema

    parameter_group = ParameterGroup.query.get(db_id)

    if request.method == 'GET':
        if parameter_group is None:
            return '{} not found.'.format(db_id), 404
        return parameter_group_schema.dumps(parameter_group).data

    if request.method == 'PUT':
        parameter_group_schema.load(request.json, db.session, parameter_group)
        db.session.commit()
        return parameter_group_schema.dumps(parameter_group).data, 200

    if request.method == 'DELETE':
        if parameter_group is not None:
            db.session.delete(parameter_group)
            db.session.commit()
        return '', 204
