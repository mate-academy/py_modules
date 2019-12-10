"""This script is a part of task py_modules
(being the tasktracker.py separated by classes)"""


class Worker:
    """This class represents an object that has its own identity,
    obtains tasks (with automatic task plan update) and adds log
    for the tasks executed"""
    def __init__(self, name):
        """Initiate the worker"""
        self.name = name
        self.current_task = None

    def get_name(self):
        """Provide worker's name"""
        return self.name

    def get_task_from_dp(self, daily_plan):
        """Obtain the task from the task list (DailyPlan) on LIFO basis
        and update the list by removing the task obtained"""
        self.current_task = daily_plan.provide_task_to_worker()

    def get_current_task(self):
        """Provide the task taken from daily plan"""
        return self.current_task

    def log_task(self, log, dp_task, time_spent=1):
        """Send the log to the log file"""
        log_message = (self.name, dp_task, time_spent)
        log.write_to_log(log_message)
