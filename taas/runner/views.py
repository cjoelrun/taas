from flask import Blueprint, request
from taas.runner.service import create_test_case_run, create_test_suite_run, execute_test_case_run, execute_test_suite_run
from taas.test_case.models import TestCase
from taas.test_suite.models import TestSuite

blueprint = Blueprint('runner', __name__, url_prefix='/run')


@blueprint.route('/test-cases/<db_id>', methods=['POST'])
def run_test_case(db_id):
    from taas.test_run.schemas import test_run_schema
    test_case = TestCase.query.get(db_id)
    test_run = create_test_case_run(test_case, request.json['parameter_id'])
    execute_test_case_run(test_run)
    return test_run_schema.dumps(test_run).data, 200


@blueprint.route('/test-suites/<db_id>', methods=['POST'])
def run_test_suite(db_id):
    from taas.test_suite_run.schemas import test_suite_run_schema
    test_suite = TestSuite.query.get(db_id)
    test_suite_run = create_test_suite_run(test_suite, request.json['parameter_id'])
    execute_test_suite_run(test_suite_run)
    return test_suite_run_schema.dumps(test_suite_run).data, 200
