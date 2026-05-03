import random

import pytest
from task3_2 import BankDynArray

from task3 import DynArray


@pytest.fixture
def make_dyn_array():
    def _make_dyn_array(values):
        arr = DynArray()
        for v in values:
            arr.append(v)
        return arr
    return _make_dyn_array

@pytest.fixture
def make_rand_dyn_array():
    def _make_dyn_array(size):
        arr = DynArray()
        for i in range(size):
            arr.append(random.randint(1, 100))
        return arr
    return _make_dyn_array

@pytest.fixture
def banker_array():
    return BankDynArray()

