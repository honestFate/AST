import pytest
from task7_2 import merge_ordered_lists

from task7 import OrderedList, OrderedStringList


def check_integrity(ordered, expected):
    forward = [node.value for node in ordered.get_all()]
    assert forward == expected
    if not expected:
        assert ordered.head is None
        assert ordered.tail is None
        return
    assert ordered.head is not None
    assert ordered.tail is not None
    assert ordered.head.prev is None
    assert ordered.tail.next is None
    assert ordered.head.value == expected[0]
    assert ordered.tail.value == expected[-1]
    backward = []
    node = ordered.tail
    while node is not None:
        backward.append(node.value)
        node = node.prev
    assert backward == expected[::-1]


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1),
    (2, 1, 1),
    (2, 2, 0),
    (-5, -1, -1),
])
def test_compare_numeric(a, b, expected):
    assert OrderedList(True).compare(a, b) == expected


@pytest.mark.parametrize("values, asc, expected", [
    ([], True, []),
    ([1], True, [1]),
    ([3, 1, 2], True, [1, 2, 3]),
    ([3, 1, 2], False, [3, 2, 1]),
    ([5, 5, 5], True, [5, 5, 5]),
    ([2, 1, 2, 1, 3], True, [1, 1, 2, 2, 3]),
    ([2, 1, 2, 1, 3], False, [3, 2, 2, 1, 1]),
    ([-1, 0, -5, 3], True, [-5, -1, 0, 3]),
    ([-1, 0, -5, 3], False, [3, 0, -1, -5]),
])
def test_add(make_ordered_list, values, asc, expected):
    ordered = make_ordered_list(values, asc)
    check_integrity(ordered, expected)


@pytest.mark.parametrize("values, asc, target, found", [
    ([1, 2, 3], True, 2, True),
    ([1, 2, 3], True, 4, False),
    ([1, 2, 3], True, 0, False),
    ([3, 2, 1], False, 2, True),
    ([3, 2, 1], False, 4, False),
    ([3, 2, 1], False, 0, False),
    ([], True, 1, False),
    ([1, 1, 2, 3], True, 1, True),
    ([5, 3, 3, 1], False, 3, True),
])
def test_find(make_ordered_list, values, asc, target, found):
    node = make_ordered_list(values, asc).find(target)
    if found:
        assert node is not None
        assert node.value == target
    else:
        assert node is None


@pytest.mark.parametrize("values, asc, target, expected", [
    ([], True, 1, []),
    ([1], True, 1, []),
    ([1], True, 2, [1]),
    ([1, 2, 3], True, 2, [1, 3]),
    ([1, 2, 2, 3], True, 2, [1, 2, 3]),
    ([3, 2, 1], False, 2, [3, 1]),
    ([3, 2, 2, 1], False, 2, [3, 2, 1]),
    ([1, 2, 3], True, 5, [1, 2, 3]),
    ([1, 2, 3], True, 0, [1, 2, 3]),
])
def test_delete(make_ordered_list, values, asc, target, expected):
    ordered = make_ordered_list(values, asc)
    ordered.delete(target)
    check_integrity(ordered, expected)


@pytest.mark.parametrize("values, expected", [
    ([], 0),
    ([1], 1),
    ([3, 1, 2], 3),
    ([1, 1, 1], 3),
])
def test_len(make_ordered_list, values, expected):
    assert make_ordered_list(values).len() == expected


def test_clean_resets(make_ordered_list):
    ordered = make_ordered_list([1, 2, 3], True)
    ordered.clean(True)
    check_integrity(ordered, [])
    assert ordered.len() == 0


def test_clean_changes_direction(make_ordered_list):
    ordered = make_ordered_list([1, 2, 3], True)
    ordered.clean(False)
    for v in [1, 2, 3]:
        ordered.add(v)
    check_integrity(ordered, [3, 2, 1])


def test_string_compare_strips():
    lst = OrderedStringList(True)
    assert lst.compare("  abc ", "abc") == 0
    assert lst.compare("a", "b") == -1


