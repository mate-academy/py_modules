import worker
import log
import hourlyRateTask
import fixPriceTask


def test_report():
    w1 = worker.Worker(1, "bill")
    w2 = worker.Worker(2, "tom")

    t1 = fixPriceTask.FTask(1, "task1", 34)
    t2 = fixPriceTask.FTask(2, "task2", 10)
    t3 = hourlyRateTask.HTask(3, "task3", 5, 10)

    test_log = log.Log()

    w1.approve(test_log, t2)
    w2.approve(test_log, t1)
    w2.approve(test_log, t3)
    assert test_log.report() == "task3,tom: 50\n" \
                                "task1,tom: 34\n" \
                                "task2,bill: 10"
