"""
Module to create a log that keeps track of
workers earnings.

Classes
-------
Log
"""


class Log:
    """
    Create report about all workers and their earning
    Attributes
    ----------
    database : dict  --  data base for all workers and earnings

    Methods
    -------
    report()
    """
    def __init__(self):
        self.database = {}

    def report(self):
        """Return report that contains workers names and earnings"""
        rep = ''
        for name, money in self.database.items():
            rep += f'{name}\t${money}\n'
        return rep

    def get_database(self):
        """Return database"""
        return self.database
