from sqlalchemy.orm import joinedload
from taas.execution.models import Execution
from taas.execution_run.models import ExecutionRun
from taas.step.models import Step
from taas.test_case.models import TestCase
from taas.test_run.models import TestRun
from taas.database import db


class RunService:

    def run_test_case(self, test_case_id):
        test_case = TestCase.query.get(test_case_id)

        test_case_run = TestRun()
        test_case_run.status = "started"
        test_case_run.test_case_id = test_case_id

        db.session.add(test_case_run)
        db.session.commit()

        sorted_steps = sorted(test_case.steps, key=lambda step: step.order)
        for step in sorted_steps:
            execution_run = ExecutionRun()
            execution_run.step_id = step.id
            execution_run.test_run_id = test_case_run.id
            db.session.add(execution_run)
        db.session.commit()

        print('Starting run {} for test case {}'.format(test_case_run.id, test_case_id))
        self.run_next_step(test_case_run.id)
        return test_case_run

    def run_next_step(self, test_run_id):
        test_run = TestRun.query.get(test_run_id)

        for execution_run in test_run.execution_runs:
            if execution_run.status is None:
                print('Running next execution {}'.format(execution_run.id))
                execution_run.status = 'Submitted'
                db.session.commit()
                # TODO this is ugly af
                step = Step.query.get(execution_run.step_id)
                execution = Execution.query.get(step.execution_id)
                parameters = {'key': 'value'}
                from taas.tasks import run_strategy
                run_strategy.delay(execution_run.id, execution.strategy, parameters)
                return  # end on next execution run

        # no more exeuction runs, test_run must be over
        print('Finished test run {}'.format(test_run_id))
        test_run.status = 'Success'
        return