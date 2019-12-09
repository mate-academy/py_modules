import hourlytask
import task
import worker
import log


def test_report_one():
    info = log.Log()
    worker_artem = worker.Worker("Artem")
    worker_alex = worker.Worker("Alex")
    worker_masha = worker.Worker("Masha")
    masha_fixet_task = task.Task("Task1", 300)
    fixet_task = task.Task("Task2", 100)
    hoyrly_task = hourlytask.HourlyTask("Task3", 200, 3)
    worker_masha.get_task(masha_fixet_task, info)
    worker_artem.get_task(fixet_task, info)
    worker_alex.get_task(hoyrly_task, info)
    assert info.report() == 'Masha\t$300\nArtem\t$100\nAlex\t$600'
