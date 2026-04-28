import pytest
from task2_2 import (
    linked_list_2_concat,
    linked_list_2_is_cycled,
    linked_list_2_reverse,
    linked_list_2_sort,
)

from task2 import LinkedList2, Node


def make_cycled_linked_list(values, cycle_to_id):
    linked_list = LinkedList2()
    for v in values:
        linked_list.add_in_tail(Node(v))
    if cycle_to_id is not None and linked_list.head is not None:
        node = linked_list.head
        i = 0
        while i < cycle_to_id:
            node = node.next
            i += 1
        linked_list.tail.next = node
    return linked_list

def check_head_and_tail(linked_list, expected):
    if len(expected) == 0:
        assert linked_list.head is None
        assert linked_list.tail is None
        return
    if len(expected) == 1:
        assert linked_list.head == linked_list.tail
    assert linked_list.head is not None
    assert linked_list.tail is not None
    assert linked_list.head.value == expected[0]
    assert linked_list.head.prev is None
    assert linked_list.tail.value == expected[-1]
    assert linked_list.tail.next is None
    backward = []
    node = linked_list.tail
    while node is not None:
        backward.append(node.value)
        node = node.prev
    assert backward == expected[::-1]

@pytest.mark.parametrize("values, param, expected", [
    ([1], 1, 1),
    ([0, 1], 1, 1),
    ([1, 0], 1, 1),
    ([-1, 0, 1], 1, 1),
    ([1, 2, 3, 4, 5], 3, 3),
    ([1, 2, 3, 4, 5], 5, 5),
    ([], 1, None),
    ([0], 1, None),
    ([0, 1], 2, None),
])
def test_find_first(make_linked_list_2, values, param, expected):
    linked_list = make_linked_list_2(values)
    result = linked_list.find(param)
    if result is None:
        assert result == expected
    else:
        assert result.value == expected

@pytest.mark.parametrize("values, param, expected", [
    ([1], 1, [1]),
    ([0, 1], 1, [1]),
    ([1, 0], 1, [1]),
    ([-1, 0, 1], 1, [1]),
    ([1, 2, 3, 4, 5], 3, [3]),
    ([1, 2, 3, 4, 5], 5, [5]),
    ([], 1, []),
    ([0], 1, []),
    ([0, 1], 2, []),
    ([1, 1], 1, [1, 1]),
    ([1, 1, 1], 1, [1, 1, 1]),
    ([-1, 0, -1], -1, [-1, -1]),
    ([3, 2, 3, 4, 3], 3, [3, 3, 3]),
    ([5, 1, 5, 2, 3, 5, 4, 5, 5], 5, [5, 5, 5, 5, 5])
])
def test_find_all(make_linked_list_2, values, param, expected):
    linked_list = make_linked_list_2(values)
    result = linked_list.find_all(param)
    assert len(result) == len(expected)
    for result_node, expected_value in zip(result, expected):
        assert result_node.value == expected_value

@pytest.mark.parametrize("values, param, expected", [
    ([], 1, []),
    ([1], 1, []),
    ([0], 1, [0]),
    ([0, 1], 1, [0]),
    ([1, 0], 1, [0]),
    ([0, 1], 2, [0, 1]),
    ([1, 1], 1, [1]),
    ([-1, 0, 1], 1, [-1, 0]),
    ([1, 2, 3, 3, 4], 3, [1, 2, 3, 4]),
    ([3, 2, 3, 4, 3], 3, [2, 3, 4, 3])
])
def test_delete_first(make_linked_list_2, linked_list_2_to_list, values, param,
                      expected):
    linked_list = make_linked_list_2(values)
    linked_list.delete(param)
    check_head_and_tail(linked_list, expected)
    assert linked_list_2_to_list(linked_list) == expected

