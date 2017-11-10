import time

from taas.strategies.base_strategy import BaseStrategy, Result


class WaitStrategy(BaseStrategy):
    def execute(self):
        wait_time = self._execution_data.get('wait_time', 1)
        time.sleep(wait_time)
        print("Waited {} seconds".format(wait_time))
        return Result(True, "Wait complete.")
