"""This script is a part of task py_modules
(being the tasktracker.py separated by classes)"""


class Log:
    """This class represents object that obtains inputs
    from class Worker objects and generates report
    based on those inputs and values from class Task"""

    def __init__(self):
        self.log_file = []

    def write_to_log(self, log_message):
        """Write the data reported by worker to the log"""
        self.log_file.append(log_message)

    def get_report(self):
        """Take all the tuples with workers' logs from the log file,
         calculate and report amount to be paid to worker. The same
         formulae used both for fixed payment tasks and for per hour tasks
         as by-default time input for fixed payment tasks is equal to 1"""
        report = ""
        for item in self.log_file:
            report += f"{item[0]} earned ${item[1][1] * item[2]}\n"
            # I know SoC principle is broken here (the same function
            # calculates and reports) but this approach seems to be logical
            # from OOP point of view as neither worker him/herself nor task
            # should be responsible for the payment
        return report
