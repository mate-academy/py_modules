"""register container"""


class Register:
    """container for task and workers. Base on dictionary"""
    def __init__(self):
        self.register_task = {}

    def add_task(self, worker, task):
        """add new task on dictionary"""
        self.register_task[task] = worker

    def __repr__(self):
        return f"{self.register_task}"

    def __iter__(self):
        return self

    def __next__(self):
        if not self.register_task:
            raise StopIteration
        return self.register_task.popitem()

    def __str__(self):
        return f"{self.register_task}"
