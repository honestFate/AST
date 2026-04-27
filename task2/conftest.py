import pytest

from task2 import LinkedList2, Node


@pytest.fixture
def make_linked_list_2():
    def _make_list_2(values):
        linked_list = LinkedList2()
        for v in values:
            linked_list.add_in_tail(Node(v))
        return linked_list
    return _make_list_2

@pytest.fixture
def linked_list_2_to_list():
    def _to_list(linked_list):
        values = []
        node = linked_list.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return values
    return _to_list

@pytest.fixture
def linked_list_2_to_list_reversed():
    def _to_list(linked_list):
        values = []
        node = linked_list.tail
        while node is not None:
            values.append(node.value)
            node = node.prev
        return values
    return _to_list

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

