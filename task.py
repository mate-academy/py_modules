"""
module for task representation
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
