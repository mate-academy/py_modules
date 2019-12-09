from log import MyLog
from payment import HourlyPaymentPerTask, FixedPaymentPerTask
from tasks import HourlyTask, FixedTask
from worker import Worker


def test_report():
    # Data initialization
    w1 = Worker("Bill", 5, True)
    w2 = Worker("John", 3, True)
    t1 = HourlyTask(w1, 4, True, 4)
    t2 = FixedTask(w2, 30, True)
    p1 = HourlyPaymentPerTask(w1, t1)
    p2 = FixedPaymentPerTask(w2, t2)
    logger = MyLog(p1, p2)
    assert logger.report() == """Bill\t$20
John\t$30"""
