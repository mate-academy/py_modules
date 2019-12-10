"""
task module
"""
# from hourly import Hourly
# from fixed import Fixed


class Task:
    """
    Parent object
    define Task object
    """

    def __init__(self, task_name):
        self.hour_tasks = {'Task1': 10, 'Task2': 20}
        self.fixed_tasks = {'Task3': 500}
        self._tasks = {**self.hour_tasks, **self.fixed_tasks}
        self.task_name = task_name
        self.price = None

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
        return self.price

    def get_rate(self):
        """
        Return total price
        :return:
        """
        self.price = self.get_price()
        return f"{self.price}$"


if __name__ == '__main__':
    pass
