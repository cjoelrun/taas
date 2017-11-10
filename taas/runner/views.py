from flask import Blueprint, request
from taas.database import db
from taas.parameter.models import Parameter
from taas.runner.service import create_test_case_run, create_test_suite_run, execute_test_case_run, execute_test_suite_run
from taas.test_case.models import TestCase
from taas.test_suite.models import TestSuite
from taas.test_suite_run.models import TestSuiteRun

blueprint = Blueprint('runner', __name__, url_prefix='/run')


@blueprint.route('/test-cases/<db_id>', methods=['POST'])
def run_test_case(db_id):
    from taas.test_run.schemas import test_run_schema
    parameter_id = request.json['parameter_id']
    parameter = Parameter.query.get(parameter_id)
    test_case = TestCase.query.get(db_id)

    if parameter.parameter_group_id != test_case.parameter_group_id:
        error_message = 'Parameter {} not a member of ParameterGroup {}'.format(parameter_id, test_case.parameter_group_id)
        return {'error': error_message}, 422

    test_run = create_test_case_run(test_case, parameter_id)
    execute_test_case_run(test_run)
    return test_run_schema.dumps(test_run).data, 200


@blueprint.route('/test-suites/<db_id>', methods=['POST'])
def run_test_suite(db_id):
    from taas.test_suite_run.schemas import test_suite_run_schema
    parameter_id = request.json['parameter_id']
    parameter = Parameter.query.get(parameter_id)
    test_suite = TestSuite.query.get(db_id)

    if parameter.parameter_group_id != test_suite.parameter_group_id:
        error_message = 'Parameter {} not a member of ParameterGroup {}'.format(parameter_id, test_suite.parameter_group_id)
        return {'error': error_message}, 422

    test_suite_run = create_test_suite_run(test_suite, parameter_id)
    execute_test_suite_run(test_suite_run)
    return test_suite_run_schema.dumps(test_suite_run).data, 200


@blueprint.route('/test-suites/finish', methods=['POST'])
def finish_test_suite_runs():
    unfinished_suite_runs = TestSuiteRun.query.filter(TestSuiteRun.status == 'Running')
    for suite_run in unfinished_suite_runs:
        running_cases = [rc for rc in suite_run.test_case_runs if rc.status is None or rc.status == 'Running']
        if len(running_cases) != 0:
            continue
        is_success = all(tc.status == 'Success' for tc in suite_run.test_case_runs)
        suite_run.status = 'Success' if is_success else 'Failed'
        db.session.commit()

    return '', 200
