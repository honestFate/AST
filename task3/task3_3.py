import random

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
def test_insert_index_exception(make_dyn_array, values, pos):
    arr = make_dyn_array(values)
    with pytest.raises(IndexError):
        arr.insert(pos, 0)
    assert arr == make_dyn_array(values)

@pytest.mark.parametrize("values, pos", [
    ([], -1),
    ([], 1),
    ([], 0),
    ([1, 2, 4], -10),
    ([1, 2, 4], 3),
    ([1, 2, 4], 4),
    ([1, 2, 4], 100)
])
def test_delete_index_exception(make_dyn_array, values, pos):
    arr = make_dyn_array(values)
    with pytest.raises(IndexError):
        arr.delete(pos)
    assert arr == make_dyn_array(values)

@pytest.mark.parametrize("size, expected_size", [
    (16, 32),
    (32, 64),
    (1024, 2048),
    (0, 16),
    (1, 16),
    (5, 16),
    (15, 16)
])
def test_insert_buffer(make_rand_dyn_array, size, expected_size):
    arr = make_rand_dyn_array(size)
    arr.insert(size, 0)
    assert arr.capacity == expected_size

@pytest.mark.parametrize("size, empty_size, expected_size", [
    (16, 16, 21),
    (17, 15, 32),
    (2, 14, 16),
    (128, 0, 128),
    (128, 128, 170),
    (25, 50, 50),
    (26, 50, 50),
    (27, 50, 51)
])
def test_delete_buffer(make_rand_dyn_array, size, empty_size, expected_size):
    arr = make_rand_dyn_array(size)
    if size + empty_size != arr.capacity:
        arr.resize(size + empty_size)
    arr.delete(random.randint(0, size - 1))
    assert arr.capacity == expected_size

