from flask import Blueprint, request

from taas.database import db
from taas.execution.models import Execution

blueprint = Blueprint('execution', __name__, url_prefix='/executions')


@blueprint.route('', methods=['GET', 'POST'])
def executions():
    from taas.execution.schemas import execution_schema

    if request.method == 'GET':
        all_executions = Execution.query.all()
        return execution_schema.dumps(all_executions, many=True)

    if request.method == 'POST':
        execution = execution_schema.load(request.json, db.session).data
        db.session.add(execution)
        db.session.commit()

        return execution_schema.dumps(execution).data, 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def executions_by_id(db_id):
    from taas.execution.schemas import execution_schema

    execution = Execution.query.get(db_id)

    if request.method == 'GET':
        if execution is None:
            return '{} not found.'.format(db_id), 404
        return execution_schema.dumps(execution).data

    if request.method == 'PUT':
        execution_schema.load(request.json, db.session, execution)
        db.session.commit()
        return execution_schema.dumps(execution).data, 200

    if request.method == 'DELETE':
        if execution is not None:
            db.session.delete(execution)
            db.session.commit()
        return '', 204
