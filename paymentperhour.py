"""
Realisation task model.
Classes
-------
PaymentPerHour
"""
from task import Task


class PaymentPerHour(Task):
    """Payment per hour task class
    Attributes
    ----------
    task_name - new task name
    payment_per_hour - payment for one hour of work
    hours_worked - how many hours worker worked
    Methods
    -------
    get_payment()
    """
    def __init__(self, task_name, payment_per_hour, hours_worked):
        super().__init__(task_name)
        self._payment_per_hour = payment_per_hour
        self._hours_worked = hours_worked

    def get_payment(self):
        """return task payment per hour * hours worked"""
        return self._payment_per_hour * self._hours_worked
