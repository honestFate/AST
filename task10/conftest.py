import pytest

from task10 import PowerSet


@pytest.fixture
def make_power_set():
    def _make(values=()):
        power_set = PowerSet()
        for value in values:
            power_set.put(value)
        return power_set

    return _make

