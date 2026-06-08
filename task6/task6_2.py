import ctypes

INITIAL_CAPACITY = 16


class DynamicArrayDeque:
    def __init__(self):
        self._capacity = INITIAL_CAPACITY
        self._array = self._make_array(self._capacity)
        self._head = 0
        self._count = 0

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def _index(self, offset):
        return (self._head + offset) % self._capacity

    def size(self):
        return self._count

    def addFront(self, item):
        self._grow_if_full()
        self._head = (self._head - 1) % self._capacity
        self._array[self._head] = item
        self._count += 1

    def addTail(self, item):
        self._grow_if_full()
        self._array[self._index(self._count)] = item
        self._count += 1

    def removeFront(self):
        if self._count == 0:
            return None
        item = self._array[self._head]
        self._array[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._count -= 1
        self._shrink_if_sparse()
        return item

    def removeTail(self):
        if self._count == 0:
            return None
        tail = self._index(self._count - 1)
        item = self._array[tail]
        self._array[tail] = None
        self._count -= 1
        self._shrink_if_sparse()
        return item

    def _grow_if_full(self):
        if self._count < self._capacity:
            return
        self._resize(self._capacity * 2)

    def _shrink_if_sparse(self):
        if self._capacity <= INITIAL_CAPACITY or self._count > self._capacity // 4:
            return
        self._resize(self._capacity // 2)

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for offset in range(self._count):
            new_array[offset] = self._array[self._index(offset)]
        self._array = new_array
        self._capacity = new_capacity
        self._head = 0


def is_palindrome(text):
    deque = DynamicArrayDeque()
    for char in text:
        deque.addTail(char)
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True


def is_balanced(expression):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in expression:
        if char not in pairs:
            stack.append(char)
        elif not stack or stack.pop() != pairs[char]:
            return False
    return not stack


"""
task: 7.1
name: front vs tail complexity
time: addFront/removeFront O(n), addTail/removeTail O(1) (addTail амортизированно)
memory: O(1)
В Deque реализованной через list addTail = append и removeTail = pop выполняются
за O(1) амортизированно, т.к. сдвиг не нужен. addFront = insert и
removeFront = pop(0) работают за O(n), при вставке/удалении в начало листа все
последующие элементы сдвигаются

task: 7.2
name: tests
time: O(n)
memory: O(n)

task: 7.3
name: palindrome check
time: O(n)
memory: O(n)
рефлексия: записываю строку посимволно в deque, затем беру по 1 элементу с начала
и конца и сравниваю.

task: 7.4
name: minimum element in deque
time: get_min O(1); удаление текущего минимума O(n)
memory: O(1)
рефлексия: не дошел до корректного решения через вторую деку, решил через
кэширование минимума и его пересчёте, если минимум удалён.

task: 7.5
name: deque (dynamic array)
time: addFront/addTail/removeFront/removeTail O(1) амортизированно
memory: O(n)

task: 7.6
name: balanced check (three types)
time: O(n)
memory: O(n)
рефлексия: дин массив реализован внутри deque, т.к. использование в том же
виде динамического массива из старого задания была невозможна из-за
используемого тут кольцевого указателя. Нужно переписать и вынести дин
массив в отдельный класс.
"""

