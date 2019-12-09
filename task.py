"""Module class Task"""


class Task:
    """Class Task accepts one argument - status.
    'default fixed'"""
    def __init__(self, status='fixed', time=1):
        self.status = status
        self.time_work = time

    def get_status_task(self):
        """Get status Task"""
        return self.status

    def set__status_task(self, status):
        """Set status task"""
        self.status = status

    def calc_payment(self):
        """Calculate payment"""
        if self.status == 'fixed':
            return '$20'
        return '${}'.format(15*self.time_work)
