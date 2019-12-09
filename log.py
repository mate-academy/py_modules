"""
Realisation of the log of completed tasks.
Classes
-------
Log
"""

import linked_list


class Log:
    """
    Class for working with logs
    Attributes
    ----------
    Methods
    -------
    confirm()
    report()
    """
    def __init__(self):
        self._array = linked_list.List()

    def confirm(self, worker_name, task_name, task_payment):
        """insert record in linked list
        Attributes
        ----------
        worker_name - the name of the worker who completed the task
        task_name - the name of the completed task
        task_payment - payment for completed task
        """
        self._array.insert(worker_name, task_name, task_payment)

    def report(self):
        """return string with all records from linked list"""
        log = self._array.state()
        result = []
        for record in log:
            result.append(f"{record.worker_name()}\t${record.task_payment()}")
        return "\n".join(result)


if __name__ == "__main__":
    pass
