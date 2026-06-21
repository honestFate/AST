import secrets
from itertools import islice, permutations

from task8 import HashTable


class DynamicHashTable(HashTable):
    def __init__(self, sz: int = 17, stp: int = 3, load_factor: float = 0.75) -> None:
        super().__init__(sz, stp)
        self.count = 0
        self.load_factor = load_factor

    def _is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

    def _next_prime(self, n: int) -> int:
        candidate = n
        while not self._is_prime(candidate):
            candidate += 1
        return candidate

    def _place(self, value: str) -> int | None:
        index = self.seek_slot(value)
        if index is None:
            return None
        if self.slots[index] is None:
            self.count += 1
        self.slots[index] = value
        return index

    def _resize(self) -> None:
        values = [value for value in self.slots if value is not None]
        self.size = self._next_prime(self.size * 2)
        self.slots = [None] * self.size
        self.count = 0
        for value in values:
            self._place(value)

    def put(self, value: str) -> int | None:
        if (self.count + 1) / self.size > self.load_factor:
            self._resize()
        index = self._place(value)
        if index is None:
            self._resize()
            index = self._place(value)
        return index


class MultiHashTable:
    _BASES = (257, 263, 269, 271, 277, 281, 283, 293)

    def __init__(self, sz: int, hash_count: int = 2) -> None:
        self.size = sz
        self.hash_count = hash_count
        self.slots: list[str | None] = [None] * self.size
        self.bases = self._make_bases()

    def _make_bases(self) -> list[int]:
        bases: list[int] = []
        for seed in self._BASES:
            base = seed % self.size
            if base >= 2 and base not in bases:
                bases.append(base)
            if len(bases) == self.hash_count:
                return bases
        candidate = 2
        while len(bases) < self.hash_count and candidate < self.size:
            if candidate not in bases:
                bases.append(candidate)
            candidate += 1
        return bases

    def _candidates(self, value: str) -> list[int]:
        result: list[int] = []
        for base in self.bases:
            acc = 0
            for char in value:
                acc = (acc * base + ord(char)) % self.size
            if acc not in result:
                result.append(acc)
        return result

    def put(self, value: str) -> int | None:
        candidates = self._candidates(value)
        for index in candidates:
            if self.slots[index] == value:
                return index
        for index in candidates:
            if self.slots[index] is None:
                self.slots[index] = value
                return index
        return None

    def find(self, value: str) -> int | None:
        for index in self._candidates(value):
            if self.slots[index] == value:
                return index
        return None


class SaltedHashTable(HashTable):
    def __init__(self, sz: int, stp: int, salt: int | None = None) -> None:
        super().__init__(sz, stp)
        if salt is None:
            self.base = secrets.randbelow(self.size - 2) + 2
        else:
            self.base = (salt % (self.size - 2)) + 2

    def hash_fun(self, value: str) -> int:
        acc = 0
        for char in value:
            acc = (acc * self.base + ord(char)) % self.size
        return acc


def make_collision_keys(count: int) -> list[str]:
    perms = permutations("abcdefgh")
    return ["".join(perm) for perm in islice(perms, count)]


def probe_count(table: HashTable, value: str) -> int:
    index = table.hash_fun(value)
    inspected = 1
    while table.slots[index] is not None and table.slots[index] != value:
        index = (index + table.step) % table.size
        inspected += 1
        if inspected >= table.size:
            break
    return inspected


def ddos_flood(table: HashTable, keys: list[str]) -> int:
    total = 0
    for key in keys:
        total += probe_count(table, key)
        table.put(key)
    return total


"""
task: 9.1
name: cryptographic hash functions (SHA-256, MD5)

task: 9.2
name: consistent hashing

task: 9.3
name: DynamicHashTable
time: put O(1) амортизированно, O(n) при рехешировании
memory: O(n)
рефлексия: Использовал наследование вместо композиции, не используется динамический
массив. Нет геттера для буфера, ресайз неявный.

task: 9.4
name: MultiHashTable
time: put/find O(d * k), d - число хэш-функций, k - длина строки
memory: O(n)

task: 9.5
name: collision attack and SaltedHashTable
time: ddos_flood O(n^2) на исходной, O(n) на солёной
memory: O(1)
рефлексия: использовал фиксированную соль на всю таблицу, а не динамическую
для каждого значения.
"""

