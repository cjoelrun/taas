import importlib


def load_strategies(plugins):
    plugins.append("taas.strategies.builtin")
    for plugin in plugins:
        importlib.import_module(plugin)
