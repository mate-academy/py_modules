class Task:
    '''
    Parent class for task
    '''
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment

    def get_payment(self):
        '''
        Retyrn salary for task
        '''
        return self.payment

    def get_name(self):
        '''
        :return name of task
        '''
        return self.name