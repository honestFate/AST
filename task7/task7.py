class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def is_ascending(self):
        return self.__ascending

    def _should_go_first(self, value, other):
        result = self.compare(value, other)
        if self.__ascending:
            return result < 0
        return result > 0

    def _append(self, new_node):
        new_node.prev = self.tail
        new_node.next = None
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def _insert_before(self, node, new_node):
        if node is None:
            self._append(new_node)
            return
        prev = node.prev
        new_node.prev = prev
        new_node.next = node
        node.prev = new_node
        if prev is None:
            self.head = new_node
        else:
            prev.next = new_node

    def _unlink(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def add(self, value):
        new_node = Node(value)
        node = self.head
        while node is not None and not self._should_go_first(value, node.value):
            node = node.next
        self._insert_before(node, new_node)

    def find(self, val):
        node = self.head
        while node is not None:
            if self.compare(node.value, val) == 0:
                return node
            if self._should_go_first(val, node.value):
                return None
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if self.compare(node.value, val) == 0:
                self._unlink(node)
                return
            if self._should_go_first(val, node.value):
                return
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def remove_duplicates(self):
        node = self.head
        while node is not None and node.next is not None:
            if self.compare(node.value, node.next.value) == 0:
                self._unlink(node.next)
            else:
                node = node.next

    def contains_sublist(self, other):
        node = self.head
        target = other.head
        while target is not None:
            while node is not None and self.compare(node.value, target.value) != 0:
                node = node.next
            if node is None:
                return False
            node = node.next
            target = target.next
        return True

    def most_frequent(self):
        if self.head is None:
            return None
        mode = self.head.value
        best_count = 1
        current_count = 1
        node = self.head.next
        while node is not None:
            if self.compare(node.value, node.prev.value) == 0:
                current_count += 1
            else:
                current_count = 1
            if current_count > best_count:
                best_count = current_count
                mode = node.value
            node = node.next
        return mode

    def find_index(self, val):
        index = 0
        node = self.head
        while node is not None:
            if self.compare(node.value, val) == 0:
                return index
            if self._should_go_first(val, node.value):
                return -1
            node = node.next
            index += 1
        return -1


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super().__init__(asc)

    def compare(self, v1, v2):
        s1 = v1.strip()
        s2 = v2.strip()
        if s1 < s2:
            return -1
        if s1 > s2:
            return 1
        return 0

