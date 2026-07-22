from packages.core import Engine
from packages.utils import logging

class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.logger = logging.Logger('orchestrator').logger

    def start(self):
        self.logger.info('Starting orchestrator')
        self.engine.adapt()

    def stop(self):
        self.logger.info('Stopping orchestrator')