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

    def _on_add_start(self):
        self._credits += self.APPEND_TARIFF

    def _on_remove_start(self):
        self._credits += self.DELETE_TARIFF

    def _on_copy(self, n):
        self.charge(n)

    def _on_shift(self, n):
        self.charge(n)

    def _on_write(self):
        self.charge(1)


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


task: 3.6
name: BankDynArray
рефлексия: использовал гораздо большие тарифы, чтобы пройти
тесты, стоило изменить порог сжатия массива, либо тарифы на
реаллокацию

task: 3.7
name: MdDynArray
рефлексия: реализовал рекурсивный многомерный массив, если
количество измерений известно при инициализации, стоило
реализовать через обычный одномерный массив внутри
"""

