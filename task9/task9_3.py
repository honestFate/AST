import pytest
from task9_2 import BitStringDictionary, OrderedListDictionary


@pytest.mark.parametrize("key, value", [
    ("key1", "value1"),
    ("ключ 23", 512),
    ("", 0),
    ("a", -1),
    ("z" * 50, [1, 2, 3]),
])
def test_put_new_key(make_native_dictionary, key, value):
    table = make_native_dictionary()
    table.put(key, value)
    assert table.is_key(key)
    assert table.get(key) == value


def test_put_existing_key_overwrites(make_native_dictionary):
    table = make_native_dictionary()
    table.put("token", 1)
    assert table.get("token") == 1
    table.put("token", 1024)
    assert table.get("token") == 1024
    assert table.is_key("token")


@pytest.mark.parametrize("present, absent", [
    (["one", "two", "three"], "four"),
    (["a"], "b"),
    ([], "missing"),
])
def test_is_key_present_and_absent(make_native_dictionary, present, absent):
    table = make_native_dictionary()
    for index, key in enumerate(present):
        table.put(key, index)
    for key in present:
        assert table.is_key(key) is True
    assert table.is_key(absent) is False


def test_get_missing_returns_none(make_native_dictionary):
    table = make_native_dictionary(items=[("present", 100)])
    assert table.get("present") == 100
    assert table.get("absent") is None


@pytest.mark.parametrize("v1, v2", [
    ("ab", "ba"),
    ("ad", "da"),
    ("listen", "silent"),
])
def test_collision_keys_independent(make_native_dictionary, v1, v2):
    table = make_native_dictionary()
    assert table.hash_fun(v1) == table.hash_fun(v2)
    table.put(v1, 1)
    table.put(v2, 2)
    assert table.get(v1) == 1
    assert table.get(v2) == 2
    assert table.is_key(v1)
    assert table.is_key(v2)


@pytest.mark.parametrize("key", ["", "a", "abc", "hello", "z" * 50])
def test_hash_fun_in_range(make_native_dictionary, key):
    table = make_native_dictionary()
    assert 0 <= table.hash_fun(key) < table.size


def test_ordered_put_get_and_order():
    d = OrderedListDictionary()
    for key, value in [("banana", 2), ("apple", 1), ("cherry", 3)]:
        d.put(key, value)
    assert d.get("apple") == 1
    assert d.get("banana") == 2
    assert d.get("cherry") == 3
    assert d.keys == ["apple", "banana", "cherry"]


def test_ordered_overwrite():
    d = OrderedListDictionary()
    d.put("x", 1)
    d.put("x", 2)
    assert d.get("x") == 2
    assert d.keys == ["x"]


def test_ordered_is_key_and_missing():
    d = OrderedListDictionary()
    d.put("present", 1)
    assert d.is_key("present") is True
    assert d.is_key("absent") is False
    assert d.get("absent") is None


def test_ordered_delete():
    d = OrderedListDictionary()
    for key, value in [("a", 1), ("b", 2), ("c", 3)]:
        d.put(key, value)
    assert d.delete("b") is True
    assert d.is_key("b") is False
    assert d.keys == ["a", "c"]
    assert d.delete("b") is False


@pytest.mark.parametrize("key, value", [
    ("000", 0),
    ("101", "five"),
    ("111", [7]),
])
def test_bitstring_put_get(key, value):
    d = BitStringDictionary(3)
    d.put(key, value)
    assert d.is_key(key)
    assert d.get(key) == value


def test_bitstring_index_mapping():
    d = BitStringDictionary(4)
    assert d._index("0000") == 0
    assert d._index("0001") == 1
    assert d._index("1010") == 10
    assert d._index("1111") == 15


def test_bitstring_overwrite_and_missing():
    d = BitStringDictionary(2)
    d.put("01", "a")
    d.put("01", "b")
    assert d.get("01") == "b"
    assert d.get("10") is None
    assert d.is_key("11") is False


def test_bitstring_delete():
    d = BitStringDictionary(3)
    d.put("011", 99)
    assert d.delete("011") is True
    assert d.is_key("011") is False
    assert d.get("011") is None
    assert d.delete("011") is False

