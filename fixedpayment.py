"""
Realisation task model.
Classes
-------
FixedPayment
"""
from task import Task


class FixedPayment(Task):
    """Fixed payment task class
    Attributes
    ----------
    task_name - new task name
    payment - payment for task
    Methods
    -------
    get_payment()
    """
    def __init__(self, task_name, payment):
        super().__init__(task_name)
        self._payment = payment

    def get_payment(self):
        """return task payment"""
        return self._payment
