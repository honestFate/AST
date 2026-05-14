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
        self.len = 0

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def enqueue(self, item):
        if self.size() == QUEQUE_CAPACITY:
            raise OverflowError("QUEQUE_CAPACITY of {QUEQUE_CAPACITY} is full, " \
            "unable to add new items")
        self.queue[self.end] = item
        self.end.shift()
        self.len += 1

    def dequeue(self):
        if self.size() == 0:
            return None
        temp = self.queue[self.start.get()]
        self.start.shift()
        self.len -= 1
        return temp

    def size(self):
        return self.len


class StackQueue:
    def __init__(self):
        self.append_queue = Stack()
        self.remove_queue = Stack()
        self.mode = APPEND_MODE

    def enqueue(self, item):
        self.append_queue.push(item)

    def dequeue(self):
        if self.remove_queue.size() == 0:
            if self.append_queue.size() == 0:
                return None
            while self.append_queue.size() > 0:
                self.remove_queue.push(self.append_queue.pop())
        return self.remove_queue.pop()

    def size(self):
        return self.append_queue.size() + self.remove_queue.size()


def rotate_queue(queue, n):
    if queue.size() == 0:
        return
    for i in range(n % queue.size()):
        queue.enqueue(queue.dequeue())

def reverse_order(queue):
    if queue.size() == 0:
        return
    stack = Stack()
    while queue.peek() is not None:
        stack.push(queue.dequeue())
    while stack.peek() is not None:
        queue.push(stack.pop())
