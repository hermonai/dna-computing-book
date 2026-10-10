from pathlib import Path
import importlib.util
import sys
import json
import pytest
from collections import Counter
from itertools import permutations
import math

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "ch12_reference_tests", ROOT / "drafts/ch12/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_literal_trace_and_independent_path_oracle():
    kept, trace = m.filter_trace(
        m.walks(m.VERTICES, m.EDGES, 5), m.VERTICES, "A", "D"
    )
    oracle = {
        p
        for p in permutations(m.VERTICES)
        if p[0] == "A"
        and p[-1] == "D"
        and all(e in m.EDGES for e in zip(p, p[1:]))
    }
    assert set(kept) == oracle == {tuple("ABCD"), tuple("ACBD")}
    assert [v["copies"] for v in trace] == [34, 6, 2, 2, 2, 2, 2]


def test_filters_preserve_multiplicity_and_do_not_invent():
    pool = Counter({tuple("ABCD"): 7, tuple("ABD"): 2})
    kept, _ = m.filter_trace(pool, m.VERTICES, "A", "D")
    assert kept == {tuple("ABCD"): 7}
    assert pool[tuple("ABD")] == 2


def test_invalid_generator_is_detected_only_by_independent_verifier():
    invalid = tuple("ABDC")
    # Match the requested endpoints to expose missing adjacency verification.
    kept, _ = m.filter_trace(Counter({invalid: 1}), m.VERTICES, "A", "C")
    assert invalid in kept
    assert not m.verify(invalid, m.VERTICES, m.EDGES, "A", "C")


def test_bounded_generation_can_miss_real_witnesses():
    kept, _ = m.filter_trace(
        m.walks(m.VERTICES, m.EDGES, 3), m.VERTICES, "A", "D"
    )
    assert not kept
    assert m.verify(tuple("ABCD"), m.VERTICES, m.EDGES, "A", "D")


@pytest.mark.parametrize("p", ["ABBD", "ABD", "DBCA", "ABDC", "AXCD"])
def test_verifier_rejects_wrong_certificates(p):
    assert not m.verify(tuple(p), m.VERTICES, m.EDGES, "A", "D")


def test_exact_filters_commute():
    p = m.walks(m.VERTICES, m.EDGES, 5)
    f = lambda q: "B" in q
    g = lambda q: len(q) == 4
    assert m.retain(m.retain(p, f), g) == m.retain(m.retain(p, g), f)


def test_capacity_breaks_commutativity():
    assert m.results()["order"] == {"F_then_G": [], "G_then_F": ["good"]}


def test_retention_expected_counts_and_fixed_diagonal_commutation():
    n = [10, 10000]
    a = [0.8, 0.01]
    b = [0.7, 0.1]
    assert m.expected_pass(n, a) == [8, 100]
    assert m.expected_pass(m.expected_pass(n, a), b) == pytest.approx(
        m.expected_pass(m.expected_pass(n, b), a)
    )


@pytest.mark.parametrize(
    "n,q", [(0, 0.2), (1, 0.2), (10, 0.2), (7, 0), (7, 1)]
)
def test_detection_formula_against_binomial_zero_term(n, q):
    assert m.detect_probability(n, q) == pytest.approx(1 - (1 - q) ** n)


def test_tiny_detection_avoids_cancellation():
    assert m.detect_probability(100, 1e-20) == pytest.approx(
        1e-18, rel=1e-12, abs=0
    )


@pytest.mark.parametrize("n,p", [(-1, 0.5), (1, 1.1), (2, float("nan"))])
def test_invalid_detection_inputs(n, p):
    with pytest.raises(ValueError):
        m.detect_probability(n, p)


def test_generated_results():
    assert m.results() == json.loads(
        (ROOT / "drafts/ch12/results.json").read_text()
    )
