from flask import Blueprint, jsonify, request

from taas.step.models import Step
from taas.database import db

blueprint = Blueprint('step', __name__, url_prefix='/steps')


@blueprint.route('', methods=['GET', 'POST'])
def steps():
    if request.method == 'GET':
        return jsonify([s.serialize() for s in Step.query.all()])

    if request.method == 'POST':
        step = Step()
        step.update_fields(request.json)
        db.session.add(step)
        db.session.commit()

        return jsonify(step.serialize()), 201


@blueprint.route('/<db_id>', methods=['GET', 'PUT', 'DELETE'])
def steps_by_id(db_id):
    step = Step.query.get(db_id)

    if request.method == 'GET':
        if step is None:
            return '{} not found.'.format(db_id), 404
        return jsonify(step.serialize())

    if request.method == 'PUT':
        step.update_fields(request.json)
        db.session.commit()
        return jsonify(step.serialize()), 200

    if request.method == 'DELETE':
        if step is not None:
            db.session.delete(step)
            db.session.commit()
        return '', 204
