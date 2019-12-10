"""
hourly payment module
"""
from task import Task


class Hourly(Task):
    """
    Task child object
    We can set random time
    for task completion
    """
    # tasks = {'Task1': 10, 'Task2': 20}

    def __init__(self, task_name):
        super().__init__(task_name)
        self._time = 5  # random.randint(1, 11)
        self.price = self.hour_tasks[self.task_name] * self._time


if __name__ == '__main__':
    pass
