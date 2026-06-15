import pytest

from task8 import HashTable


@pytest.fixture
def make_hash_table():
    def _make(values=(), sz=17, stp=3):
        table = HashTable(sz, stp)
        for value in values:
            table.put(value)
        return table

    return _make

