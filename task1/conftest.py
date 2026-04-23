import pytest
from task1 import Node, LinkedList

@pytest.fixture
def make_linked_list():
    def _make_list(values):
        linkedList = LinkedList()
        for v in values:
            linkedList.add_in_tail(Node(v))
        return linkedList
    return _make_list

@pytest.fixture
def linked_list_to_list():
    def _make_list(linkedList):
        values = []
        node = linkedList.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return values
    return _make_list