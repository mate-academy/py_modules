"""
Module used to create tasks.
The task can be of two types: with fixed payment
and hourly payment.

Classes
-------
Task
"""


class Task:
    """
    A class that define type of the task and payment for this task
    Attributes
    ----------
    task_type : str  --  type of the task
    hours : float -- number of hours for hourly task

    Methods
    -------
    payment()
    """

    def __init__(self, task_type='fixed', hours=None):
        self.task_type = task_type.lower()
        self.hours = hours

    def payment(self):
        """Return payment that worker get for the task"""
        fixed_pay = 100
        hourly_rate = 10
        total = 0
        if self.task_type == 'fixed':
            return fixed_pay

        if self.task_type == 'hourly':
            try:
                total = self.hours * hourly_rate
            except TypeError:
                raise Exception("TypeError! Parameter hours not specified")
        return total

    def get_task_type(self):
        """Return type of the task"""
        return self.task_type
