"""
tests module
"""
import log


def test_report_hourly():
    """

    :return:
    """
    work_one = log.MyLog("Bill", 'Task1')
    assert work_one.report() == "Please pay 50$ to Bill for Task1!"


def test_report_fixed():
    """

    :return:
    """
    work_two = log.MyLog("Ted", 'Task3')
    assert work_two.report() == "Please pay 500$ to Ted for Task3!"


def test_report_none():
    """

    :return:
    """
    work_three = log.MyLog("Tony", 'Task4')
    assert work_three.report() == "Worker or Task doesnt exists"
