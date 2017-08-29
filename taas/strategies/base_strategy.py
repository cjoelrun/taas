
class BaseStrategy(object):
    def __init__(self, parameters=None, execution_data=None):
        self._parameters = parameters
        self._execution_data = execution_data

    def set_up(self):
        pass

    def perform_action(self):
        raise NotImplementedError

    def perform_validation(self):
        raise NotImplementedError

    def tear_down(self):
        pass


class Result:
    def __init__(self, success=None, message=None):
        self.success = success
        self.message = message
