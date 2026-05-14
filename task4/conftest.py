import pytest

from task4 import Stack


@pytest.fixture
def make_stack():
    def _make_stack(values):
        stack = Stack()
        for v in reversed(values):
            stack.push(v)
        return stack
    return _make_stack
