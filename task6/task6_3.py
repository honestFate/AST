import random

import pytest
from task6_2 import DynamicArrayDeque, is_balanced, is_palindrome

from task6 import Deque


@pytest.mark.parametrize("values, item, expected", [
    ([], 1, [1]),
    ([2], 1, [1, 2]),
    ([2, 3], 1, [1, 2, 3]),
    ([2, 3, 4], 1, [1, 2, 3, 4]),
])
def test_add_front(make_deque, deque_to_list, values, item, expected):
    deque = make_deque(values)
    size_before = deque.size()
    deque.addFront(item)
    assert deque.size() == size_before + 1
    assert deque_to_list(deque) == expected

@pytest.mark.parametrize("values, item, expected", [
    ([], 1, [1]),
    ([1], 2, [1, 2]),
    ([1, 2], 3, [1, 2, 3]),
    ([1, 2, 3], 4, [1, 2, 3, 4]),
])
def test_add_tail(make_deque, deque_to_list, values, item, expected):
    deque = make_deque(values)
    size_before = deque.size()
    deque.addTail(item)
    assert deque.size() == size_before + 1
    assert deque_to_list(deque) == expected

@pytest.mark.parametrize("values, expected_item, expected_rest", [
    ([], None, []),
    ([1], 1, []),
    ([1, 2], 1, [2]),
    ([1, 2, 3], 1, [2, 3]),
])
def test_remove_front(make_deque, deque_to_list, values, expected_item, expected_rest):
    deque = make_deque(values)
    size_before = deque.size()
    item = deque.removeFront()
    assert item == expected_item
    assert deque.size() == max(size_before - 1, 0)
    assert deque_to_list(deque) == expected_rest

@pytest.mark.parametrize("values, expected_item, expected_rest", [
    ([], None, []),
    ([1], 1, []),
    ([1, 2], 2, [1]),
    ([1, 2, 3], 3, [1, 2]),
])
def test_remove_tail(make_deque, deque_to_list, values, expected_item, expected_rest):
    deque = make_deque(values)
    size_before = deque.size()
    item = deque.removeTail()
    assert item == expected_item
    assert deque.size() == max(size_before - 1, 0)
    assert deque_to_list(deque) == expected_rest

@pytest.mark.parametrize("values, expected", [
    ([], 0),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3, 4, 5], 5),
])
def test_size(make_deque, values, expected):
    assert make_deque(values).size() == expected

def test_mixed_order(make_deque, deque_to_list):
    deque = make_deque([])
    deque.addTail(2)
    deque.addFront(1)
    deque.addTail(3)
    deque.addFront(0)
    assert deque_to_list(deque) == [0, 1, 2, 3]

@pytest.mark.parametrize("values, expected", [
    ([5], 5),
    ([3, 1, 2], 1),
    ([1, 2, 3], 1),
    ([3, 2, 1], 1),
    ([-1, -5, 3], -5),
    ([7, 7, 7], 7),
])
def test_min_after_add(make_deque, values, expected):
    assert make_deque(values).get_min() == expected

def test_min_empty():
    assert Deque().get_min() is None

def test_min_with_add_front():
    deque = Deque()
    for v in [3, 1, 2]:
        deque.addFront(v)
    assert deque.get_min() == 1

def test_min_updates_after_remove():
    deque = Deque()
    deque.addTail(5)
    deque.addFront(2)
    deque.addTail(8)
    deque.addFront(1)
    assert deque.get_min() == 1
    assert deque.removeFront() == 1
    assert deque.get_min() == 2
    assert deque.removeFront() == 2
    assert deque.get_min() == 5
    assert deque.removeTail() == 8
    assert deque.get_min() == 5

def test_min_random():
    deque = Deque()
    reference = []
    for _ in range(1000):
        op = random.randint(0, 3)
        value = random.randint(-100, 100)
        if op == 0:
            deque.addFront(value)
            reference.insert(0, value)
        elif op == 1:
            deque.addTail(value)
            reference.append(value)
        elif op == 2:
            expected = reference.pop(0) if reference else None
            assert deque.removeFront() == expected
        else:
            expected = reference.pop() if reference else None
            assert deque.removeTail() == expected
        assert deque.size() == len(reference)
        assert deque.get_min() == (min(reference) if reference else None)


def test_dyn_empty():
    deque = DynamicArrayDeque()
    assert deque.removeFront() is None
    assert deque.removeTail() is None
    assert deque.size() == 0

def test_dyn_fifo(make_dyn_deque, deque_to_list):
    deque = make_dyn_deque([1, 2, 3, 4, 5])
    assert deque_to_list(deque) == [1, 2, 3, 4, 5]

def test_dyn_front_grows_and_drains():
    deque = DynamicArrayDeque()
    for i in range(100):
        deque.addFront(i)
    for i in range(99, -1, -1):
        assert deque.removeFront() == i
    assert deque.size() == 0

def test_dyn_tail_grows_and_drains():
    deque = DynamicArrayDeque()
    for i in range(100):
        deque.addTail(i)
    for i in range(100):
        assert deque.removeFront() == i
    assert deque.size() == 0

@pytest.mark.parametrize("text, expected", [
    ("", True),
    ("a", True),
    ("abba", True),
    ("racecar", True),
    ("level", True),
    ("ab", False),
    ("abc", False),
    ("abca", False),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected

@pytest.mark.parametrize("expression, expected", [
    ("", True),
    ("()", True),
    ("()[]{}", True),
    ("([{}])", True),
    ("(())}{(", False),
    ("[]({})", True),
    ("(", False),
    (")(", False),
    ("([)]", False),
    ("(]", False),
])
def test_is_balanced(expression, expected):
    assert is_balanced(expression) == expected

