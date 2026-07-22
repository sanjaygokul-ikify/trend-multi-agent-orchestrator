import argparse
from packages.core import Engine
from services import orchestrator

def main():
    parser = argparse.ArgumentParser(description='Multi-Agent Orchestrator')
    parser.add_argument('--start', action='store_true', help='Start the orchestrator')
    parser.add_argument('--stop', action='store_true', help='Stop the orchestrator')
    args = parser.parse_args()

    engine = Engine([], [], orchestrator.Policy())
    orchestrator_instance = orchestrator.Orchestrator(engine)

    if args.start:
        orchestrator_instance.start()
    elif args.stop:
        orchestrator_instance.stop()