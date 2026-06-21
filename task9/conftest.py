import pytest

from task9 import NativeDictionary


@pytest.fixture
def make_native_dictionary():
    def _make(items=(), sz=17):
        table = NativeDictionary(sz)
        for key, value in items:
            table.put(key, value)
        return table

    return _make

