"""
module for fixed task representation
"""
from task import Task
from worker import Worker


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
