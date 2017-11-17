import argh
import taas.app
import taas.async
import taas.tasks
import taas.plugins.plugin_loader as plugin_loader


@argh.decorators.named('start-api')
@argh.arg('--host', default='localhost', help='')
@argh.arg('--port', default='5000', help='')
@argh.arg('--plugin', help='')
def start_api(host=None, port=None, plugin=None):
    plugin_loader.load_plugin(plugin)
    app = taas.app.create_app()
    app.run(host=host, port=port, debug=False)


@argh.decorators.named('start-worker')
@argh.arg('--plugin', help='')
def start_worker(plugin=None):
    plugin_loader.load_plugin(plugin)
    flask_app = taas.app.create_app()
    celery_worker = taas.async.make_celery(flask_app)
    taas.tasks.add_scheduled_tasks(celery_worker)
    # start command: celery -A taas.tasks worker --beat -l info
    celery_worker.start(argv=['taas.tasks', 'worker', '-B', '-l', 'info'])


def main():
    parser = argh.ArghParser()
    parser.add_commands([start_api, start_worker])
    parser.dispatch()


if __name__ == '__main__':
    main()
