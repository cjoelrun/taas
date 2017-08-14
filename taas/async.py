from taas.app import create_app
from celery import Celery


def make_celery(app=None):
    app = app or create_app()
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'],
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery()


@celery.task
def run_strategy(execution_run_id, strategy_name, parameters):
    print('Running strategy {} with {}'.format(strategy_name, parameters))
    import requests
    response = requests.post('http://localhost:5000/run/execution-runs/{}/finish'.format(execution_run_id))
    print(response)