"""
module for fixed payment representation
"""
from fixed_task import FixedTask
from payment import Payment
from worker import Worker


class FixedPaymentPerTask(Payment):
    """
    Child class that inherit from Payment and represents fixed payment
    parameters per task which connected with each worker and each worker task.
    """

    def __init__(self, worker: Worker, task: FixedTask):
        super().__init__(worker)
        self.task = task

    def __str__(self) -> str:
        return f"FixedPayment(worker:{self.worker}, task:{self.task}"

    def payment_result(self):
        """
        Return total payment from each fixed payment task.
        :return: int
        """
        if self.worker.presence_at_work and self.task.completed:
            return self.task.total_task_payment
        return 0
