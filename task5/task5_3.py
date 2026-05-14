import pytest
from task5_2 import (
    QUEUE_CAPACITY,
    StackQueue,
    StaticArrayQueue,
    reverse_order,
    rotate_queue,
)

from task5 import Queue


@pytest.mark.parametrize("values, expected", [
    ([], 0),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3),
    ([1, 2, 3, 4, 5], 5),
])
def test_size(make_queue, values, expected):
    assert make_queue(values).size() == expected

@pytest.mark.parametrize("values, val, expected_queue", [
    ([], 1, [1]),
    ([1], 2, [1, 2]),
    ([1, 2], 3, [1, 2, 3]),
    ([1, 2, 3], 4, [1, 2, 3, 4]),
    ([1, 2, 3, 4], 5, [1, 2, 3, 4, 5]),
])
def test_enqueue(make_queue, values, val, expected_queue):
    queue = make_queue(values)
    queue.enqueue(val)
    assert queue.queue == expected_queue

@pytest.mark.parametrize("values, expected_queue, expected_val", [
    ([], [], None),
    ([1], [], 1),
    ([1, 2], [2], 1),
    ([4, 2, 3], [2, 3], 4),
    ([5, 2, 3, 4], [2, 3, 4], 5),
])
def test_dequeue(make_queue, values, expected_queue, expected_val):
    queue = make_queue(values)
    assert queue.dequeue() == expected_val
    assert queue.queue == expected_queue

def test_fifo_order(make_queue, queue_to_list):
    queue = make_queue([1, 2, 3, 4, 5])
    assert queue_to_list(queue) == [1, 2, 3, 4, 5]
    assert queue.size() == 0
    assert queue.dequeue() is None

@pytest.mark.parametrize("values, expected", [
    ([], 0),
    ([1], 1),
    ([1, 2, 3], 3),
    (list(range(10)), 10),
    (list(range(QUEUE_CAPACITY)), QUEUE_CAPACITY),
])
def test_static_size(make_static_queue, values, expected):
    assert make_static_queue(values).size() == expected

def test_static_dequeue_empty():
    queue = StaticArrayQueue()
    assert queue.dequeue() is None

def test_static_fifo_order(make_static_queue):
    queue = make_static_queue([1, 2, 3, 4, 5])
    assert [queue.dequeue() for _ in range(5)] == [1, 2, 3, 4, 5]
    assert queue.size() == 0
    assert queue.dequeue() is None

def test_static_overflow():
    queue = StaticArrayQueue()
    for i in range(QUEUE_CAPACITY):
        queue.enqueue(i)
    with pytest.raises(OverflowError):
        queue.enqueue(0)
    assert queue.size() == QUEUE_CAPACITY
    assert queue.dequeue() == 0

def test_static_cycle(queue_to_list):
    queue = StaticArrayQueue()
    for x in range(QUEUE_CAPACITY):
        queue.enqueue(x)
    for _ in range(3):
        queue.dequeue()
    for x in (-1, -2, -3):
        queue.enqueue(x)
    expected = list(range(3, QUEUE_CAPACITY)) + [-1, -2, -3]
    assert queue_to_list(queue) == expected

@pytest.mark.parametrize("values, expected", [
    ([], False),
    ([1], False),
    (list(range(QUEUE_CAPACITY - 1)), False),
    (list(range(QUEUE_CAPACITY)), True),
])
def test_static_is_full(make_static_queue, values, expected):
    assert make_static_queue(values)._is_full() == expected

@pytest.mark.parametrize("values, expected", [
    ([], 0),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 3),
    ([1, 2, 3, 4, 5], 5),
])
def test_stack_queue_size(make_stack_queue, values, expected):
    assert make_stack_queue(values).size() == expected

def test_stack_queue_dequeue_none():
    queue = StackQueue()
    assert queue.dequeue() is None

def test_stack_queue_fifo(make_stack_queue, queue_to_list):
    queue = make_stack_queue([1, 2, 3, 4, 5])
    assert queue_to_list(queue) == [1, 2, 3, 4, 5]
    assert queue.size() == 0
    assert queue.dequeue() is None

def test_stack_queue_alternating():
    queue = StackQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(3)
    assert queue.dequeue() == 2
    queue.enqueue(4)
    queue.enqueue(5)
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5
    assert queue.dequeue() is None

@pytest.mark.parametrize("values, n, expected", [
    ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5, 1]),
    ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
    ([1, 2, 3, 4, 5], 4, [5, 1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 7, [3, 4, 5, 1, 2]),
    ([1, 2, 3], 1, [2, 3, 1]),
    ([42], 5, [42]),
])
def test_rotate_queue(make_queue, queue_to_list, values, n, expected):
    queue = make_queue(values)
    rotate_queue(queue, n)
    assert queue_to_list(queue) == expected

def test_rotate_empty_queue():
    queue = Queue()
    rotate_queue(queue, 5)
    assert queue.size() == 0

@pytest.mark.parametrize("values, expected", [
    ([], []),
    ([1], [1]),
    ([1, 2], [2, 1]),
    ([1, 2, 3], [3, 2, 1]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
])
def test_reverse_order(make_queue, queue_to_list, values, expected):
    queue = make_queue(values)
    reverse_order(queue)
    assert queue_to_list(queue) == expected

def test_reverse_order_with_none_values(make_queue, queue_to_list):
    queue = make_queue([1, None, 2, None])
    reverse_order(queue)
    assert queue_to_list(queue) == [None, 2, None, 1]

