"""Module class Log"""
import register


class Log:
    """Class Log where all the work is recorded"""
    def __init__(self):
        self.register = register.Register()

    def confirm(self, worker, task):
        """Confirm task"""
        self.register.add_task(worker, task)

    def report(self):
        """Report about task"""
        return self.register.get_register()
