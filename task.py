"""This module describes class of the task"""


class Task:
    """Class of task
    By default all tasks are fixed payment,
    unless explicitly indicated hourly payment task
    """
    def __init__(self, payment, estimate, is_hourly_pay=False):
        self.payment = float(payment)
        self.estimate = estimate
        self.is_hourly_pay = is_hourly_pay

    def get_payment_type(self):
        """Get type of payment"""
        if self.is_hourly_pay:
            return 'It is hourly payment task'
        return 'It is fixed payment task'

    def get_estimate(self):
        """Get estimate"""
        return f'{self.estimate}h'
