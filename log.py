'''
Module log
'''


class Log:
    '''
    Log
    '''
    def __init__(self):
        self.info_log = {}

    def confirm(self, worker, task):
        '''
        Add worker and salary to log
        '''
        self.info_log[worker.name] = task.get_payment()

    def report(self):
        '''
        :return info
        '''
        return '\n'.join(f"{name}\t${payment}" for name, payment in self.info_log.items())
