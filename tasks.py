"""
module for tasks representation
"""
from worker import Worker


class Task:
    """
    Parent class that represents task parameters which connected
    with each worker.
    """

    def __init__(self, worker: Worker, estimated_time: int, completed: bool):
        self.worker = worker
        self.title = ""
        self.estimated_hours = estimated_time
        self.completed = completed

    def __str__(self) -> str:
        return f"Task(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})"

    def __repr__(self) -> str:
        return f"<T(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})>"


class HourlyTask(Task):
    """
    Child class that inherit from Task and represents hourly
    task parameters which connected with each worker.
    """

    def __init__(self, worker: Worker, estimated_time: int,
                 completed: bool, total_task_hours: int):
        super().__init__(worker, estimated_time, completed)
        self.total_task_hours = total_task_hours

    def __str__(self) -> str:
        return f"HourlyTask(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})" \
               f"total_task_hours:{self.total_task_hours}"

    def __repr__(self) -> str:
        return f"HT<(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})" \
               f"total_task_hours:{self.total_task_hours}>"


class FixedTask(Task):
    """
    Child class that inherit from Task and represents fixed
    task parameters which connected with each worker.
    """

    def __init__(self, worker: Worker, total_task_payment,
                 completed: bool, estimated_time: int = 0):
        super().__init__(worker, estimated_time, completed)
        self.total_task_payment = total_task_payment

    def __str__(self) -> str:
        return f"FixedTask(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})" \
               f"total_task_payment:{self.total_task_payment}"

    def __repr__(self) -> str:
        return f"FT<(worker:{self.worker}, title:{self.title}, " \
               f"estimated_time:{self.estimated_hours}," \
               f"completed:{self.completed})" \
               f"total_task_payment:{self.total_task_payment}>"