@pytest.mark.parametrize("values, param, expected", [
    ([], 1, []),
    ([1], 1, []),
    ([0], 1, [0]),
    ([0, 1], 1, [0]),
    ([1, 0], 1, [0]),
    ([0, 1], 2, [0, 1]),
    ([1, 1], 1, []),
    ([1, 1, 1], 1, []),
    ([-1, 0, 1], 1, [-1, 0]),
    ([1, 2, 3, 3, 4], 3, [1, 2, 4]),
    ([3, 2, 3, 4, 3], 3, [2, 4])
])
def test_delete_all(make_linked_list_2, linked_list_2_to_list, values, param, expected):
    linked_list = make_linked_list_2(values)
    linked_list.delete(param, all=True)
    check_head_and_tail(linked_list, expected)
    assert linked_list_2_to_list(linked_list) == expected

@pytest.mark.parametrize("values, insert_pos, param, expected", [
    ([], None, 0, [0]),
    ([1], None, 0, [1, 0]),
    ([1], 0, 0, [1, 0]),
    ([0, 1], None, 2, [0, 1, 2]),
    ([0, 1], 0, 2, [0, 2, 1]),
    ([0, 1], 1, 2, [0, 1, 2]),
    ([-1, 0, 1], 2, 2, [-1, 0, 1, 2]),
    ([1, 2, 3, 4, 5], 3, 0, [1, 2, 3, 4, 0, 5]),
    ([1, 2, 3, 4, 5], 4, 0, [1, 2, 3, 4, 5, 0]),
    ([1, 2, 3, 4, 5], None, 0, [1, 2, 3, 4, 5, 0])
])
def test_insert(make_linked_list_2, linked_list_2_to_list, get_node_by_id, values,
                insert_pos, param, expected):
    linked_list = make_linked_list_2(values)
    if insert_pos is None:
        linked_list.insert(None, Node(param))
    else:
        linked_list.insert(get_node_by_id(linked_list, insert_pos), Node(param))
    check_head_and_tail(linked_list, expected)
    assert linked_list_2_to_list(linked_list) == expected

@pytest.mark.parametrize("values, param, expected", [
    ([], 0, [0]),
    ([1], 0, [0, 1]),
    ([0], 1, [1, 0]),
    ([0, 1], 2, [2, 0, 1]),
    ([-1, 0, 1], 2, [2, -1, 0, 1]),
    ([1, 2, 3, 4, 5], 0, [0, 1, 2, 3, 4, 5])
])
def test_add_in_head(make_linked_list_2, linked_list_2_to_list, values,
                     param, expected):
    linked_list = make_linked_list_2(values)
    linked_list.add_in_head(Node(param))
    check_head_and_tail(linked_list, expected)
    assert linked_list_2_to_list(linked_list) == expected

@pytest.mark.parametrize("values, param, expected", [
    ([], 0, [0]),
    ([1], 0, [1, 0]),
    ([0], 1, [0, 1]),
    ([0, 1], 2, [0, 1, 2]),
    ([-1, 0, 1], 2, [-1, 0, 1, 2]),
    ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5, 0])
])
def test_add_in_tail(make_linked_list_2, linked_list_2_to_list, values,
                     param, expected):
    linked_list = make_linked_list_2(values)
    linked_list.add_in_tail(Node(param))
    check_head_and_tail(linked_list, expected)
    assert linked_list_2_to_list(linked_list) == expected

@pytest.mark.parametrize("values, expected", [
    ([], []),
    ([1], []),
    ([0, 1], []),
    ([0, 1, 2], []),
    ([1, 2, 3, 4, 5, 6, 1], [])
])
def test_clean(make_linked_list_2, linked_list_2_to_list, values, expected):
    linked_list = make_linked_list_2(values)
    linked_list.clean()
    check_head_and_tail(linked_list, expected)
    assert linked_list_2_to_list(linked_list) == expected

