from task1 import LinkedList, Node


def linked_list_sum(l1, l2):
    if l1.len() != l2.len():
        return None
    result = LinkedList()
    l1_node = l1.head
    l2_node = l2.head
    while l1_node is not None:
        result_node = Node(l1_node.value + l2_node.value)
        result.add_in_tail(result_node)
        l1_node = l1_node.next
        l2_node = l2_node.next
    return result

