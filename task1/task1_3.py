import pytest
from task1_2 import linked_list_sum

from task1 import Node


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
    assert linked_list.tail.value == expected[-1]
    assert linked_list.tail.next is None

@pytest.mark.parametrize("values, param, expected", [
    ([0], 1, [0]),
    ([1], 1, []),
    ([0, 1], 1, [0]),
    ([1, 0], 1, [0]),
    ([1, 1, 1], 1, [1, 1]),
    ([1, 0, 1], 1, [0, 1]),
    ([2, 1, 0, 1, 1, 0, 1, 2], 1, [2, 0, 1, 1, 0, 1, 2]),
    ([2, 1, 0, 1, 1, 0, 1, 2], 2, [1, 0, 1, 1, 0, 1, 2])
])
def test_delete_single(make_linked_list, linked_list_to_list, values, param, expected):
    linked_list = make_linked_list(values)
    linked_list.delete(param)
    check_head_and_tail(linked_list, expected)
    assert linked_list_to_list(linked_list) == expected

@pytest.mark.parametrize("values, param, expected", [
    ([0], 1, [0]),
    ([1], 1, []),
    ([0, 1], 1, [0]),
    ([1, 0], 1, [0]),
    ([1, 1, 1], 1, []),
    ([1, 0, 1], 1, [0]),
    ([2, 1, 0, 1, 1, 0, 1, 2], 1, [2, 0, 0, 2]),
    ([2, 1, 0, 1, 1, 0, 1, 2], 2, [1, 0, 1, 1, 0, 1])
])
def test_delete_all(make_linked_list, linked_list_to_list, values, param, expected):
    linked_list = make_linked_list(values)
    linked_list.delete(param, all=True)
    check_head_and_tail(linked_list, expected)
    assert linked_list_to_list(linked_list) == expected

@pytest.mark.parametrize("values, expected", [
    ([0], []),
    ([1], []),
    ([0, 1], []),
    ([1, 0], []),
    ([1, 1, 1], []),
    ([1, 0, 1], [])
])
def test_clean(make_linked_list, linked_list_to_list, values, expected):
    linked_list = make_linked_list(values)
    linked_list.clean()
    check_head_and_tail(linked_list, expected)
    assert linked_list_to_list(linked_list) == expected

@pytest.mark.parametrize("values, param, expected", [
    ([0], 1, []),
    ([1], 1, [1]),
    ([0, 1], 1, [1]),
    ([1, 0], 1, [1]),
    ([1, 1, 1], 1, [1, 1, 1]),
    ([1, 0, 1], 1, [1, 1]),
    ([2, 1, 0, 1, 1, 0, 1, 2], 2, [2, 2]),
    ([2, 1, 0, 1, 1, 0, 1, 2], 1, [1, 1, 1, 1])
])
def test_find_all(make_linked_list, values, param, expected):
    linked_list = make_linked_list(values)
    for result_node, expected_node in zip(linked_list.find_all(param), expected):
        assert result_node.value == expected_node

@pytest.mark.parametrize("values, expected", [
    ([], 0),
    ([0], 1),
    ([1], 1),
    ([0, 1], 2),
    ([1, 0], 2),
    ([1, 1, 1], 3),
    ([1, 0, 1], 3),
    ([2, 1, 0, 1, 1, 0, 1, 2], 8)
])
def test_len(make_linked_list, values, expected):
    linked_list = make_linked_list(values)
    linked_list.len() == expected

@pytest.mark.parametrize("values, param, position, expected", [
    ([0], 1, 0, [0, 1]),
    ([0, 1], 2, 0, [0, 2, 1]),
    ([0, 1], 2, 1, [0, 1, 2]),
    ([0, 1, 2, 3], 4, 1, [0, 1, 4, 2, 3]),
    ([], 1, None, [1]),
    ([0], 1, None, [1, 0]),
    ([0, 1], 2, None, [2, 0, 1])
])
def test_insert_node(make_linked_list, linked_list_to_list, get_node_by_id, values,
                     param, position, expected):
    linked_list = make_linked_list(values)
    if position is None:
        linked_list.insert(None, Node(param))
    else:
        linked_list.insert(get_node_by_id(linked_list, position), Node(param))
    check_head_and_tail(linked_list, expected)
    assert linked_list_to_list(linked_list) == expected

@pytest.mark.parametrize("values_1, values_2, expected", [
    ([0], [0], [0]),
    ([0], [1], [1]),
    ([1], [0], [1]),
    ([1], [1], [2]),
    ([], [], []),
    ([10], [1], [11]),
    ([1], [10], [11]),
    ([21, 21, 21, 42], [21, 21, 21, 42], [42, 42, 42, 84])
])
def test_list_sum(make_linked_list, linked_list_to_list, values_1, values_2, expected):
    linked_list_1 = make_linked_list(values_1)
    linked_list_2 = make_linked_list(values_2)
    result = linked_list_sum(linked_list_1, linked_list_2)
    assert linked_list_to_list(result) == expected

