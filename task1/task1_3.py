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
    ([2, 1, 0, 1, 1, 0, 1, 2], 2, [1, 0, 1, 1, 0, 1, 2]),
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
    ([2, 1, 0, 1, 1, 0, 1, 2], 2, [1, 0, 1, 1, 0, 1]),
])
def test_delete_all(make_linked_list, linked_list_to_list, values, param, expected):
    linkedList = make_linked_list(values)
    linkedList.delete(param, all=True)
    check_head_and_tail(linkedList, expected)
    assert linked_list_to_list(linkedList) == expected