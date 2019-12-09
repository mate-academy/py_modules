"""module Worker class"""


class Worker:
    """
    Class to represent worker
    """
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        Returns:
            Name of the worker
        """
        return self.name

    def take_task(self, task, log):
        """
        Take task and try to confirm it in log
        Args:
            task: task that worker try to confirm
            log: current log
        """
        log.confirm(self, task)
