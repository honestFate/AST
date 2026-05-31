import pytest
from task6_2 import DynamicArrayDeque

from task6 import Deque


@pytest.fixture
def make_deque():
    def _make_deque(values):
        deque = Deque()
        for v in values:
            deque.addTail(v)
        return deque
    return _make_deque


@pytest.fixture
def make_dyn_deque():
    def _make_dyn_deque(values):
        deque = DynamicArrayDeque()
        for v in values:
            deque.addTail(v)
        return deque
    return _make_dyn_deque


@pytest.fixture
def deque_to_list():
    def _to_list(deque):
        values = []
        while deque.size() > 0:
            values.append(deque.removeFront())
        return values
    return _to_list

