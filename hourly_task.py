"""
module for hourly task representation
"""
from task import Task
from worker import Worker


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
