"""
module for hourly payment representation
"""
from hourly_task import HourlyTask
from payment import Payment
from worker import Worker


class HourlyPaymentPerTask(Payment):
    """
    Child class that inherit from Payment and represents hourly payment
    parameters per task which connected with each worker and each worker task.
    """

    def __init__(self, worker: Worker, task: HourlyTask):
        super().__init__(worker)
        self.task = task

    def __str__(self) -> str:
        return f"HourlyPayment(worker:{self.worker}, task:{self.task}"

    def payment_result(self):
        """
        Return total payment from each hourly payment task.
        :return: int
        """
        if self.worker.presence_at_work \
                and self.task.completed \
                and self.task.total_task_hours >= self.task.estimated_hours:
            return self.task.total_task_hours * self.worker.hourly_rate
        return 0
