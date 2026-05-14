import pytest
from task5_2 import StackQueue, StaticArrayQueue

from task5 import Queue


@pytest.fixture
def make_queue():
    def _make_queue(values):
        queue = Queue()
        for v in values:
            queue.enqueue(v)
        return queue
    return _make_queue

@pytest.fixture
def make_static_queue():
    def _make_static_queue(values):
        queue = StaticArrayQueue()
        for v in values:
            queue.enqueue(v)
        return queue
    return _make_static_queue

@pytest.fixture
def make_stack_queue():
    def _make_stack_queue(values):
        queue = StackQueue()
        for v in values:
            queue.enqueue(v)
        return queue
    return _make_stack_queue

@pytest.fixture
def queue_to_list():
    def _queue_to_list(queue, n=0):
        values = []
        for _ in range(n if n > 0 else queue.size()):
            values.append(queue.dequeue())
        return values
    return _queue_to_list

