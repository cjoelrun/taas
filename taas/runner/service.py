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
    task = run_test_suite.delay(test_suite_run.id)
    test_suite_run.task_id = task.id
    db.session.add(test_suite_run)
    db.session.commit()


def execute_test_case_run(test_case_run):
    from taas.tasks import run_test_case
    task = run_test_case.delay(test_case_run.id)
    test_case_run.task_id = task.id
    db.session.add(test_case_run)
    db.session.commit()


def cancel_test_case_run(test_case_run):
    from taas.async import celery
    celery.control.revoke(test_case_run.task_id, terminate=True)
    test_case_run.status = 'Cancelled'
    db.session.add(test_case_run)
    db.session.commit()


def cancel_test_suite_run(test_suite_run):
    from taas.async import celery
    celery.control.revoke(test_suite_run.task_id, terminate=True)
    test_suite_run.status = 'Cancelled'
    db.session.add(test_suite_run)
    db.session.commit()
    running_cases = [rc for rc in test_suite_run.test_case_runs if rc.status is None or rc.status == 'Running']
    for rc in running_cases:
        cancel_test_case_run(rc)
