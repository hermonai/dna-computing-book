import importlib.util
import json
import math
from collections import Counter
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna_ch09", ROOT / "drafts/ch09/reference.py"
)
ref = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ref)


def test_primer_polarity():
    assert ref.primer_pair("TTACGATCGTACGG", 2, 12, 3, 3) == (
        "ACG",
        "GTA",
        "ACGATCGTAC",
    )
    with pytest.raises(ValueError):
        ref.primer_pair("ACGT", 0, 4, 3, 3)


def test_lineage_by_independent_endpoint_enumeration():
    # Each tuple is (left coordinate, right coordinate, 5'-to-3' sign).
    strands = [(0, 14, 1), (0, 14, -1)]
    for expected in ref.lineage(6):
        n = expected["cycle"]
        assert len(strands) == 2 ** (n + 1)
        exact = sum(a == 2 and b == 12 for a, b, _ in strands)
        assert exact == expected["exact"]
        assert expected["original"] + expected["one_end"] + exact == len(
            strands
        )
        if n:
            assert expected["exact"] == 2 ** (n + 1) - 2 * n - 2
            assert expected["exact_duplexes"] == 2**n - 2 * n
        children = [
            (a, 12, -1) if sign == 1 else (2, b, 1)
            for a, b, sign in strands
        ]
        strands += children


def test_cycle_two_is_not_exact_duplex():
    assert ref.lineage(2)[2]["exact"] == 2
    assert ref.lineage(2)[2]["exact_duplexes"] == 0
    assert ref.lineage(3)[3]["exact_duplexes"] == 2


@pytest.mark.parametrize("e", [0, 0.2, 0.7, 1])
def test_amplification_product(e):
    assert ref.amplify(3, [e] * 6)[-1] == pytest.approx(3 * (1 + e) ** 6)
    assert ref.amplify(0, [e] * 3) == [0] * 4


def test_variable_efficiency_not_arithmetic_average():
    assert ref.amplify(10, [1, 0])[-1] == 20
    assert ref.amplify(10, [0.5, 0.5])[-1] == 22.5


@pytest.mark.parametrize(
    "f,r,b",
    [
        (90, 120, 1400),
        (0, 50, 100),
        (100, 0, 10),
        (100, 100, 0),
        (100, 100, 35),
    ],
)
def test_budget_invariants(f, r, b):
    rows = ref.budgeted(10, [1] * 8, f, r, b, 10, 3, 3)
    for row in rows:
        added = row["n"] - 10
        assert row["forward"] + added == pytest.approx(f)
        assert row["reverse"] + added == pytest.approx(r)
        assert row["dntp"] + 14 * added == pytest.approx(b)
        assert min(row[k] for k in ("n", "forward", "reverse", "dntp")) >= 0
        assert added <= min(f, r, b / 14) + 1e-12


def test_budget_plateau_and_mean_counts():
    assert (
        ref.budgeted(10, [1] * 5, 90, 120, 1400, 10, 3, 3)[-1]["n"] == 100
    )
    assert (
        ref.budgeted(10, [1] * 5, 100, 100, 35, 10, 3, 3)[-1]["n"] == 12.5
    )


def test_branching_moments_by_exact_distribution():
    distribution = {1: 1.0}
    for mean, variance in ref.branching_moments(1, 0, [0.5] * 4):
        m = sum(n * p for n, p in distribution.items())
        v = sum((n - m) ** 2 * p for n, p in distribution.items())
        assert mean == pytest.approx(m)
        assert variance == pytest.approx(v)
        new = Counter()
        for n, p in distribution.items():
            for k in range(n + 1):
                new[n + k] += p * math.comb(n, k) * 0.5**n
        distribution = new


def test_threshold_inverse_and_gain_nonidentifiability():
    assert ref.cq(100, 1, 102400) == 10
    assert ref.cq(400, 1, 102400) == 8
    assert ref.cq(50, 1, 102400, gain=2) == 10
    assert ref.cq(0, 1, 102400) is None
    assert ref.cq(10, 0, 102400) is None
    assert ref.cq(102400, 0, 102400) == 0


def test_slope_and_sampling():
    assert ref.efficiency_from_slope(
        -math.log(10) / math.log(2)
    ) == pytest.approx(1)
    assert ref.efficiency_from_slope(-4) == pytest.approx(10**0.25 - 1)
    assert ref.empty_probability(0) == 1
    assert ref.empty_probability(3) == pytest.approx(math.exp(-3))
    with pytest.raises(ValueError):
        ref.efficiency_from_slope(-1)


@pytest.mark.parametrize("bad", [-0.1, 1.1, math.nan, math.inf])
def test_invalid_efficiency(bad):
    with pytest.raises(ValueError):
        ref.amplify(1, [bad])


def test_results_are_current():
    actual = json.loads(json.dumps(ref.results()))
    assert actual == json.loads(
        (ROOT / "drafts/ch09/results.json").read_text()
    )
