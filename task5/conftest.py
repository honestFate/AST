import pytest

from task5 import Queue


@pytest.fixture
def make_queue():
    def _make_queue(values):
        queue = Queue()
        for v in values:
            queue.enqueue(v)
        return queue
    return _make_queue
