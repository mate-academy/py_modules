import log
import task
import worker


def test_repo():
    bill = worker.Worker('Bill')
    john = worker.Worker('John')
    log_file = log.Log()
    fixed_task = task.Task('fixed')
    hourly_task = task.Task('hourly', time=2)
    log_file.confirm(bill, fixed_task)
    log_file.confirm(john, hourly_task)
    assert log_file.report() == """Bill\t$20
John\t$30"""
