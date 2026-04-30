from task2 import LinkedList2, Node


class Dummy(Node):
    def __init__(self):
        super().__init__(None)

class DummyLinkedList2:
    def __init__(self):
        self.head = Dummy()
        self.tail = Dummy()
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def add_in_tail(self, item):
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev.next = item
        self.tail.prev = item

    def find(self, val):
        node = self.head.next
        while type(node) != Dummy:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []
        node = self.head.next
        while type(node) != Dummy:
            if node.value == val:
                found_nodes.append(node)
            node = node.next
        return found_nodes

    def delete(self, val, all=False):
        node = self.head.next
        while type(node) != Dummy:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
            if node.value == val and not all:
                return
            node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        node = self.head.next
        i = 0
        while type(node) != Dummy:
            i += 1
            node = node.next
        return i

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        newNode.next = afterNode.next
        newNode.prev = afterNode
        afterNode.next.prev = newNode
        afterNode.next = newNode

    def add_in_head(self, newNode):
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode


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

def linked_list_2_bubble_sort(linked_list):
    if linked_list.len() < 2:
        return
    node = linked_list.tail
    while node is not linked_list.head:
        nested_node = linked_list.head
        while nested_node != node:
            if nested_node.value > nested_node.next.value:
                temp = nested_node.value
                nested_node.value = nested_node.next.value
                nested_node.next.value = temp
            nested_node = nested_node.next
        node = node.prev

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
рефлексия: просто меняем местами prev с next, в конце меняем указатели
начала и конца списка.


task: 2.11
name: detect cycle in linked list (Floyd's tortoise and hare)
time: O(n)
memory: O(1)
рефлексия: не понял рекомендации, думал, что мы не храним длину списка.
Алгоритм Флойда нашёл в интернете. Он был рассчитан на односвязный
список, поэтому была идея просто всегда проверять что prev у
следующей ноды ведет на текущую. Но не был уверен, что будет в
тестовых данных и такой подход пройдет тесты.


task: 2.12
name: sort doubly linked list (returns new list)
time: O(n log n)
memory: O(n)
рефлексия: почему-то подумал, что не нужно писать саму сортировку.
Добавил linked_list_2_bubble_sort, вложенный цикл с O(n^2) сложностью и
O(1) по памяти. Большенство алгоритмов не подходят, т.к. нет произвольного
доступа к элементам, которое в них подразумевается. 


task: 2.13
name: concat two sorted doubly linked lists via merge
time: O(n log n + m log m) на сортировку входных, O(n + m) на merge
memory: O(n + m)
рефлексия: для отсортированных данных просто выбираем подходящий элемент,
пока не закончатся элементы в одной из структур. Затем добавляем всё,
что осталось.
"""

