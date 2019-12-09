"""
Realisation task model.
Classes
-------
Task
"""


class Task:
    """parent class task
    Attributes
    ----------
    task_name - new task name
    Methods
    -------
    get_name()
    """
    def __init__(self, task_name):
        self._task_name = task_name

    def __repr__(self):
        return f"Task: {self._task_name}"

    def get_name(self):
        """return task name"""
        return self._task_name


if __name__ == "__main__":
    pass
