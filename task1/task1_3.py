import pytest
from task1 import Node, LinkedList

def check_head_and_tail(linkedList, expected):
    if len(expected) == 0:
        assert linkedList.head is None
        assert linkedList.tail is None
        return
    if len(expected) == 1:
        assert linkedList.head == linkedList.tail
    assert linkedList.head is not None
    assert linkedList.tail is not None
    assert linkedList.head.value == expected[0]
    assert linkedList.tail.value == expected[-1]
    assert linkedList.tail.next is None

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
    linkedList = make_linked_list(values)
    linkedList.delete(param)
    check_head_and_tail(linkedList, expected)
    assert linked_list_to_list(linkedList) == expected

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
    linkedList = make_linked_list(values)
    linkedList.delete(param, all=True)
    check_head_and_tail(linkedList, expected)
    assert linked_list_to_list(linkedList) == expected

@pytest.mark.parametrize("values, expected", [
    ([0], []),
    ([1], []),
    ([0, 1], []),
    ([1, 0], []),
    ([1, 1, 1], []),
    ([1, 0, 1], [])
])
def test_clean(make_linked_list, linked_list_to_list, values, expected):
    linkedList = make_linked_list(values)
    linkedList.clean()
    check_head_and_tail(linkedList, expected)
    assert linked_list_to_list(linkedList) == expected

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
    linkedList = make_linked_list(values)
    for result_node, expected_node in zip(linkedList.find_all(param), expected):
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
    linkedList = make_linked_list(values)
    linkedList.len() == expected

@pytest.mark.parametrize("values, param, position, expected", [
    ([0], 1, 0, [0, 1]),
    ([0, 1], 2, 0, [0, 2, 1]),
    ([0, 1], 2, 1, [0, 1, 2]),
    ([0, 1, 2, 3], 4, 1, [0, 1, 4, 2, 3]),
    ([], 1, None, [1]),
    ([0], 1, None, [1, 0]),
    ([0, 1], 2, None, [2, 0, 1])
])
def test_insert_node(make_linked_list, linked_list_to_list, get_node_by_id, values, param, position, expected):
    linkedList = make_linked_list(values)
    if position is None:
        linkedList.insert(None, Node(param))
    else:
        linkedList.insert(get_node_by_id(linkedList, position), Node(param))
    check_head_and_tail(linkedList, expected)
    assert linked_list_to_list(linkedList) == expected