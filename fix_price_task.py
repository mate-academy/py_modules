"""task object"""
import tasks


class FTask(tasks.Task):
    """fix price task"""
    def __init__(self, id_task, name, sum_pay):
        super().__init__(id_task, name)
        self.sum_pay = sum_pay

    def get_sum_pay(self):
        """return fix price sum"""
        return self.sum_pay
