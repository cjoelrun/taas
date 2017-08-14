from flask import Blueprint, request
from taas.database import db
from taas.execution_run.models import ExecutionRun
from taas.runner.service import RunService

blueprint = Blueprint('runner', __name__, url_prefix='/run')


@blueprint.route('/test-cases/<db_id>', methods=['POST'])
def run_test_case(db_id):
    from taas.test_run.schemas import test_run_schema
    test_run = RunService().run_test_case(db_id)
    return test_run_schema.dumps(test_run).data, 200


@blueprint.route('/execution-runs/<db_id>/finish', methods=['POST'])
def finish_execution_run(db_id):
    print('Finishing execution run {}'.format(db_id))
    execution_run = ExecutionRun.query.get(db_id)
    execution_run.status = 'Success'
    db.session.commit()

    RunService().run_next_step(execution_run.test_run_id)

    return '', 200


