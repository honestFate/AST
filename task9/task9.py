class NativeDictionary:
    def __init__(self, sz: int) -> None:
        self.size = sz
        self.slots: list[str | None] = [None] * self.size
        self.values: list[object] = [None] * self.size

    def hash_fun(self, key: str) -> int:
        return sum(ord(char) for char in key) % self.size

    def _seek_slot(self, key: str) -> int | None:
        index = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[index] is None or self.slots[index] == key:
                return index
            index = (index + 1) % self.size
        return None

    def is_key(self, key: str) -> bool:
        index = self._seek_slot(key)
        return index is not None and self.slots[index] == key

    def put(self, key: str, value: object) -> None:
        index = self._seek_slot(key)
        if index is None:
            return
        self.slots[index] = key
        self.values[index] = value

    def get(self, key: str) -> object:
        index = self._seek_slot(key)
        if index is None or self.slots[index] != key:
            return None
        return self.values[index]
