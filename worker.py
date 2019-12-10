"""This module describe class of the worker"""


class Worker:
    """Class of worker"""
    def __init__(self, name):
        self.name = name

    def complete_task(self, task, log):
        """Only worker can confirm task completion"""
        log.confirm(self, task)

    def get_name(self):
        """Get name of worker"""
        return self.name
