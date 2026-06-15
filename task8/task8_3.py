import pytest
from task8_2 import (
    DynamicHashTable,
    MultiHashTable,
    SaltedHashTable,
    ddos_flood,
    make_collision_keys,
)

from task8 import HashTable


@pytest.mark.parametrize("value", ["", "a", "abc", "hello", "z" * 50])
def test_hash_fun_in_range(make_hash_table, value):
    table = make_hash_table(sz=17, stp=3)
    assert 0 <= table.hash_fun(value) < 17


@pytest.mark.parametrize("v1, v2", [
    ("ab", "ba"),
    ("ad", "da"),
    ("abc", "cba"),
])
def test_collision_stored_in_different_slots(make_hash_table, v1, v2):
    table = make_hash_table(sz=17, stp=3)
    i1 = table.put(v1)
    i2 = table.put(v2)
    assert i1 != i2
    assert table.find(v1) == i1
    assert table.find(v2) == i2


def test_put_find_roundtrip(make_hash_table):
    values = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    table = make_hash_table(sz=17, stp=3)
    placed = {value: table.put(value) for value in values}
    for value, index in placed.items():
        assert index is not None
        assert table.find(value) == index


def test_find_missing_returns_none(make_hash_table):
    table = make_hash_table(values=["one", "two"], sz=17, stp=3)
    assert table.find("three") is None


def test_repeated_put_keeps_one_slot(make_hash_table):
    table = make_hash_table(sz=17, stp=3)
    first = table.put("token")
    second = table.put("token")
    assert first == second


def test_full_table_put_returns_none(make_hash_table):
    table = make_hash_table(values=["a", "b", "c", "d", "e"], sz=5, stp=1)
    assert table.put("f") is None
    assert table.seek_slot("f") is None


def test_dynamic_grows_and_keeps_values():
    table = DynamicHashTable(sz=5, stp=1)
    initial = table.size
    keys = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for key in keys:
        table.put(key)
    assert table.size > initial
    assert table.count == len(keys)
    for key in keys:
        assert table.find(key) is not None


def test_dynamic_load_factor_respected():
    table = DynamicHashTable(sz=7, stp=3, load_factor=0.75)
    for key in ["a", "b", "c", "d", "e", "f"]:
        table.put(key)
    assert table.count / table.size <= 0.75


def test_multi_bases_are_valid():
    table = MultiHashTable(17, hash_count=4)
    assert len(table.bases) == 4
    assert len(set(table.bases)) == 4
    assert all(2 <= base < table.size for base in table.bases)


def test_multi_roundtrip():
    table = MultiHashTable(17, hash_count=4)
    keys = ["one", "two", "three", "four", "five"]
    placed = {}
    for key in keys:
        index = table.put(key)
        if index is not None:
            placed[key] = index
    assert placed
    for key, index in placed.items():
        assert table.find(key) == index


def test_multi_find_missing():
    table = MultiHashTable(17, hash_count=3)
    table.put("present")
    assert table.find("absent") is None


def test_multi_full_returns_none():
    table = MultiHashTable(5, hash_count=2)
    results = [table.put(char) for char in "abcdefghij"]
    assert None in results


def test_collision_attack_collapses_to_one_slot():
    keys = make_collision_keys(20)
    table = HashTable(17, 3)
    slots = {table.hash_fun(key) for key in keys}
    assert len(slots) == 1


def test_ddos_degrades_plain_table():
    keys = make_collision_keys(40)
    table = HashTable(101, 3)
    n = len(keys)
    assert ddos_flood(table, keys) == n * (n + 1) // 2


def test_salt_neutralizes_ddos():
    keys = make_collision_keys(40)
    plain_cost = ddos_flood(HashTable(101, 3), keys)
    salted_cost = ddos_flood(SaltedHashTable(101, 3, salt=5), keys)
    assert salted_cost < plain_cost
    assert salted_cost <= 2 * len(keys)


def test_salt_spreads_attack_keys():
    keys = make_collision_keys(20)
    salted = SaltedHashTable(101, 7, salt=5)
    slots = {salted.hash_fun(key) for key in keys}
    assert len(slots) > 1


def test_salted_table_roundtrip():
    keys = make_collision_keys(20)
    salted = SaltedHashTable(101, 7, salt=5)
    for key in keys:
        assert salted.put(key) is not None
    for key in keys:
        assert salted.find(key) is not None


def test_salted_find_missing():
    salted = SaltedHashTable(101, 7, salt=5)
    salted.put("present")
    assert salted.find("absent") is None

