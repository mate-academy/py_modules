"""module containing HourlyPaymentTask class"""
import task


class HourlyPaymentTask(task.Task):
    """Class to represent task with hourly payment"""
    def __init__(self, task_name, payment, time_to_complete):
        super().__init__(task_name, payment)
        self.time_to_complete = time_to_complete

    def get_payment(self):
        """
        Calculate payment for all time of work
        Returns:
            Payment for given time of work
        """
        return self.payment * self.time_to_complete
