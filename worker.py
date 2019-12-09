"""Module class Worker"""


class Worker:
    """Class Worker accepts one argument - name"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """Get name"""
        return self.name

    def set_name(self, name):
        """Set name"""
        self.name = name
