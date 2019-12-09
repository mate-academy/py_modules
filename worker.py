"""worker module"""
import register_container


class Worker:
    """Worker has id, name and can approve task"""
    def __init__(self, worker_id, name):
        self.worker_id = worker_id
        self.name = name
        self.tasks = register_container.Register()

    def get_name(self):
        """get worker name"""
        return self.name

    def approve(self, log, task):
        """add task into register list"""
        self.tasks.add_task(self, task)
        log.confirm(self, task)

    def get_worker_tasks(self):
        """get all worker tasks"""
        return self.tasks

    def __hash__(self):
        return hash(self.name) ^ hash(self.worker_id)

    def __str__(self):
        return f"{self.name}, {self.worker_id}"
