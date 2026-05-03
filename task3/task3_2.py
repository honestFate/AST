from task3 import DynArray


class BankDynArray(DynArray):
    APPEND_TARIFF = 9
    DELETE_TARIFF = 2

    def __init__(self):
        super().__init__()
        self._credits = 0

    def charge(self, amount):
        self._credits -= amount
        assert self._credits >= 0

    def append(self, itm):
        self._credits += self.APPEND_TARIFF
        if self.count == self.capacity:
            self.charge(self.count)
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1
        self.charge(1)

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        self._credits += self.APPEND_TARIFF
        if self.count == self.capacity:
            self.charge(self.count)
            self.resize(2 * self.capacity)
        for k in range(self.count, i, -1):
            self.array[k] = self.array[k - 1]
        self.charge(self.count - i)
        self.array[i] = itm
        self.count += 1
        self.charge(1)

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        self._credits += self.DELETE_TARIFF
        for k in range(i, self.count - 1):
            self.array[k] = self.array[k + 1]
        self.charge(self.count - i - 1)
        self.array[self.count - 1] = None
        self.count -= 1
        self.charge(1)
        if self.count < self.capacity / 2 and self.capacity > self.min_capacity:
            new_capacity = max(int(self.capacity / 1.5), self.min_capacity)
            self.charge(self.count)
            self.resize(new_capacity)

class MdDynArray:
    def __init__(self, dims, fill=None):
        self.dims = list(dims)
        self.fill = fill
        self._data = DynArray()
        for _ in range(self.dims[0]):
            if len(self.dims) == 1:
                self._data.append(fill)
            else:
                self._data.append(MdDynArray(self.dims[1:], fill))

    def __getitem__(self, key):
        if not isinstance(key, tuple):
            key = (key,)
        head = key[0]
        tail = key[1:]
        if not tail:
            return self._data[head]
        return self._data[head][tail]

    def __setitem__(self, key, value):
        if not isinstance(key, tuple):
            key = (key,)
        head = key[0]
        tail = key[1:]
        if not tail:
            self._data[head] = value
        else:
            self._data[head][tail] = value

    def __len__(self):
        return self.dims[0]

"""
task: 3.1
name: insert value in dynamic array
time: O(n)
memory: O(n)


task: 3.2
name: delete value in dynamic array
time: O(n)
memory: O(n)
"""

