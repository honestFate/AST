import random
from itertools import product

import pytest
from task3_2 import MdDynArray


def delete_until_shrink(arr):
    n = 0
    cap_before = arr.capacity
    while True:
        if arr.capacity <= arr.min_capacity:
            return n
        arr.delete(arr.count - 1)
        n += 1
        assert arr._credits >= 0
        if arr.capacity != cap_before:
            return n

def append_until_expand(arr):
    n = 0
    cap_before = arr.capacity
    while True:
        arr.append(0)
        n += 1
        assert arr._credits >= 0
        if arr.capacity != cap_before:
            return n

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

def test_credits_only_appends(banker_array):
    for _ in range(10_000):
        banker_array.append(0)
        assert banker_array._credits >= 0

def test_credits_only_deletes(banker_array):
    for _ in range(10_000):
        banker_array.append(0)

    while banker_array.count > 0:
        banker_array.delete(banker_array.count - 1)
        assert banker_array._credits >= 0

@pytest.mark.parametrize("initial_size", [32, 64, 256, 1024, 4096])
def test_credits_worst_case_oscillation(banker_array, initial_size):
    for _ in range(initial_size):
        banker_array.append(0)
        assert banker_array._credits >= 0

    for _ in range(20):
        deletes = delete_until_shrink(banker_array)
        appends = append_until_expand(banker_array)

        assert deletes > 0
        assert appends > 0

@pytest.mark.parametrize("dims", [
    [1],
    [5],
    [2, 3],
    [3, 4, 2],
    [2, 2, 2, 2],
])
def test_mdim_len(dims):
    arr = MdDynArray(dims)
    assert len(arr) == dims[0]

@pytest.mark.parametrize("dims, fill", [
    ([1], 0),
    ([5], None),
    ([2, 3], 7),
    ([2, 3, 4], -1),
    ([1, 1, 1, 1], "x"),
])
def test_mdim_fill(dims, fill):
    arr = MdDynArray(dims, fill=fill)
    for idx in product(*[range(d) for d in dims]):
        assert arr[idx] == fill

@pytest.mark.parametrize("dims", [
    [5],
    [2, 3],
    [3, 4, 2],
    [2, 2, 2, 2],
])
def test_mdim_set_then_get(dims):
    arr = MdDynArray(dims, fill=0)
    setted = {}
    for i, idx in enumerate(product(*[range(d) for d in dims])):
        arr[idx] = i * 10 + 1
        setted[idx] = i * 10 + 1
    for idx, val in setted.items():
        assert arr[idx] == val


def test_ndim_1d_accepts_int_and_tuple_key():
    arr = MdDynArray([5], fill=0)
    arr[2] = 42
    assert arr[2] == 42
    assert arr[(2,)] == 42
    arr[(3,)] = 99
    assert arr[3] == 99


def test_ndim_rows_are_independent():
    arr = MdDynArray([3, 3], fill=0)
    arr[0, 0] = 1
    arr[1, 1] = 2
    arr[2, 2] = 3
    assert arr[0, 0] == 1
    assert arr[1, 1] == 2
    assert arr[2, 2] == 3
    assert arr[0, 1] == 0
    assert arr[1, 0] == 0
    assert arr[2, 0] == 0


def test_mdim_subarray():
    arr = MdDynArray([2, 3, 4], fill=0)
    arr[1, 2, 3] = 42
    sub = arr[1]
    assert isinstance(sub, MdDynArray)
    assert len(sub) == 3
    assert sub[2, 3] == 42

    sub2 = arr[1, 2]
    assert isinstance(sub2, MdDynArray)
    assert len(sub2) == 4
    assert sub2[3] == 42


@pytest.mark.parametrize("dims, key", [
    ([5], 5),
    ([5], -1),
    ([5], 100),
    ([3, 4], (3, 0)),
    ([3, 4], (0, 4)),
    ([3, 4], (-1, 0)),
    ([3, 4], (0, -1)),
    ([2, 3, 4], (2, 0, 0)),
    ([2, 3, 4], (0, 3, 0)),
    ([2, 3, 4], (0, 0, 4)),
    ([2, 3, 4], (0, 0, -1)),
])
def test_mdim_getitem_index_exception(dims, key):
    arr = MdDynArray(dims, fill=0)
    with pytest.raises(IndexError):
        _ = arr[key]

@pytest.mark.parametrize("dims, key", [
    ([5], 5),
    ([5], -1),
    ([3, 4], (3, 0)),
    ([3, 4], (0, 4)),
    ([2, 3, 4], (2, 0, 0)),
    ([2, 3, 4], (0, 0, -1)),
])
def test_mdim_setitem_index_exception(dims, key):
    arr = MdDynArray(dims, fill=0)
    with pytest.raises(IndexError):
        arr[key] = 0
    for idx in product(*[range(d) for d in dims]):
        assert arr[idx] == 0

def test_mdim_capacity():
    arr = MdDynArray([3, 3], fill=0)
    leaf = arr._data[0]._data
    assert leaf.capacity == leaf.min_capacity
    assert leaf.count == 3

