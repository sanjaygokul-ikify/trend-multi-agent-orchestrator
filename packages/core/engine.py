import logging
from typing import Dict, List, Optional
from .types import Agent, Task, Policy
from .exceptions import InvalidAgentError, InvalidTaskError


class Engine:
    def __init__(self, agents: List[Agent], tasks: List[Task], policy: Policy):
        self.agents = agents
        self.tasks = tasks
        self.policy = policy
        self.logger = logging.getLogger(__name__)

    def register_agent(self, agent: Agent) -> None:
        if not agent:
            self.logger.error("Invalid agent")
            raise InvalidAgentError("Invalid agent")
        self.agents.append(agent)
        self.logger.info(f"Agent {agent.id} registered")

    def assign_task(self, task: Task, agent: Agent) -> None:
        if not task:
            self.logger.error("Invalid task")
            raise InvalidTaskError("Invalid task")
        if not agent:
            self.logger.error("Invalid agent")
            raise InvalidAgentError("Invalid agent")
        agent.tasks.append(task)
        self.tasks.append(task)  # Add task to the tasks list
        self.logger.info(f"Task {task.id} assigned to agent {agent.id}")

    def execute_task(self, task: Task, agent: Agent) -> None:
        if not task:
            self.logger.error("Invalid task")
            raise InvalidTaskError("Invalid task")
        if not agent:
            self.logger.error("Invalid agent")
            raise InvalidAgentError("Invalid agent")
        # Execute the task
        self.logger.info(f"Task {task.id} executed by agent {agent.id}")

    def adapt(self) -> None:
        self.policy.update(self.agents, self.tasks)
        self.logger.info("Policy updated")

    def report(self, agent: Agent, task: Task) -> None:
        if not agent:
            self.logger.error("Invalid agent")
            raise InvalidAgentError("Invalid agent")
        if not task:
            self.logger.error("Invalid task")
            raise InvalidTaskError("Invalid task")
        # Report the task execution result
        self.logger.info(f"Task {task.id} reported by agent {agent.id}")