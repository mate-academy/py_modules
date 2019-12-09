"""
fixed payment module
"""
from task import Task


class Fixed(Task):
    """
    Task child object
    We can update tasks dict
    """
    tasks = {'Task3': 500}

    def __init__(self, task_name):
        super().__init__(task_name)
        # self.tasks = {'Task3': 500}
        self._time = 1
        self.price = self.tasks[self.task_name] * self._time


if __name__ == '__main__':
    pass
