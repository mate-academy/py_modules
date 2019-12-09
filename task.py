"""module containing Task class"""


class Task:
    """class representing task with fixed payment"""
    def __init__(self, task_name, payment):
        self.task_name = task_name
        self.payment = payment
        self.completed = False

    def get_status(self):
        """
        Returns:
            Boolean. Status of task: completed or not completed
        """
        return self.completed

    def change_status(self):
        """
        Returns:
            Boolean. Changed status of task
        """
        self.completed = not self.completed

    def get_task_name(self):
        """
        Returns:
            Task name
        """
        return self.task_name

    def get_payment(self):
        """
        Returns:
            Payment for completing the task
        """
        return self.payment
