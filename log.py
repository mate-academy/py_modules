class Log:
    '''
    Log
    '''
    def __init__(self):
        pass
        self.info_log = {}

    def confirm(self, worker, task):
        '''
        Add worker and salary to log
        '''
        self.info_log[worker.name] = task.get_payment()

    def report(self):
        return '\n'.join(f"{name}\t${payment}" for name, payment in self.info_log.items())