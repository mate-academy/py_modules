"""
Realisation task model.
Classes
-------
Task
FixedPayment
PaymentPerHour
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


if __name__ == "__main__":
    pass
