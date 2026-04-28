import pytest
from task3 import DynArray

@pytest.mark.parametrize("values, param, pos, expected", [
    ([1, 2, 4], 3, 2, [1, 2, 3, 4])
])
def test_insert(make_dyn_array, values, param, pos, expected):
    arr = make_dyn_array(values)
    print(arr[0])
    arr.insert(pos, param)
    assert arr == make_dyn_array(expected)