from __future__ import annotations

from typing import Any


class PowerSet:
    def __init__(self) -> None:
        self._items: dict[Any, None] = {}

    def size(self) -> int:
        return len(self._items)

    def put(self, value: Any) -> None:
        self._items[value] = None

    def get(self, value: Any) -> bool:
        return value in self._items

    def remove(self, value: Any) -> bool:
        if value not in self._items:
            return False
        del self._items[value]
        return True

    def intersection(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for value in self._items:
            if value in set2._items:
                result.put(value)
        return result

    def union(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for value in self._items:
            result.put(value)
        for value in set2._items:
            result.put(value)
        return result

    def difference(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for value in self._items:
            if value not in set2._items:
                result.put(value)
        return result

    def issubset(self, set2: PowerSet) -> bool:
        return all(value in self._items for value in set2._items)

    def equals(self, set2: PowerSet) -> bool:
        return self.size() == set2.size() and self.issubset(set2)

