"""
Module to test following modules:
task, worker, log
"""


import task
import worker
import log


def test_report():
    """Testing function"""
    worker_1 = worker.Worker('Bill')
    worker_2 = worker.Worker('John')
    task_1 = task.Task('fixed')
    task_2 = task.Task('hourly', hours=3)
    task_3 = task.Task()
    total_log = log.Log()
    worker_1.confirm(task_1, total_log)
    worker_2.confirm(task_2, total_log)
    worker_2.confirm(task_3, total_log)
    total_log.report()
    return """Bill\t$100
John\t$130"""
