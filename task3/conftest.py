import pytest
from task3 import DynArray

@pytest.fixture
def make_dyn_array():
    def _make_dyn_array(values):
        arr = DynArray()
        for v in values:
            arr.append(v)
        return arr
    return _make_dyn_array