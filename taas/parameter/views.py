from flask import Blueprint, jsonify

from taas.parameter.models import Parameter

blueprint = Blueprint('parameter', __name__, url_prefix='/parameters')


@blueprint.route('/')
def parameters():
    return jsonify(Parameter.query.all())
