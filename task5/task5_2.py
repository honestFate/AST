import ctypes

from task4.task4 import Stack

QUEUE_CAPACITY = 42

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
        self.queue = self._make_array(QUEUE_CAPACITY)
        self.start = CyclePointer(QUEUE_CAPACITY)
        self.end = CyclePointer(QUEUE_CAPACITY)
        self.len = 0

    def _is_full(self):
        return self.len == QUEUE_CAPACITY

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def enqueue(self, item):
        if self.size() == QUEUE_CAPACITY:
            raise OverflowError(f"QUEUE_CAPACITY of {QUEUE_CAPACITY} is full, " \
            "unable to add new items")
        self.queue[self.end.get()] = item
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
    while queue.size() > 0:
        stack.push(queue.dequeue())
    while stack.size() > 0:
        queue.enqueue(stack.pop())

"""
task: 5.1
name: queue (list)
enqueue: time O(1) амортизированно, memory O(1)
dequeue: time O(n), memory O(1)
size: time O(1), memory O(1)

task: 5.2
name: enqueue and dequeue complexity
enqueue O(1) амортизированно, так как используется list
как реализация очереди, append в конец происходит за O(1),
если не нужна реаллокация. dequeue в свою очередь за O(n),
так как удаляем из начала и нужно сдвинуть все элементы,
что находятся правее.

task: 5.3
name: rotate queue
time: O(n)
memory: O(1)

task: 5.4
name: queue (two stacks)
enqueue: time O(1), memory O(1)
dequeue: time O(1) амортизированно, memory O(1)

task: 5.5
name: reverse queue
time: O(n)
memory: O(n)

task: 5.6
name: queue (static array)
enqueue: time O(1), memory O(1)
dequeue: time O(1), memory O(1)
is_full: time O(1), memory O(1)
size: time O(1), memory O(1)
"""

