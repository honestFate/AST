import pytest

from task1 import LinkedList, Node


@pytest.fixture
def make_linked_list():
    def _make_list(values):
        linked_list = LinkedList()
        for v in values:
            linked_list.add_in_tail(Node(v))
        return linked_list
    return _make_list

@pytest.fixture
def linked_list_to_list():
    def _make_list(linked_list):
        values = []
        node = linked_list.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return values
    return _make_list

@pytest.fixture
def get_node_by_id():
    def _get_node(linked_list, id):
        i = 0
        node = linked_list.head
        while node is not None and i != id:
            i += 1
            node = node.next
        return node
    return _get_node
