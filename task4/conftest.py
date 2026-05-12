from task4 import Stack
import pytest

@pytest.fixture
def make_stack():
    def _make_stack(values):
        stack = Stack()
        for v in values:
            stack.push(v)
        return stack
    return _make_stack

@pytest.fixture
def make_reverse_stack():
    def _make_reverse_stack(values):
        stack = Stack()
        if not values:
            return stack
        values.reverse()
        for v in values:
            stack.push(v)
        return stack
    return _make_reverse_stack
