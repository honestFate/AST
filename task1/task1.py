class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        founded_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                founded_nodes.append(node)
            node = node.next
        return founded_nodes

    def delete(self, val, all=False):
        prev_node = None
        node = self.head
        while node is not None:
            if node.value == val:
                if prev_node is not None:
                    prev_node.next = node.next
                else:
                    self.head = node.next
                if node.next is None:
                    self.tail = prev_node
                if not all:
                    return
            else:
                prev_node = node
            node = node.next
        return

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        i = 0
        while node is not None:
            node = node.next
            i += 1
        return i

    def insert(self, afterNode, newNode):
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return
        newNode.next = afterNode.next
        afterNode.next = newNode
        if afterNode == self.tail:
            self.tail = newNode