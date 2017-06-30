from flask import Blueprint, jsonify

from taas.step.models import Step

blueprint = Blueprint('step', __name__, url_prefix='/steps')


@blueprint.route('/')
def steps():
    return jsonify(Step.query.all())
