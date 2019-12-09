"""
worker module
"""


class Worker:
    """
    Worker objects
    We can update workers list
    """
    _workers = ['Bill', 'John', 'Ted']

    def worker_available(self):
        """
        Return workers list
        :return:
        """
        return self._workers

    def add_worker(self):
        """
        Add new worker
        :return:
        """
        new_worker = None
        self._workers += new_worker
        return self._workers


if __name__ == '__main__':
    pass
