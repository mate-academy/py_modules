"""This script checks the operation of whole tasktracker"""
import tasks
import day_plan
import worker
import log


def test_tasks_creation():
    """Check if new tasks are properly created"""
    task_1 = tasks.Task("one", 20)
    task_2 = tasks.Task("two", 25)
    assert(task_1.get_rate()) == 20
    assert(task_2.get_name()) == "two"


def test_daily_plan_creation():
    """Check if tasks are added to the Daily Plan
    in respective order"""
    task_1 = tasks.Task("one", 20)
    task_2 = tasks.Task("two", 25)
    day_plan_obj = day_plan.DailyPlan()
    day_plan_obj.create_plan(task_1, task_2)
    assert(day_plan_obj.get_plan()) == [('one', 20), ('two', 25)]


def test_worker_creation():
    """Check if new workers are properly created"""
    worker_1 = worker.Worker("John")
    assert(worker_1.get_name()) == "John"


def test_tasks_assignment_from_daily_plan():
    """Check if tasks are properly assigned from Daily Plan to worker
    and if Daily Plan is properly updated"""
    task_1 = tasks.Task("one", 20)
    task_2 = tasks.Task("two", 25)
    day_plan_obj = day_plan.DailyPlan()
    day_plan_obj.create_plan(task_1, task_2)
    worker_1 = worker.Worker("John")
    worker_1.get_task_from_dp(day_plan_obj)
    assert(worker_1.get_current_task()) == ('two', 25)
    assert(day_plan_obj.get_plan()) == [('one', 20)]


def test_tasks_reporting():
    """Check if tasks are properly logged and reported"""
    logg = log.Log()
    task_1 = tasks.Task("one", 20)
    task_2 = tasks.Task("two", 70)
    day_plan_obj = day_plan.DailyPlan()
    day_plan_obj.create_plan(task_1, task_2)
    worker_1 = worker.Worker("John")
    worker_2 = worker.Worker("Mary")
    worker_2.get_task_from_dp(day_plan_obj)
    worker_2.log_task(logg, worker_2.get_current_task())
    worker_1.get_task_from_dp(day_plan_obj)
    worker_1.log_task(logg, worker_1.get_current_task(), 5)
    assert(logg.get_report()) == """Mary earned $70
John earned $100
"""
