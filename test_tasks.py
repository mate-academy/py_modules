import task
import worker
import log


def test_report():
    lg = log.Log()
    w1 = worker.Worker('Bill')
    w2 = worker.Worker('John')
    t1 = task.Task(35, 2)
    t2 = task.Task(15, 5, True)
    w1.complete_task(t1, lg)
    w2.complete_task(t2, lg)
    assert lg.report() == "Bill\t35.0$\nJohn\t75.0$"
