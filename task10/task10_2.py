from typing import Any

from task10 import PowerSet


class ProductPowerSet(PowerSet):
    def cartesian_product(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for left in self._items:
            for right in set2._items:
                result.put((left, right))
        return result


def intersection_many(sets: list[PowerSet]) -> PowerSet:
    if len(sets) < 3:
        return PowerSet()
    result = sets[0]
    for other in sets[1:]:
        result = result.intersection(other)
    return result


class Bag:
    def __init__(self) -> None:
        self._counts: dict[Any, int] = {}

    def size(self) -> int:
        return sum(self._counts.values())

    def add(self, value: Any) -> None:
        self._counts[value] = self._counts.get(value, 0) + 1

    def remove(self, value: Any) -> bool:
        if value not in self._counts:
            return False
        self._counts[value] -= 1
        if self._counts[value] == 0:
            del self._counts[value]
        return True

    def frequencies(self) -> list[tuple[Any, int]]:
        return list(self._counts.items())


"""
task: 11.1
name: PowerSet basic operations
time: put, get, remove, size O(1) в среднем
memory: O(1)

task: 11.2
name: set operations
time: intersection, difference, issubset, equals O(n); union O(n + m)
memory: O(n)

task: 11.4
name: cartesian product
time: O(n * m)
memory: O(n * m)

task: 11.5
name: intersection of three or more sets
time: O(k * n), k - число множеств
memory: O(n)

task: 11.6
name: multiset Bag
time: add, remove O(1) в среднем; frequencies O(n)
memory: O(n)
"""

