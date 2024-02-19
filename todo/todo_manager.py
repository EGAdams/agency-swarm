import threading
from abc import ABC, abstractmethod

# Singleton pattern to ensure only one instance of TodoManager exists.
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Observer pattern to notify about task list changes.
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# Concrete implementation of a task manager that uses Singleton and Observer.
class TodoManager(Subject, metaclass=SingletonMeta):
    def __init__(self):
        self._observers = []
        self.tasks = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def add_task(self, task):
        self.tasks.append(task)
        self.notify()

    def remove_task(self, task):
        self.tasks.remove(task)
        self.notify()

    def complete_task(self, task):
        # Assuming Task has a 'completed' attribute.
        task.completed = True
        self.notify()