@pytest.mark.parametrize("values, expected", [
    ([], 0),
    ([1], 1),
    ([100], 1),
    ([0, 1], 2),
    ([0, 1, 2], 3),
    ([1, 2, 3, 4, 5, 6, 1], 7)
])
def test_len(make_linked_list_2, values, expected):
    linked_list = make_linked_list_2(values)
    assert linked_list.len() == expected

@pytest.mark.parametrize("values, expected", [
    ([], []),
    ([1], [1]),
    ([100], [100]),
    ([0, 1], [1, 0]),
    ([1, 0], [0, 1]),
    ([0, 1, 2], [2, 1, 0]),
    ([2, 1, 0], [0, 1, 2]),
    ([0, 1, 2, 3], [3, 2, 1, 0]),
    ([1, 2, 3, 4, 5, 6, 1], [1, 6, 5, 4, 3, 2, 1]),
    ([1, 1, 1, 2, 3, 1, 1], [1, 1, 3, 2, 1, 1, 1])
])
def test_reverse(make_linked_list_2, linked_list_2_to_list, values, expected):
    linked_list = make_linked_list_2(values)
    linked_list_2_reverse(linked_list)
    check_head_and_tail(linked_list, expected)
    assert linked_list_2_to_list(linked_list) == expected

@pytest.mark.parametrize("values, cycle_to, expected", [
    ([], None, False),
    ([1], None, False),
    ([1], 0, True),
    ([1, 2], None, False),
    ([1, 2], 0, True),
    ([1, 2], 1, True),
    ([1, 2, 3], None, False),
    ([1, 2, 3], 0, True),
    ([1, 2, 3], 1, True),
    ([1, 2, 3], 2, True),
    ([1, 2, 3, 4, 5], None, False),
    ([1, 2, 3, 4, 5], 0, True),
    ([1, 2, 3, 4, 5], 2, True),
    ([1, 2, 3, 4, 5], 4, True),
    ([1, 2, 3, 4, 5, 6, 7, 8], None, False),
    ([1, 2, 3, 4, 5, 6, 7, 8], 4, True)
])
def test_is_cycled(values, cycle_to, expected):
    linked_list = make_cycled_linked_list(values, cycle_to)
    assert linked_list_2_is_cycled(linked_list) == expected

@pytest.mark.parametrize("values, expected", [
    ([], []),
    ([1], [1]),
    ([100], [100]),
    ([0, 1], [0, 1]),
    ([1, 0], [0, 1]),
    ([0, 1, 2], [0, 1, 2]),
    ([2, 1, 0], [0, 1, 2]),
    ([1, 2, 0], [0, 1, 2]),
    ([-1, 2, 0], [-1, 0, 2]),
    ([3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 1, 2, 3, 4, 5, 5, 6, 9]),
    ([1, 1, 1, 1], [1, 1, 1, 1])
])
def test_sort(make_linked_list_2, linked_list_2_to_list, values, expected):
    linked_list = make_linked_list_2(values)
    result = linked_list_2_sort(linked_list)
    check_head_and_tail(result, expected)
    assert linked_list_2_to_list(result) == expected

@pytest.mark.parametrize("values_1, values_2, expected", [
    ([], [], []),
    ([1], [], [1]),
    ([], [1], [1]),
    ([1], [1], [1, 1]),
    ([0], [1], [0, 1]),
    ([1], [0], [0, 1]),
    ([4, 3, 1], [5, 2], [1, 2, 3, 4, 5]),
    ([4, 3, 1], [], [1, 3, 4]),
    ([-1, -2], [1], [-2, -1, 1]),
    ([1, 3], [2, 4], [1, 2, 3, 4]),
    ([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3])
])
def test_concat(make_linked_list_2, linked_list_2_to_list, values_1, values_2,
                expected):
    linked_list_1 = make_linked_list_2(values_1)
    linked_list_2 = make_linked_list_2(values_2)
    result = linked_list_2_concat(linked_list_1, linked_list_2)
    check_head_and_tail(result, expected)
    assert linked_list_2_to_list(result) == expected

