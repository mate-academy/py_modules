"""
module for log representation
"""
from payment import Payment, HourlyPaymentPerTask, FixedPaymentPerTask


class Log:
    """
    Log class represents information about task and worker
    which connected with each payment.
    """

    def __init__(self, *payments: Payment):
        self.payments = payments

    def __repr__(self) -> str:
        return f"<Log(payments:{self.payments})>"

    def confirm(self) -> dict:
        """
        Generate dict of items "worker name: task payment".
        :return: dict
        """
        task_payments = {}
        for payment in self.payments:
            if isinstance(payment, HourlyPaymentPerTask) \
                    and payment.payment_result() > 0:
                task_payments[payment.worker.name] = payment.payment_result()
            elif isinstance(payment, FixedPaymentPerTask) \
                    and payment.payment_result() > 0:
                task_payments[payment.worker.name] = payment.payment_result()
            else:
                return {}
        return task_payments

    def report(self):
        """
        Generate string report from confirm() method result.
        :return: str
        """
        return '\n'.join(f"{worker_name}\t${task_payment}"
                         for worker_name, task_payment
                         in self.confirm().items())
