"""This script is a part of task py_modules
(being the tasktracker.py separated by classes)"""


class Task:
    """This class objects maintain and provide the requisites of the task"""
    def __init__(self, name: str, rate: int):
        """Initiate the task with name and rate"""
        self.name = name
        self.rate = rate

    def get_name(self):
        """Provide the name of the task"""
        return self.name

    def get_rate(self):
        """Provide the rate of the task"""
        return self.rate
