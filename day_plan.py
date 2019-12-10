"""This script is a part of task py_modules
(being the tasktracker.py separated by classes)"""
import tasks


class DailyPlan:
    """This class objects collect
    and maintain the list of tasks to be executed"""
    def __init__(self):
        """Initiate the empty list"""
        self.tasks = []

    def create_plan(self, *to_be_created: tasks.Task):
        """Fill the list of tasks to be executed"""
        return self.tasks.extend((task.name, task.rate)
                                 for task in to_be_created)

    def provide_task_to_worker(self):
        """Eliminate last task input from the daily plan
        as it has already been assigned to worker"""
        return self.tasks.pop()

    def get_plan(self):
        """Provide daily plan being recent list of tasks"""
        return self.tasks
