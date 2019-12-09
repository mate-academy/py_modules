"""hourly rate representation"""
import tasks


class HTask(tasks.Task):
    """hourly rate task"""
    def __init__(self, id_task, name, sum_pay, hours):
        super().__init__(id_task, name)
        self.sum_pay = sum_pay
        self.hours = hours

    def get_sum_pay(self):
        """return sum pay: hours * sum pay"""
        return self.hours * self.sum_pay
