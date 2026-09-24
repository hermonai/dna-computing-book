from pathlib import Path
import importlib.util
import sys
import json
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "ch13_reference_tests", ROOT / "drafts/ch13/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)

from collections import Counter
from itertools import product, permutations
import math


def test_truth_table_trace_and_duplicate_negative_control():
    out, trace = m.solve(3, m.CNF, 7)
    assert out == Counter({(0, 1, 0): 7, (1, 0, 1): 7})
    assert [r["copies"] for r in trace] == [56, 42, 28, 14]
    assert m.results()["duplicate_bug"] == 14


@pytest.mark.parametrize(
    "clauses",
    list(product(list(product((1, -1, 2, -2), repeat=2)), repeat=2)),
)
def test_all_two_clause_formulas_match_independent_oracle(clauses):
    out, _ = m.solve(2, clauses, 3)
    assert sorted(out) == m.oracle(2, clauses)
    assert all(v == 3 for v in out.values())


def test_partition_conserves_nonuniform_counts_and_is_disjoint():
    pool = Counter(
        {a: i + 1 for i, a in enumerate(product((0, 1), repeat=3))}
    )
    before = pool.copy()
    for clause in [(1, 2, 3), (1, 1), (-1, 1), (), (-2, 3)]:
        yes, no, branches = m.clause_partition(pool, clause)
        assert yes + no == pool and not (yes.keys() & no.keys())
        assert sum(branches) == sum(yes.values())
    assert pool == before


def test_clause_order_invariance():
    expected, _ = m.solve(3, m.CNF)
    for clauses in permutations(m.CNF):
        assert m.solve(3, clauses)[0] == expected


def test_degenerate_formulas():
    assert m.solve(0, ())[0] == Counter({(): 1})
    assert not m.solve(0, ((),))[0]
    assert len(m.solve(2, ())[0]) == 4
    assert not m.solve(2, ((1,), (-1,)))[0]
    assert len(m.solve(2, ((1, -1),))[0]) == 4
    assert not m.solve(2, (), 0)[0]


@pytest.mark.parametrize(
    "args", [(-1, ()), (2, ((0,),)), (2, ((3,),)), (2, ((True,),))]
)
def test_invalid_formula(args):
    with pytest.raises(ValueError):
        m.solve(*args)


def test_probability_independent_binomial_oracle():
    n, M, s, q = 3, 7, 2, 0.5
    u = s * q / 2**n
    direct = sum(
        math.comb(M, k) * u**k * (1 - u) ** (M - k) for k in range(1, M + 1)
    )
    assert m.witness_probability(n, M, s, q) == pytest.approx(direct)
    assert m.witness_probability(0, 1) == 1
    assert m.witness_probability(0, 0) == 0
    assert m.witness_probability(10, 100, 0) == 0
    assert m.witness_probability(10, 100, 1, 0) == 0
    assert m.witness_probability(40, 1) == pytest.approx(
        2**-40, rel=1e-14, abs=0
    )


@pytest.mark.parametrize(
    "args", [(2, -1), (2, 1, 5), (2, 1, 1, float("nan")), (2, 1, 1, 1.1)]
)
def test_probability_rejects_invalid(args):
    with pytest.raises(ValueError):
        m.witness_probability(*args)


def test_committed_result_artifact_matches_execution():
    assert (
        json.loads((ROOT / "drafts/ch13/results.json").read_text())
        == m.results()
    )
