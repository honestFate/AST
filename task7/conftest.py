import pytest

from task7 import OrderedList, OrderedStringList


@pytest.fixture
def make_ordered_list():
    def _make(values, asc=True):
        ordered = OrderedList(asc)
        for v in values:
            ordered.add(v)
        return ordered
    return _make


@pytest.fixture
def make_ordered_string_list():
    def _make(values, asc=True):
        ordered = OrderedStringList(asc)
        for v in values:
            ordered.add(v)
        return ordered
    return _make

