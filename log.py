"""docstring"""
import register_container


class Log:
    """log all tasks with workers"""
    def __init__(self):
        self.logs = register_container.Register()

    def confirm(self, worker, task):
        """confirm task"""
        task.worker = worker
        self.logs.add_task(worker, task)

    def report(self):
        """str representation"""
        return "\n".join(f"{task.get_name()},{worker.get_name()}:"
                         f"{task.get_sum_pay()}" for task, worker in self.logs)
