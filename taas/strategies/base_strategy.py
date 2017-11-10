
class BaseStrategy(object):
    def __init__(self, parameters=None, execution_data=None):
        self._parameters = parameters
        self._execution_data = execution_data

    def execute(self):
        raise NotImplementedError


class Result:
    def __init__(self, success=None, message=None):
        self.success = success
        self.message = message
