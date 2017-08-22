from taas.execution_run.models import ExecutionRun
from taas.test_run.models import TestRun
from taas.database import db
from taas.test_suite_run.models import TestSuiteRun


def create_test_suite_run(test_suite, parameter_id):
    test_suite_run = TestSuiteRun()
    test_suite_run.test_suite_id = test_suite.id
    test_suite_run.parameter_id = parameter_id

    db.session.add(test_suite_run)
    db.session.commit()

    for test_case in test_suite.test_cases:
        test_case_run = create_test_case_run(test_case, parameter_id)
        test_suite_run.test_case_runs.append(test_case_run)
    db.session.commit()

    return test_suite_run


def create_test_case_run(test_case, parameter_id):
    test_case_run = TestRun()
    test_case_run.test_case_id = test_case.id
    test_case_run.parameter_id = parameter_id

    db.session.add(test_case_run)
    db.session.commit()

    sorted_steps = sorted(test_case.steps, key=lambda step: step.order)
    for step in sorted_steps:
        execution_run = ExecutionRun()
        execution_run.step_id = step.id
        execution_run.test_run_id = test_case_run.id
        db.session.add(execution_run)
    db.session.commit()

    return test_case_run


def execute_test_suite_run(test_suite_run):
    from taas.tasks import run_test_suite
    run_test_suite.delay(test_suite_run.id)


def execute_test_case_run(test_case_run):
    from taas.tasks import run_test_case
    run_test_case.delay(test_case_run.id)
