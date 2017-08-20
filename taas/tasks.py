from taas.async import celery
from taas.database import db
from taas.execution_run.models import ExecutionRun
import requests


@celery.task
def run_strategy(execution_run_id, strategy_name, parameters):
    session = db.create_scoped_session()
    execution_run = session.query(ExecutionRun).get(execution_run_id)
    execution_run.status = 'Running'
    session.commit()

    print('Running strategy {} with {}'.format(strategy_name, parameters))

    execution_run.status = 'Success'
    session.commit()
    session.close()

    response = requests.post('{}/run/execution-runs/{}/finish'.format(celery.callback_url, execution_run_id))
    print(response)
