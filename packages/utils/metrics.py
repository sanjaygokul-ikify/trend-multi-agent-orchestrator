import time
from typing import Dict

class Metrics:
    def __init__(self):
        self.metrics = {}

    def record(self, name: str, value: int):
        self.metrics[name] = value

    def get(self, name: str) -> int:
        return self.metrics.get(name, 0)

    def timer(self, name: str, func):
        def decorator(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.record(name, int((end_time - start_time) * 1000))
            return result
        return decorator