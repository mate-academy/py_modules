"""
module for payment representation
"""
from tasks import FixedTask, HourlyTask
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