@pytest.mark.parametrize("values, asc, expected", [
    (["banana", "apple", "cherry"], True, ["apple", "banana", "cherry"]),
    (["banana", "apple", "cherry"], False, ["cherry", "banana", "apple"]),
    (["  b  ", "a", " c"], True, ["a", "  b  ", " c"]),
])
def test_string_add(make_ordered_string_list, values, asc, expected):
    ordered = make_ordered_string_list(values, asc)
    assert [n.value for n in ordered.get_all()] == expected


def test_string_find_ignores_whitespace(make_ordered_string_list):
    node = make_ordered_string_list(["apple", "banana"], True).find("  apple  ")
    assert node is not None
    assert node.value == "apple"


@pytest.mark.parametrize("values, asc, expected", [
    ([], True, []),
    ([1, 1, 1], True, [1]),
    ([1, 2, 2, 3, 3, 3], True, [1, 2, 3]),
    ([1, 2, 3], True, [1, 2, 3]),
    ([3, 3, 2, 1, 1], False, [3, 2, 1]),
])
def test_remove_duplicates(make_ordered_list, values, asc, expected):
    ordered = make_ordered_list(values, asc)
    ordered.remove_duplicates()
    check_integrity(ordered, expected)


@pytest.mark.parametrize("values1, values2, asc, expected", [
    ([], [], True, []),
    ([1, 3, 5], [2, 4, 6], True, [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3], [], True, [1, 2, 3]),
    ([], [1, 2, 3], True, [1, 2, 3]),
    ([1, 2, 2], [2, 3], True, [1, 2, 2, 2, 3]),
    ([5, 3, 1], [6, 2], False, [6, 5, 3, 2, 1]),
])
def test_merge(make_ordered_list, values1, values2, asc, expected):
    first = make_ordered_list(values1, asc)
    second = make_ordered_list(values2, asc)
    merged = merge_ordered_lists(first, second)
    check_integrity(merged, expected)
    assert [n.value for n in first.get_all()] == sorted(values1, reverse=not asc)
    assert [n.value for n in second.get_all()] == sorted(values2, reverse=not asc)


def test_merge_preserves_subclass(make_ordered_string_list):
    first = make_ordered_string_list(["apple", "cherry"], True)
    second = make_ordered_string_list(["banana"], True)
    merged = merge_ordered_lists(first, second)
    assert isinstance(merged, OrderedStringList)
    assert [n.value for n in merged.get_all()] == ["apple", "banana", "cherry"]


@pytest.mark.parametrize("values, sub, asc, expected", [
    ([1, 2, 3, 4, 5], [2, 4], True, True),
    ([1, 2, 3, 4, 5], [2, 6], True, False),
    ([1, 2, 2, 3], [2, 2], True, True),
    ([1, 2, 3], [2, 2], True, False),
    ([1, 2, 3], [], True, True),
    ([5, 4, 3, 2, 1], [4, 2], False, True),
])
def test_contains_sublist(make_ordered_list, values, sub, asc, expected):
    ordered = make_ordered_list(values, asc)
    sublist = make_ordered_list(sub, asc)
    assert ordered.contains_sublist(sublist) == expected


@pytest.mark.parametrize("values, asc, expected", [
    ([], True, None),
    ([1], True, 1),
    ([1, 2, 2, 3], True, 2),
    ([1, 1, 2, 3, 3, 3], True, 3),
    ([4, 4, 2, 2], True, 2),
    ([5, 5, 5, 3, 1], False, 5),
])
def test_most_frequent(make_ordered_list, values, asc, expected):
    assert make_ordered_list(values, asc).most_frequent() == expected


@pytest.mark.parametrize("values, asc, target, expected", [
    ([10, 20, 30], True, 20, 1),
    ([10, 20, 30], True, 10, 0),
    ([10, 20, 30], True, 30, 2),
    ([10, 20, 30], True, 25, -1),
    ([10, 20, 30], True, 5, -1),
    ([30, 20, 10], False, 20, 1),
    ([1, 1, 2], True, 1, 0),
    ([], True, 1, -1),
])
def test_find_index(make_ordered_list, values, asc, target, expected):
    assert make_ordered_list(values, asc).find_index(target) == expected

