"""
log module
"""
from worker import Worker
from task import Task


class Log:
    """
    Log object
    """
    def __init__(self, worker, task):
        self.worker = worker
        self.task = task
        self.worker_confirm = Worker()
        self.task_confirm = Task(self.task)
        self._confirm = False

    def confirm(self):
        """
        See if we can provide such worker and task
        :return:
        """
        if self.worker in self.worker_confirm.worker_available():
            if self.task in self.task_confirm.task_acceptable():
                self._confirm = True
        return self._confirm

    def report(self):
        """
        Ask user to pay
        :return:
        """
        if self.confirm():
            return f"Please pay {self.task_confirm.get_rate()} to {self.worker} for {self.task}!"
        return f"Worker or Task doesnt exists"


if __name__ == '__main__':
    pass
