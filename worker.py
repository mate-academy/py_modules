"""
module for worker representation
"""


class Worker:
    """
    Class represents worker.
    """

    def __init__(self, name: str, hourly_rate: int, presence_at_work: bool):
        self.name = name
        self.hourly_rate = hourly_rate
        self.working_hours_per_day = 8
        self.presence_at_work = presence_at_work

    def __str__(self) -> str:
        return f"Worker(name:{self.name}, hourly_rate:{self.hourly_rate}, " \
               f"working_hours_per_day:{self.working_hours_per_day}," \
               f"presence_at_work:{self.presence_at_work})"

    def __repr__(self) -> str:
        return f"<(name:{self.name}, hourly_rate:{self.hourly_rate}, " \
               f"working_hours_per_day:{self.working_hours_per_day}," \
               f"presence_at_work:{self.presence_at_work})>"
