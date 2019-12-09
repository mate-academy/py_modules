"""
module for payment representation
"""
from worker import Worker


class Payment:
    """
    Parent class payment which contain information about every worker.
    """

    def __init__(self, worker: Worker):
        self.worker = worker

    def __str__(self) -> str:
        return f"Payment(worker:{self.worker}"

    def payment_result(self):
        """
        Return daily worker salary.
        :return: int
        """
        return self.worker.hourly_rate * self.worker.working_hours_per_day
