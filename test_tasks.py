"""tests module"""
import worker
import log
import hourly_rate_task
import fix_price_task


def test_report():
    """tested"""
    worker1 = worker.Worker(1, "bill")
    worker2 = worker.Worker(2, "tom")

    task1 = fix_price_task.FTask(1, "task1", 34)
    task2 = fix_price_task.FTask(2, "task2", 10)
    task3 = hourly_rate_task.HTask(3, "task3", 5, 10)

    test_log = log.Log()

    worker1.approve(test_log, task2)
    worker2.approve(test_log, task1)
    worker2.approve(test_log, task3)
    assert test_log.report() == "task3,tom:50\n" \
                                "task1,tom:34\n" \
                                "task2,bill:10"
