class HashTable:
    def __init__(self, sz: int, stp: int) -> None:
        self.size = sz
        self.step = stp
        self.slots: list[str | None] = [None] * self.size

    def hash_fun(self, value: str) -> int:
        return sum(ord(char) for char in value) % self.size

    def seek_slot(self, value: str) -> int | None:
        index = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[index] is None or self.slots[index] == value:
                return index
            index = (index + self.step) % self.size
        return None

    def put(self, value: str) -> int | None:
        index = self.seek_slot(value)
        if index is None:
            return None
        self.slots[index] = value
        return index

    def find(self, value: str) -> int | None:
        index = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[index] == value:
                return index
            if self.slots[index] is None:
                return None
            index = (index + self.step) % self.size
        return None

