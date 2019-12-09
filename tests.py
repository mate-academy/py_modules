"""
tests module
"""
from log import Log


def test_report_hourly():
    """

    :return:
    """
    work_one = Log("Bill", 'Task1')
    assert work_one.report() == "Please pay 50$ to Bill for Task1!"


def test_report_fixed():
    """

    :return:
    """
    work_two = Log("Ted", 'Task3')
    assert work_two.report() == "Please pay 500$ to Ted for Task3!"


def test_report_none():
    """

    :return:
    """
    work_three = Log("Tony", 'Task4')
    assert work_three.report() == "Worker or Task doesnt exists"
