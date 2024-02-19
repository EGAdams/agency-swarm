from typing import Callable, List

# Functions for various test pipeline strategies
def compile_strategy():
    # Compilation logic goes here
    pass

def execute_tests_strategy():
    # Test execution logic goes here
    pass

def report_tests_strategy():
    # Test reporting logic goes here
    pass

# Function to execute a strategy
def execute_strategy(strategy: Callable):
    strategy()

# Function to notify observers
def notify_observers(observers: List[Callable], event: str):
    for observer in observers:
        observer(event)

# Observer functions
def on_test_compiled(event):
    if event == "compiled":
        # Handle test compiled event
        pass

def on_test_executed(event):
    if event == "executed":
        # Handle test executed event
        pass

def on_test_reported(event):
    if event == "reported":
        # Handle test reported event
        pass

# Test Pipeline Orchestrator Agent
class TestPipelineOrchestratorAgent:
    def __init__(self):
        self.observers = []
        self.current_strategy = None

    def add_observer(self, observer: Callable):
        self.observers.append(observer)

    def set_strategy(self, strategy: Callable):
        self.current_strategy = strategy

    def execute_strategy(self):
        if self.current_strategy:
            execute_strategy(self.current_strategy)
            self.notify_observers()

    def notify_observers(self):
        if self.current_strategy == compile_strategy:
            notify_observers(self.observers, "compiled")
        elif self.current_strategy == execute_tests_strategy:
            notify_observers(self.observers, "executed")
        elif self.current_strategy == report_tests_strategy:
            notify_observers(self.observers, "reported")

# Example usage
if __name__ == "__main__":
    orchestrator = TestPipelineOrchestratorAgent()
    orchestrator.set_strategy(compile_strategy)
    orchestrator.add_observer(on_test_compiled)
    orchestrator.add_observer(on_test_executed)
    orchestrator.add_observer(on_test_reported)
    orchestrator.execute_strategy()

    # Further logic to set different strategies and add observers
