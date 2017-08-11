from flask import Blueprint, jsonify, request

from taas.step.models import Step
from taas.database import db

blueprint = Blueprint('step', __name__, url_prefix='/steps')


@blueprint.route('', methods=['GET', 'POST'])
def steps():
    from taas.step.schemas import step_schema

    if request.method == 'GET':
        all_params = Step.query.all()
        return step_schema.dumps(all_params, many=True)

    if request.method == 'POST':
        step = step_schema.load(request.json, db.session).data
        db.session.add(step)
        db.session.commit()

        return step_schema.dumps(step).data, 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def steps_by_id(db_id):
    from taas.step.schemas import step_schema

    step = Step.query.get(db_id)

    if request.method == 'GET':
        if step is None:
            return '{} not found.'.format(db_id), 404
        return step_schema.dumps(step).data

    if request.method == 'PUT':
        step_schema.load(request.json, db.session, step)
        db.session.commit()
        return step_schema.dumps(step).data, 200

    if request.method == 'DELETE':
        if step is not None:
            db.session.delete(step)
            db.session.commit()
        return '', 204
