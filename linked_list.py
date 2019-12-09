"""linked list realisation"""
from linked_list_item import Item


class List:
    """item list realisation"""
    def __init__(self):
        self.head = None

    def state(self):
        """
        :return: items list in str format
        """
        result = []
        if self.head is not None:
            current = self.head
            result = [current]
            while current.previous is not None:
                current = current.previous
                result.append(current)
            return result
        return result

    def insert(self, worker_name, task_name, task_payment):
        """
        Insert item in list
        :return: None
        """
        if self.head is None:
            self.head = Item(worker_name, task_name, task_payment)
        else:
            new = Item(worker_name, task_name, task_payment)
            new.previous = self.head
            self.head.next = self.head = new


    def delete(self):
        """
        Delete item from list
        :return: deleted item
        """
        if self.head is not None:
            for_del = self.head
            self.head = self.head.previous
            self.head.next = None
            return for_del
        raise IndexError
