"""Two kinds of tasks: fixed payment task and hourly payment task.
 Any task can be assigned to a worker.
  The worker has a name and can confirm task completion to the log.
 The log should be able to produce reports
  with worker's names and payment for completed tasks."""


class Task:
    """task has id, name, sum pay and worker"""
    def __init__(self, id_task, name):
        self.id_task = id_task
        self.name = name
        self.worker = None

    def __hash__(self):
        return hash(self.worker) ^ hash(self.id_task)

    def __str__(self):
        return f"{self.name}: {self.worker.get_name()}"

    def get_name(self):
        """return task name"""
        return self.name

    def get_worker(self):
        """return worker task"""
        return self.worker
