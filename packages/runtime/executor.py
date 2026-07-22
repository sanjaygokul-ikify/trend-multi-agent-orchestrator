import logging
from typing import List, Optional
from ..core.engine import Engine, Agent, Task
from ..core.exceptions import InvalidAgentError, InvalidTaskError


class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.logger = logging.getLogger(__name__)

    def execute(self, agent: Agent, task: Task) -> None:
        if not agent:
            self.logger.error("Invalid agent")
            raise InvalidAgentError("Invalid agent")
        if not task:
            self.logger.error("Invalid task")
            raise InvalidTaskError("Invalid task")
        # Execute the task
        self.logger.info(f"Task {task.id} executed by agent {agent.id}")
        self.engine.report(agent, task)