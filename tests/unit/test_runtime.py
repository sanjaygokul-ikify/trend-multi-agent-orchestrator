import unittest
from packages.core import Engine

class TestRuntime(unittest.TestCase):
    def test_runtime(self):
        policy = Engine.Policy()
        engine = Engine([], [], policy)
        agent = Engine.Agent('agent1')
        task = Engine.Task('task1', 'type1')
        engine.register_agent(agent)
        engine.assign_task(task, agent)
        engine.execute_task(task, agent)