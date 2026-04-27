from task2 import LinkedList2, Node


def linked_list_2_reverse(linked_list):
    node = linked_list.head
    while node is not None:
        temp = node.next
        node.next = node.prev
        node.prev = temp
        node = temp
    linked_list.head, linked_list.tail = linked_list.tail, linked_list.head

def linked_list_2_sort(linked_list):
    values = []
    node = linked_list.head
    while node is not None:
        values.append(node.value)
        node = node.next
    values.sort()
    result = LinkedList2()
    for v in values:
        result.add_in_tail(Node(v))
    return result

def linked_list_2_is_cycled(linked_list):
    if linked_list.head is None:
        return False
    slow = linked_list.head
    fast = linked_list.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def linked_list_2_concat(linked_list_1, linked_list_2):
    sorted_1 = linked_list_2_sort(linked_list_1)
    sorted_2 = linked_list_2_sort(linked_list_2)
    result = LinkedList2()
    node1 = sorted_1.head
    node2 = sorted_2.head
    while node1 is not None and node2 is not None:
        if node1.value <= node2.value:
            result.add_in_tail(Node(node1.value))
            node1 = node1.next
        else:
            result.add_in_tail(Node(node2.value))
            node2 = node2.next
    while node1 is not None:
        result.add_in_tail(Node(node1.value))
        node1 = node1.next
    while node2 is not None:
        result.add_in_tail(Node(node2.value))
        node2 = node2.next
    return result

"""
task: 2.1
name: find first node by value
time: O(n)
memory: O(1)


task: 2.2
name: find all nodes by value
time: O(n)
memory: O(n)


task: 2.3
name: delete first occurrence of node by value
time: O(n)
memory: O(1)


task: 2.4
name: option to delete all occurrences of val in linked list
time: O(n)
memory: O(1)


task: 2.5
name: insert new node after given node
time: O(1)
memory: O(1)


task: 2.6
name: add new node in head of linked list
time: O(1)
memory: O(1)


task: 2.7
name: clean linked list
time: O(1)
memory: O(1)


task: 2.8
name: len of linked list
time: O(n)
memory: O(1)


task: 2.9
name: tests


task: 2.10
name: reverse doubly linked list in place
time: O(n)
memory: O(1)


task: 2.11
name: detect cycle in linked list (Floyd's tortoise and hare)
time: O(n)
memory: O(1)


task: 2.12
name: sort doubly linked list (returns new list)
time: O(n log n)
memory: O(n)


task: 2.13
name: concat two sorted doubly linked lists via merge
time: O(n log n + m log m) на сортировку входных, O(n + m) на merge
memory: O(n + m)
"""

