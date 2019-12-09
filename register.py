"""Module class Register"""


class Register:
    """Class Register where all the tasks are recorded"""
    def __init__(self):
        self.register = []

    def add_task(self, worker, task):
        """Add new task"""
        self.register.append([worker.get_name(), task.calc_payment()])

    def get_register(self):
        """Get register"""
        return '\n'.join(['\t'.join(lst) for lst in self.register])
