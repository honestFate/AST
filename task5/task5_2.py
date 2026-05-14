import ctypes

from task4.task4 import Stack

APPEND_MODE = 0
REMOVE_MODE = 1
QUEQUE_CAPACITY = 42

class CyclePointer:
    def __init__(self, limit):
        self.pointer = 0
        self.limit = limit

    def shift(self):
        self.pointer = 0 if self.pointer + 1 == self.limit else self.pointer + 1

    def get(self):
        return self.pointer

class StaticArrayQueue:
    def __init__(self):
        self.queue = self._make_array(QUEQUE_CAPACITY)
        self.start = CyclePointer(QUEQUE_CAPACITY)
        self.end = CyclePointer(QUEQUE_CAPACITY)

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def enqueue(self, item):
        if self.size() == QUEQUE_CAPACITY:
            raise OverflowError("QUEQUE_CAPACITY of {QUEQUE_CAPACITY} is full, " \
            "unable to add new items")
        self.end.shift()
        self.queue[self.end] = item

    def dequeue(self):
        if self.size() == 0:
            return None
        temp = self.queue[self.start.get()]
        self.start.shift()
        return temp

    def size(self):
        return QUEQUE_CAPACITY - self.start.get() + self.end.get() if self.start.get() > self.end.get() else self.end.get() - self.start.get()


class StackQueue:
    def __init__(self):
        self.append_queue = Stack()
        self.remove_queue = Stack()
        self.mode = APPEND_MODE

    def _change_mode(self, new_mode):
        if self.mode == new_mode:
            return
        if not self.append_queue.size() and not self.remove_queue.size():
            return
        self.mode = new_mode
        if new_mode == APPEND_MODE:
            q1, q2 = self.remove_queue, self.append_queue
        else:
            q1, q2 = self.append_queue, self.remove_queue
        while q1.peek() is not None:
            q2.push(q1.pop())

    def enqueue(self, item):
        self._change_mode()
        self.append_queue.push(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        self._change_mode()
        return self.remove_queue.pop()

    def size(self):
        return max(self.append_queue.size(), self.remove_queue.size())


def rotate_queue(queue, n):
    if queue.size() == 0:
        raise ValueError("Unable to rotate empty queue")
    for i in range(n):
        queue.enqueue(queue.dequeue())

def reverse_order(queue):
    rotate_queue(queue, queue.size())
