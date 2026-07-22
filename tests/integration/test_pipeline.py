import unittest
from packages.core import Engine, Policy, Agent, Task
from services import orchestrator

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        policy = Policy()
        engine = Engine([], [], policy)
        agent = Agent('agent1')
        task = Task('task1', 'type1')
        engine.register_agent(agent)
        engine.assign_task(task, agent)
        engine.execute_task(task, agent)
        orchestrator_instance = orchestrator.Orchestrator(engine)
        orchestrator_instance.start()
        orchestrator_instance.stop()