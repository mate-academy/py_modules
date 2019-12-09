"""
Module used to create new workers.

Classes
-------
Worker
"""


import task
import log


class Worker:
    """
    A class that represent a worker
    Attributes
    ----------
    name : str  --  name of a worker

    Methods
    -------
    confirm(task, log)
    get_name()
    """
    def __init__(self, name):
        self.name = name

    def confirm(self, task_: task.Task, log_: log.Log):
        """Add worker and his payment to the database"""
        if self.name not in log_.database.keys():
            log_.database[self.name] = task_.payment()
        else:
            log_.database[self.name] += task_.payment()

    def get_name(self):
        """Return name of the worker"""
        return self.name
