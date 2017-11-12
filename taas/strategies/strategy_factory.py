from taas.strategies.base_strategy import BaseStrategy


class StrategyFactory(object):
    def __init__(self, parameters):
        self._parameters = parameters

    def create_strategy(self, strategy_name, execution_parameters, runtime_data):
        subclasses = self._all_subclasses(BaseStrategy)
        try:
            return self._get_next_subclass(subclasses, strategy_name)(self._parameters, execution_parameters, runtime_data)
        except StopIteration:
            raise Exception("Could not find {0} in {1}".format(strategy_name, subclasses))

    def _all_subclasses(self, clazz):
        return clazz.__subclasses__() + [g for s in clazz.__subclasses__() for g in self._all_subclasses(s)]

    def _get_next_subclass(self, subclasses, strategy_name):
        return next(subclass for subclass in subclasses if (strategy_name == self._fully_qualified_class_name(subclass)))

    def _fully_qualified_class_name(self, clazz):
        return '{}.{}'.format(clazz.__module__, clazz.__name__)
