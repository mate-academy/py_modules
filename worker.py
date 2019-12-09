"""
Realisation worker model.
Classes
-------
Worker
"""
from typing import List
import task


class Worker:
    """Class worker, need worker name
    Attributes
    ----------
    name - worker name
    Methods
    -------
    confirm()
    take_task()
    """

    def __init__(self, name: str):
        self._name = name
        self._tasks_in_process: List[task.Task] = []

    def __repr__(self):
        return f"Worker: {self._name}"

    def confirm(self, task_confirm, log):
        """make record about completed in log
        Attributes
        ----------
        task_confirm - completed task
        log - the log in which we write
        """
        self._tasks_in_process.remove(task_confirm)
        log.confirm(self._name, task_confirm.get_name(), task_confirm.get_payment())

    def take_task(self, task_in_process):
        """Add task in _tasks_in_process list
         Attributes
        ----------
        task_in_process - the task the worker received
        """
        self._tasks_in_process.append(task_in_process)


if __name__ == "__main__":
    pass
