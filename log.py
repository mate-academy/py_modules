"""This module describe class of the log"""


class Log:
    """Class of the log"""
    def __init__(self):
        self.complete_tasks = {}

    def confirm(self, worker, task):
        """Confirm task completion """
        payment = task.payment
        if task.is_hourly_pay:
            payment *= task.estimate
        self.complete_tasks[worker.name] = payment

    def report(self):
        """Get report of completed tasks"""
        report = '\n'.join(f'{key}\t{val}$' for key, val in
                           self.complete_tasks.items())
        return report
