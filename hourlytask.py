import task


class HourlyTask(task.Task):
    '''
    Class for hoyrly class
    '''
    def __init__(self, task_name, payment, work_time):
        super().__init__(task_name, payment)
        self.work_time = work_time

    def get_payment(self):
        '''
        Reyrn salary for task
        '''
        return super().get_payment() * self.work_time
