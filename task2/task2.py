class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            if node.next == self.head:
                return None
            node = node.next
        return None

    def find_all(self, val):
        found_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            if node.next == self.head:
                return found_nodes
            node = node.next
        return found_nodes

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None or node.prev == self.tail:
                    self.head = node.next
                if node.next is None or node.next == self.head:
                    self.tail = node.prev
                if node.next is not None:
                    node.next.prev = node.prev
                if node.prev is not None:
                    node.prev.next = node.next
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        i = 0
        while node is not None:
            i += 1
            if node.next == self.head:
                return i
            node = node.next
        return i

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_head(newNode)
            return
        if self.head is None:
            raise("afterNode should be None, when inserting in empty list")
        if afterNode == self.tail:
            self.add_in_tail(newNode)
            return
        newNode.next = afterNode.next
        newNode.prev = afterNode
        afterNode.next.prev = newNode
        afterNode.next = newNode

    def add_in_head(self, newNode):
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.tail = newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode