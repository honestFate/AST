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

"""
task: 1.1
name: delete node from linked list method
time: O(n)
memory: O(1)
reflection: ...


task: 1.2
name: option to delete all occurse of val in linked list
time: O(n)
memory: O(1)
reflection: ...


task: 1.3
name: clean linked list method
time: O(1)
memory: O(1)
reflection: ...


task: 1.4
name: method that searches linked list and returns list of nodes
time: O(n)
memory: O(n)
reflection: ...


task: 1.5
name: len method
time: O(n)
memory: O(1)
reflection: ...


task: 1.6
name: insert new node into linked list
time: O(1)
memory: O(1)
reflection: ...


task: 1.7
name: tests
time: O(n)
memory: O(n)
reflection: ...


task: 1.8
name: function for creation new linked list where l[n] = l1[n] + l2[n]
time: O(n)
memory: O(n)
reflection: ...
"""

