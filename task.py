"""
task module
"""
from hourly import Hourly
from fixed import Fixed


class Task:
    """
    Parent object
    define Task object
    """

    def __init__(self, task_name):
        self._tasks = {**Hourly.tasks, **Fixed.tasks}
        self.task_name = task_name
        self._price = None

    def task_acceptable(self):
        """
        See we can accept this type of task
        :return:
        """
        return self._tasks

    def get_price(self):
        """
        Check what type of payment task has
        :return:
        """
        if self.task_name in Hourly.tasks:
            self._price = Hourly(self.task_name).price
        else:
            self._price = Fixed(self.task_name).price
        return self._price

    def get_rate(self):
        """
        Return total price
        :return:
        """
        self._price = self.get_price()
        return f"{self._price}$"


if __name__ == '__main__':
    pass
