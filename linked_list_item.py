"""Item for linked list"""


class Item:
    """Item realisation"""
    def __init__(self, worker_name, task_name, task_payment):
        self._worker_name = worker_name
        self._task_name = task_name
        self._task_payment = task_payment
        self.next = None
        self.previous = None

    def __repr__(self):
        return self._worker_name

    def worker_name(self):
        """return worker name"""
        return self._worker_name

    def task_name(self):
        """return task name"""
        return self._task_name

    def task_payment(self):
        """return task payment"""
        return self._task_payment


if __name__ == "__main__":
    pass
