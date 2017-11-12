
class BaseStrategy(object):
    def __init__(self, parameters, execution_data, runtime_data):
        self._parameters = parameters
        self._execution_data = execution_data
        self._runtime_data = runtime_data

    def execute(self):
        raise NotImplementedError

    def add_runtime_entry(self, key, value):
        self._runtime_data[key] = value

    def get_runtime_data(self):
        return self._runtime_data


class Result:
    def __init__(self, success, message):
        self.success = success
        self.message = message
