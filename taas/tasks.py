import time

from celery.schedules import crontab
from taas.async import celery
from celery.utils.log import get_task_logger
from taas.client import TaasClient
from taas.strategies.base_strategy import Result
from taas.strategies.strategy_factory import StrategyFactory

logger = get_task_logger(__name__)


@celery.task
def run_test_case(test_case_run_id):
    logger.info('Init test case run {}'.format(test_case_run_id))

    taas_client = TaasClient(celery.callback_url)

    test_case_run = taas_client.test_case_run.get_by_id(test_case_run_id)
    test_case_run['status'] = 'Running'
    taas_client.test_case_run.update(test_case_run_id, test_case_run)

    parameters = taas_client.parameter.get_by_id(test_case_run['parameter_id'])
    strategy_factory = StrategyFactory(parameters['data'])
    logger.info('Running test case run {} with params {}'.format(test_case_run_id, parameters['data']))
    runtime_data = {}
    for execution_run_id in test_case_run['execution_runs']:
        try:
            execution_run = taas_client.execution_run.get_by_id(execution_run_id)
            step = taas_client.step.get_by_id(execution_run['step'])
            execution = taas_client.execution.get_by_id(step['execution'])
            logger.info('Running strategy {} with {}'.format(execution['strategy'], execution['data']))
            strategy = strategy_factory.create_strategy(execution['strategy'], execution['data'], runtime_data)
            result = strategy.execute()
            logger.info('Finished strategy {} with {}'.format(execution['strategy'], execution['data']))
            logger.info('Strategy {} result: {} -- {}'.format(execution['strategy'], result.success, result.message))
        except Exception as err:
            logger.error('Strategy execution error: {}'.format(err.message))
            result = Result(False, err.message)

        execution_run['status'] = 'Success' if result.success else 'Failure'
        taas_client.execution_run.update(execution_run_id, execution_run)

        if not result.success:
            test_case_run['status'] = 'Failure'
            taas_client.test_case_run.update(test_case_run_id, test_case_run)
            return

    test_case_run['status'] = 'Success'
    taas_client.test_case_run.update(test_case_run_id, test_case_run)


@celery.task
def run_test_suite(test_suite_run_id, delay=0):
    logger.info('Running test suite run {}'.format(test_suite_run_id))

    taas_client = TaasClient(celery.callback_url)

    test_suite_run = taas_client.test_suite_run.get_by_id(test_suite_run_id)
    test_suite_run['status'] = 'Running'
    taas_client.test_suite_run.update(test_suite_run_id, test_suite_run)

    for case_run_id in test_suite_run['test_case_runs']:
        time.sleep(delay)
        run_test_case.delay(case_run_id)


@celery.task
def finish_test_suites():
    logger.info('Finishing test suites.')

    taas_client = TaasClient(celery.callback_url)
    taas_client.runner.finish_test_suites()


celery.conf.beat_schedule = {
    'finish-test-suites': {
        'task': 'taas.tasks.finish_test_suites',
        'schedule': crontab(),
        'args': None
    }
}

celery.conf.timezone = 'UTC'
