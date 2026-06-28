import pytest
from task10_2 import Bag, ProductPowerSet, intersection_many


def test_put_adds_absent_and_skips_present(make_power_set):
    power_set = make_power_set()
    power_set.put("a")
    assert power_set.size() == 1
    power_set.put("a")
    assert power_set.size() == 1
    assert power_set.get("a")


def test_get_present_and_absent(make_power_set):
    power_set = make_power_set(["x", "y"])
    assert power_set.get("x") is True
    assert power_set.get("z") is False


def test_remove(make_power_set):
    power_set = make_power_set(["a", "b"])
    assert power_set.remove("a") is True
    assert power_set.get("a") is False
    assert power_set.size() == 1
    assert power_set.remove("a") is False


@pytest.mark.parametrize("left, right, expected", [
    ([1, 2, 3], [2, 3, 4], [2, 3]),
    ([1, 2], [3, 4], []),
    ([], [1, 2], []),
])
def test_intersection(make_power_set, left, right, expected):
    result = make_power_set(left).intersection(make_power_set(right))
    assert result.size() == len(expected)
    for value in expected:
        assert result.get(value)


@pytest.mark.parametrize("left, right, expected", [
    ([1, 2], [2, 3], [1, 2, 3]),
    ([1, 2], [], [1, 2]),
    ([], [3, 4], [3, 4]),
])
def test_union(make_power_set, left, right, expected):
    result = make_power_set(left).union(make_power_set(right))
    assert result.size() == len(expected)
    for value in expected:
        assert result.get(value)


@pytest.mark.parametrize("left, right, expected", [
    ([1, 2, 3], [2, 3], [1]),
    ([1, 2], [1, 2], []),
])
def test_difference(make_power_set, left, right, expected):
    result = make_power_set(left).difference(make_power_set(right))
    assert result.size() == len(expected)
    for value in expected:
        assert result.get(value)


def test_issubset_param_inside_current(make_power_set):
    current = make_power_set([1, 2, 3])
    param = make_power_set([1, 2])
    assert current.issubset(param) is True


def test_issubset_current_inside_param(make_power_set):
    current = make_power_set([1, 2])
    param = make_power_set([1, 2, 3])
    assert current.issubset(param) is False


def test_issubset_param_not_inside_current(make_power_set):
    current = make_power_set([1, 2, 3])
    param = make_power_set([3, 4])
    assert current.issubset(param) is False


@pytest.mark.parametrize("left, right, expected", [
    ([1, 2, 3], [3, 2, 1], True),
    ([1, 2], [1, 2, 3], False),
    ([1, 2], [1, 3], False),
])
def test_equals(make_power_set, left, right, expected):
    assert make_power_set(left).equals(make_power_set(right)) is expected


def test_performance(make_power_set):
    big = make_power_set(range(20000))
    other = make_power_set(range(10000, 30000))
    assert big.size() == 20000
    assert big.intersection(other).size() == 10000
    assert big.union(other).size() == 30000
    assert big.difference(other).size() == 10000


def test_cartesian_product():
    left = ProductPowerSet()
    for value in ["a", "b"]:
        left.put(value)
    right = ProductPowerSet()
    for value in [1, 2]:
        right.put(value)
    product = left.cartesian_product(right)
    assert product.size() == 4
    for pair in [("a", 1), ("a", 2), ("b", 1), ("b", 2)]:
        assert product.get(pair)


def test_intersection_many(make_power_set):
    sets = [
        make_power_set([1, 2, 3, 4]),
        make_power_set([2, 3, 4, 5]),
        make_power_set([3, 4, 5, 6]),
    ]
    result = intersection_many(sets)
    assert result.size() == 2
    assert result.get(3)
    assert result.get(4)


def test_intersection_many_empty_result(make_power_set):
    sets = [
        make_power_set([1, 2]),
        make_power_set([2, 3]),
        make_power_set([4, 5]),
    ]
    assert intersection_many(sets).size() == 0


def test_bag_add_and_frequencies():
    bag = Bag()
    for value in ["a", "a", "b"]:
        bag.add(value)
    assert dict(bag.frequencies()) == {"a": 2, "b": 1}
    assert bag.size() == 3


def test_bag_remove_one_instance():
    bag = Bag()
    bag.add("a")
    bag.add("a")
    assert bag.remove("a") is True
    assert dict(bag.frequencies()) == {"a": 1}
    assert bag.remove("a") is True
    assert bag.remove("a") is False
    assert dict(bag.frequencies()) == {}

