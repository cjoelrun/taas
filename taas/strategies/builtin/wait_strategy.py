import time

from taas.strategies.base_strategy import BaseStrategy, Result


class WaitStrategy(BaseStrategy):
    def perform_action(self):
        wait_time = self._execution_data.get('wait_time', 1)
        time.sleep(wait_time)
        print("Waited {} seconds".format(wait_time))

    def perform_validation(self):
        return Result(True, "Wait complete.")
