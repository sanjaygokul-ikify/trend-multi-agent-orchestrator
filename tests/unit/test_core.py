import unittest
from packages.core import Agent, Task, Engine, Policy, InvalidAgentError, InvalidTaskError

class TestCore(unittest.TestCase):
    def test_agent(self):
        agent = Agent('agent1')
        self.assertEqual(agent.id, 'agent1')
        self.assertEqual(agent.tasks, [])

    def test_task(self):
        task = Task('task1', 'type1')
        self.assertEqual(task.id, 'task1')
        self.assertEqual(task.type, 'type1')

    def test_engine(self):
        policy = Policy()
        engine = Engine([], [], policy)
        self.assertEqual(engine.agents, [])
        self.assertEqual(engine.tasks, [])
        self.assertEqual(engine.policy, policy)

    def test_register_agent(self):
        policy = Policy()
        engine = Engine([], [], policy)
        agent = Agent('agent1')
        engine.register_agent(agent)
        self.assertEqual(engine.agents, [agent])

    def test_assign_task(self):
        policy = Policy()
        engine = Engine([Agent('agent1')], [Task('task1', 'type1')], policy)
        engine.assign_task(engine.tasks[0], engine.agents[0])
        self.assertEqual(engine.agents[0].tasks, [engine.tasks[0]])

    def test_execute_task(self):
        policy = Policy()
        engine = Engine([Agent('agent1')], [Task('task1', 'type1')], policy)
        engine.assign_task(engine.tasks[0], engine.agents[0])
        engine.execute_task(engine.tasks[0], engine.agents[0])

    def test_adapt(self):
        policy = Policy()
        engine = Engine([], [], policy)
        engine.adapt()

    def test_report(self):
        policy = Policy()
        engine = Engine([Agent('agent1')], [Task('task1', 'type1')], policy)
        engine.assign_task(engine.tasks[0], engine.agents[0])
        engine.report(engine.agents[0], engine.tasks[0])

    def test_invalid_agent(self):
        policy = Policy()
        engine = Engine([], [], policy)
        with self.assertRaises(InvalidAgentError):
            engine.register_agent(None)

    def test_invalid_task(self):
        policy = Policy()
        engine = Engine([Agent('agent1')], [], policy)
        with self.assertRaises(InvalidTaskError):
            engine.assign_task(None, engine.agents[0])