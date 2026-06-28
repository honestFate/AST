class OrderedListDictionary:
    def __init__(self) -> None:
        self.keys: list[str] = []
        self.values: list[object] = []

    def _bisect(self, key: str) -> int:
        low = 0
        high = len(self.keys)
        while low < high:
            mid = (low + high) // 2
            if self.keys[mid] < key:
                low = mid + 1
            else:
                high = mid
        return low

    def is_key(self, key: str) -> bool:
        index = self._bisect(key)
        return index < len(self.keys) and self.keys[index] == key

    def put(self, key: str, value: object) -> None:
        index = self._bisect(key)
        if index < len(self.keys) and self.keys[index] == key:
            self.values[index] = value
            return
        self.keys.insert(index, key)
        self.values.insert(index, value)

    def get(self, key: str) -> object:
        index = self._bisect(key)
        if index < len(self.keys) and self.keys[index] == key:
            return self.values[index]
        return None

    def delete(self, key: str) -> bool:
        index = self._bisect(key)
        if index >= len(self.keys) or self.keys[index] != key:
            return False
        self.keys.pop(index)
        self.values.pop(index)
        return True


class BitStringDictionary:
    def __init__(self, key_length: int) -> None:
        self.key_length = key_length
        self.size = 1 << key_length
        self.values: list[object] = [None] * self.size
        self.present: list[bool] = [False] * self.size

    def _index(self, key: str) -> int:
        index = 0
        for bit in key:
            index = (index << 1) | int(bit)
        return index

    def is_key(self, key: str) -> bool:
        return self.present[self._index(key)]

    def put(self, key: str, value: object) -> None:
        index = self._index(key)
        self.values[index] = value
        self.present[index] = True

    def get(self, key: str) -> object:
        index = self._index(key)
        if self.present[index]:
            return self.values[index]
        return None

    def delete(self, key: str) -> bool:
        index = self._index(key)
        if not self.present[index]:
            return False
        self.values[index] = None
        self.present[index] = False
        return True


"""
task: 10.1
name: put key-value pair
time: O(1) в среднем, O(n) в худшем случае
memory: O(1)

task: 10.2
name: is_key
time: O(1) в среднем, O(n) в худшем случае
memory: O(1)

task: 10.3
name: get value by key
time: O(1) в среднем, O(n) в худшем случае
memory: O(1)

task: 10.5
name: dictionary on ordered array
time: поиск O(log n), вставка и удаление O(n)
memory: O(n)
рефлексия: у меня два параллельных отсортированных списка, ключи и значения вместе.
Нужно держать values как append-only, а в упорядоченном списке хранить пары
[ключ, индекс] и сдвигать только их. Но нужно решить проблему удаления в values, т.к.
индексы инвалидируются.

task: 10.6
name: dictionary with bit-string keys
time: O(k) на вычисление индекса, O(1) на доступ (k фиксирована)
memory: O(2^k)
"""

