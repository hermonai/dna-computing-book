from pathlib import Path
import importlib.util
import sys
import json
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "ch14_reference_tests", ROOT / "drafts/ch14/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)

from collections import Counter
from itertools import permutations


@pytest.mark.parametrize("width", range(1, 6))
def test_write_matches_tuple_oracle_and_conserves_inventory(width):
    pool = Counter({s: s + 1 for s in range(2**width)})
    for bit in range(width):
        for value in (0, 1):
            expected = Counter()
            for s, n in pool.items():
                bits = [(s >> i) & 1 for i in range(width)]
                bits[bit] = value
                expected[sum(b * 2**i for i, b in enumerate(bits))] += n
            actual = m.write(pool, bit, value, width)
            assert actual == expected
            assert sum(actual.values()) == sum(pool.values())
            assert m.write(actual, bit, value, width) == actual


@pytest.mark.parametrize("roles", list(permutations(range(3))))
def test_and_all_initial_registers_all_address_permutations(roles):
    a, b, c = roles
    pool = Counter({s: s + 1 for s in range(8)})
    expected = Counter()
    for s, n in pool.items():
        bits = [(s >> i) & 1 for i in range(3)]
        bits[c] = bits[a] & bits[b]
        expected[sum(v * 2**i for i, v in enumerate(bits))] += n
    assert m.and_gate(pool, a, b, c, 3) == expected
    assert pool == Counter({s: s + 1 for s in range(8)})


def test_clear_merges_counts_not_overwrites():
    assert m.write(Counter({0: 3, 4: 5}), 2, 0, 3) == Counter({0: 8})
    assert m.write(Counter(), 0, 1, 1) == Counter()


def test_separation_partition():
    pool = Counter({s: s + 1 for s in range(16)})
    for i in range(4):
        on, off = m.separate(pool, i, 4)
        assert on + off == pool
        assert not (on.keys() & off.keys())


def test_write_order_and_alias_negative_controls():
    start = Counter({0: 1})
    assert m.write(m.write(start, 0, 0, 2), 0, 1, 2) != m.write(
        m.write(start, 0, 1, 2), 0, 0, 2
    )
    assert m.write(m.write(start, 0, 1, 2), 1, 0, 2) == m.write(
        m.write(start, 1, 0, 2), 0, 1, 2
    )
    with pytest.raises(ValueError):
        m.and_gate(Counter({3: 1}), 0, 1, 0, 2)


@pytest.mark.parametrize(
    "pool,width,bit,value",
    [
        (Counter({-1: 1}), 2, 0, 0),
        (Counter({4: 1}), 2, 0, 0),
        (Counter({0: -1}), 2, 0, 0),
        (Counter({0: 1}), 2, 2, 0),
        (Counter({0: 1}), 2, 0, 2),
        (Counter({0: 1}), 0, 0, 0),
    ],
)
def test_invalid_operations(pool, width, bit, value):
    with pytest.raises(ValueError):
        m.write(pool, bit, value, width)


def test_retention_and_markov_stationarity():
    assert m.retained(0, 0) == 1
    assert m.retained(100, 0.99) == pytest.approx(0.3660323412732292)
    p0, p1 = 0.8, 0.2
    assert p0 * 0.98 + p1 * 0.08 == pytest.approx(p0)
    assert p0 * 0.02 + p1 * 0.92 == pytest.approx(p1)
    for k, p in [(-1, 0.9), (1, float("nan")), (1, 1.1)]:
        with pytest.raises(ValueError):
            m.retained(k, p)


def test_committed_result_artifact_matches_execution():
    assert (
        json.loads((ROOT / "drafts/ch14/results.json").read_text())
        == m.results()
    )
