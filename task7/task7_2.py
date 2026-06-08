from task7 import Node


def merge_ordered_lists(first, second):
    result = type(first)(first.is_ascending())
    a = first.head
    b = second.head
    while a is not None and b is not None:
        if first.compare(a.value, b.value) == 0 or first._precedes(a.value, b.value):
            result._append(Node(a.value))
            a = a.next
        else:
            result._append(Node(b.value))
            b = b.next
    while a is not None:
        result._append(Node(a.value))
        a = a.next
    while b is not None:
        result._append(Node(b.value))
        b = b.next
    return result


"""
task: 8.1
name: asc and clean

task: 8.2
name: compare
time: O(1)
memory: O(1)

task: 8.3
name: add
time: O(n)
memory: O(1)

task: 8.4
name: delete
time: O(n)
memory: O(1)

task: 8.5
name: OrderedStringList

task: 8.6
name: find
time: O(n) в худшем случае, в среднем ~O(n/2)
memory: O(1)

task: 8.8
name: remove_duplicates
time: O(n)
memory: O(1)

task: 8.9
name: merge_ordered_lists
time: O(n + m)
memory: O(n + m)

task: 8.10
name: contains_sublist
time: O(n + m)
memory: O(1)

task: 8.11
name: most_frequent
time: O(n)
memory: O(1)

task: 8.12
name: find_index
time: O(n)
memory: O(1)
"""

