class Worker:
    '''
    Worker class
    '''
    def __init__(self, name):
        self.name = name

    def get_task(self, task, log):
        '''
        Worker confirm task in log
        '''
        log.confirm(self, task)

    def get_name(self):
        '''
        return name
        '''
        return self.name