"""module containing Log class"""


class Log:
    """Class to represent log"""
    def __init__(self):
        self.payments = {}

    def confirm(self, worker, task):
        """
        If task doesnt completed allow worker to complete it.
        Calculate total payment for worker and add it to log
        Args:
            worker:
            task:
        """
        if not task.get_status():
            task.change_status()
            if worker.get_name() not in self.payments:
                self.payments[worker.get_name()] = task.get_payment()
            else:
                self.payments[worker.get_name()] += task.get_payment()
            return "Confirmed"

        return "Rejected. Task already completed"

    def report(self):
        """
        Returns:
            Formed log report
        """
        return '\n'.join(f"{name}\t${payment}"
                         for name, payment in self.payments.items())
