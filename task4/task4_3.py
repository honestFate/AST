import pytest


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
    assert stack.stack == make_stack(values)
    assert stack.tail_peek() == expected_val

@pytest.mark.parametrize("values, expected_stack, expected_val",[
    ([], [], None),
    ([1], [], 1),
    ([1, 2], [1], 2),
    ([1, 2, 3], [1, 2], 3),
    ([1, 2, 3, 4], [1, 2, 3], 4),
])
def test_pop(make_reverse_stack, values, expected_stack, expected_val):
    stack = make_reverse_stack(values)
    assert stack.pop() == expected_val
    assert stack.stack == expected_stack

@pytest.mark.parametrize("values, val, expected_stack",[
    ([], 1, [1]),
    ([1], 0, [1, 0]),
    ([1, 2], 1, [1, 2, 1]),
    ([1, 2, 3], 3, [1, 2, 3, 3]),
    ([1, 2, 3, 4], 5, [1, 2, 3, 4, 5]),
])
def test_push(make_reverse_stack, values, val, expected_stack):
    stack = make_reverse_stack(values)
    stack.push(val)
    assert stack.stack == expected_stack

@pytest.mark.parametrize("values, expected_val",[
    ([], None),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3),
    ([1, 2, 3, 4], 4),
])
def test_peek(make_reverse_stack, values, expected_val):
    stack = make_reverse_stack(values)
    assert stack.peek() == expected_val
    assert stack.stack == make_reverse_stack(values)
