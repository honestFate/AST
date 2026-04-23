import pytest
from task1 import Node, LinkedList

def make_linked_list(values):
    linkedList = LinkedList()
    for v in values:
        linkedList.add_in_tail(Node(v))
    return linkedList

@pytest.mark.parametrize("values, param, expected", [
    ([0], 1, [0]),
    ([1], 1, []),
    ([0, 1], 1, [0]),
])
def test_delete_single(values, param, expected):
    linkedList = make_linked_list(values)
    linkedList.delete(param)
    head = linkedList.head
    result = []
    while head is not None:
        result.append(head.value)
        head = head.next
    assert result == expected

# @pytest.mark.parametrize("values, param, expected", [
#     ([0], 1, [0]),
#     ([1], 1, []),
#     ([0, 1], 1, [0]),
# ])
# def test_delete_single(values, param, expected):
#     linkedList = make_linked_list(values)
#     linkedList.delete(param, all=True)
#     head = linkedList.head
#     result = []
#     while head.next is not None:
#         result.append(head.value)
#         head = head.next
#     assert result == expected