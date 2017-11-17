import importlib
import imp
import os
import json


def load_plugin(plugin_path):
    if not os.path.exists(plugin_path):
        raise IOError('Plugin path not found: {}'.format(plugin_path))
    config_path = os.path.join(plugin_path, 'config.json')
    if not os.path.exists(config_path):
        raise ImportError('No config found in {}'.format(plugin_path))
    config = json.load(open(config_path))
    imp.load_package(config['name'], plugin_path)
    importlib.import_module('taas.strategies.builtin')

