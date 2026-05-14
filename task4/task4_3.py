import pytest

from .task4 import Stack
from .task4_2 import evaluate_postfix, is_balanced, is_balanced_advanced


@pytest.mark.parametrize("values, expected",[
    ([], 0),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3),
    ([1, 2, 3, 4], 4),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16),
])
def test_size(make_stack, values, expected):
    assert make_stack(values).size() == expected

@pytest.mark.parametrize("values, expected_stack, expected_val",[
    ([], [], None),
    ([1], [], 1),
    ([1, 2], [1], 2),
    ([1, 2, 3], [1, 2], 3),
    ([1, 2, 3, 4], [1, 2, 3], 4),
])
def test_tail_pop(make_stack, values, expected_stack, expected_val):
    stack = make_stack(values)
    val = stack.tail_pop()
    assert stack.stack == expected_stack
    assert val == expected_val

@pytest.mark.parametrize("values, val, expected_stack",[
    ([], 1, [1]),
    ([1], 0, [1, 0]),
    ([1, 2], 1, [1, 2, 1]),
    ([1, 2, 3], 3, [1, 2, 3, 3]),
    ([1, 2, 3, 4], 5, [1, 2, 3, 4, 5]),
])
def test_tail_push(make_stack, values, val, expected_stack):
    stack = make_stack(values)
    stack.tail_push(val)
    assert stack.stack == expected_stack

@pytest.mark.parametrize("values, expected_val",[
    ([], None),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3),
    ([1, 2, 3, 4], 4),
])
def test_tail_peek(make_stack, values, expected_val):
    stack = make_stack(values)
    assert stack.tail_peek() == expected_val
    assert stack.stack == make_stack(values).stack

@pytest.mark.parametrize("values, expected_stack, expected_val",[
    ([], [], None),
    ([1], [], 1),
    ([1, 2], [2], 1),
    ([1, 2, 3], [2, 3], 1),
    ([1, 2, 3, 4], [2, 3, 4], 1),
])
def test_pop(make_stack, values, expected_stack, expected_val):
    stack = make_stack(values)
    assert stack.pop() == expected_val
    assert stack.stack == expected_stack

@pytest.mark.parametrize("values, val, expected_stack",[
    ([], 1, [1]),
    ([1], 0, [0, 1]),
    ([1, 2], 1, [1, 1, 2]),
    ([1, 2, 3], 3, [3, 1, 2, 3]),
    ([1, 2, 3, 4], 5, [5, 1, 2, 3, 4]),
])
def test_push(make_stack, values, val, expected_stack):
    stack = make_stack(values)
    stack.push(val)
    assert stack.stack == expected_stack

@pytest.mark.parametrize("values, expected_val",[
    ([], None),
    ([1], 1),
    ([1, 2], 1),
    ([4, 2, 3], 4),
    ([5, 2, 3, 4], 5),
])
def test_peek(make_stack, values, expected_val):
    stack = make_stack(values)
    assert stack.peek() == expected_val
    assert stack.stack == make_stack(values).stack

@pytest.mark.parametrize("line, expected_val",[
    ("(()((())()))", True),
    ("(()()(()", False),
    ("())(", False),
    ("))((", False),
    ("((())", False),
    ("()()()", True),
    ("()", True),
    ("((())())", True),
    ("(()()())", True),
])
def test_is_balanced(line, expected_val):
    assert is_balanced(line) == expected_val

@pytest.mark.parametrize("line, expected_val",[
    ("[{(()((({}))()))}]", True),
    ("(()([])(()", False),
    ("{())(}", False),
    ("[]{}))((", False),
    ("((()){}", False),
    ("()()()[]", True),
    ("()[]{}", True),
    ("[((())())]", True),
    ("(()([])({}))", True),
])
def test_is_balanced_advanced(line, expected_val):
    assert is_balanced_advanced(line) == expected_val

@pytest.mark.parametrize("values, expected", [
    ([], None),
    ([5], 5),
    ([3, 1], 1),
    ([1, 3], 1),
    ([5, 4, 3, 2, 1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([3, 1, 4, 1, 5, 9, 2, 6], 1),
    ([-1, -5, 3], -5),
    ([7, 7, 7], 7),
])
def test_min(make_stack, values, expected):
    assert make_stack(values).get_min() == expected


def test_min_updates_after_pop():
    stack = Stack()
    for v in [3, 1, 4, 1, 5]:
        stack.push(v)
    assert stack.get_min() == 1
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.get_min() == 1
    stack.pop()
    assert stack.get_min() == 3


@pytest.mark.parametrize("values, expected", [
    ([], None),
    ([5], 5.0),
    ([2, 4], 3.0),
    ([1, 2, 3], 2.0),
    ([10, 20, 30, 40], 25.0),
    ([-1, 1], 0.0),
    ([100], 100.0),
])
def test_mean(make_stack, values, expected):
    assert make_stack(values).get_mean() == expected


def test_mean_updates_after_pop():
    stack = Stack()
    for v in [2, 4, 6]:
        stack.push(v)
    assert stack.get_mean() == 4.0
    stack.pop()
    assert stack.get_mean() == 3.0
    stack.pop()
    assert stack.get_mean() == 2.0


@pytest.mark.parametrize("expression, expected", [
    ("1 2 + =", 3),
    ("1 2 + 3 * =", 9),
    ("8 2 + 5 * 9 + =", 59),
    ("2 3 4 * + =", 14),
    ("5 =", 5),
    ("2 3 * 4 5 * + =", 26),
    ("1 2 3 4 + + + =", 10),
    ("10 20 + 30 + 40 + =", 100),
])
def test_evaluate_postfix(expression, expected):
    assert evaluate_postfix(expression) == expected

