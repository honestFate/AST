import pytest


@pytest.mark.parametrize("values, param, pos, expected", [
    ([], 1, 0, [1]),
    ([1], 2, 1, [1, 2]),
    ([1], 2, 0, [2, 1]),
    ([1, 2, 4], 3, 0, [3, 1, 2, 4]),
    ([1, 2, 4], 3, 1, [1, 3, 2, 4]),
    ([1, 2, 4], 3, 2, [1, 2, 3, 4]),
    ([1, 2, 4], 3, 3, [1, 2, 4, 3]),
])
def test_insert(make_dyn_array, values, param, pos, expected):
    arr = make_dyn_array(values)
    arr.insert(pos, param)
    assert arr == make_dyn_array(expected)

@pytest.mark.parametrize("values, pos, expected", [
    ([1], 0, []),
    ([1, 2], 0, [2]),
    ([1, 2], 1, [1]),
    ([1, 2, 3], 0, [2, 3]),
    ([1, 2, 3], 1, [1, 3]),
    ([1, 2, 3], 2, [1, 2]),
])
def test_delete(make_dyn_array, values, pos, expected):
    arr = make_dyn_array(values)
    arr.delete(pos)
    assert arr == make_dyn_array(expected)

@pytest.mark.parametrize("values, pos", [
    ([], -1),
    ([], 1),
    ([1, 2, 4], -10),
    ([1, 2, 4], 4),
    ([1, 2, 4], 100)
])
def test_index_exception(make_dyn_array, values, pos):
    arr = make_dyn_array(values)
    with pytest.raises(IndexError):
        arr.insert(pos, "some value")
    with pytest.raises(IndexError):
        arr.delete(pos)
    assert arr == make_dyn_array(values)
