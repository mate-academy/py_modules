"""Tests for tasktracker"""
import task
import worker
import hourlytask
import log


def test_report_one():
    """test one: workers try to take not completed tasks"""
    log1 = log.Log()
    worker1 = worker.Worker("Dima")
    worker2 = worker.Worker("John")
    task1 = hourlytask.HourlyPaymentTask("Homework", 10, 3)
    task2 = task.Task("Take cup of tea", 5)
    worker1.take_task(task1, log1)
    worker2.take_task(task2, log1)
    assert log1.report() == 'Dima\t$30\nJohn\t$5'


def test_report_two():
    """test two: one of workers try to take completed task"""
    log1 = log.Log()
    worker1 = worker.Worker("Dima")
    worker2 = worker.Worker("John")
    task1 = hourlytask.HourlyPaymentTask("Homework", 10, 3)
    task2 = task.Task("Take cup of tea", 5)
    worker1.take_task(task1, log1)
    worker2.take_task(task2, log1)
    worker1.take_task(task1, log1)
    assert log1.report() == 'Dima\t$30\nJohn\t$5'


def test_report_three():
    """test three: one of workers try to take few not completed tasks"""
    log1 = log.Log()
    worker1 = worker.Worker("Dima")
    worker2 = worker.Worker("John")
    task1 = hourlytask.HourlyPaymentTask("Homework", 10, 3)
    task2 = task.Task("Take cup of tea", 5)
    task3 = task.Task("Web serfing", 25)
    worker1.take_task(task1, log1)
    worker2.take_task(task2, log1)
    worker1.take_task(task3, log1)
    assert log1.report() == 'Dima\t$55\nJohn\t$5'


def test_report_four():
    """test four: workers try to take not completed tasks"""
    log1 = log.Log()
    worker1 = worker.Worker("Dima")
    worker2 = worker.Worker("John")
    worker3 = worker.Worker("Bill")
    task1 = hourlytask.HourlyPaymentTask("Homework", 10, 3)
    task2 = task.Task("Take cup of tea", 5)
    task3 = task.Task("Web serfing", 25)
    worker1.take_task(task1, log1)
    worker2.take_task(task2, log1)
    worker3.take_task(task3, log1)
    assert log1.report() == 'Dima\t$30\nJohn\t$5\nBill\t$25'
