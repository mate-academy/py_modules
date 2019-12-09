import worker
import paymentperhour
import fixedpayment
import log


def test_report():
    worker1 = worker.Worker("Bill")
    worker2 = worker.Worker("John")
    mylog = log.Log()
    task_fixed = fixedpayment.FixedPayment("build home", 20)
    task_per_h = paymentperhour.PaymentPerHour("do nothing", 15, 2)
    worker1.take_task(task_fixed)
    worker2.take_task(task_per_h)
    worker2.confirm(task_per_h, mylog)
    worker1.confirm(task_fixed, mylog)
    assert mylog.report() == """Bill\t$20
John\t$30"""
