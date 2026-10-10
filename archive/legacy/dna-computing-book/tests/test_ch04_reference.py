"""Independent exact cases and limits of the Chapter 4 sampling model."""

import importlib.util
from pathlib import Path
from decimal import Decimal
from fractions import Fraction
from itertools import product, combinations
from math import log
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "d04", ROOT / "drafts/ch04/reference.py"
)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def test_review_record_binds_authored_sources_without_promotion():
    import hashlib
    import json
    record = json.loads((ROOT / "artifacts/deep/ch04-review.json").read_text())
    assert record["allPagesInspected"] and record["openGates"]
    assert record["figures"] == 5 and record["exercises"] == 12
    assert record["status"].endswith("no acceptance promotion")
    for path, digest in record["sources"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    accepted = json.loads((ROOT / "book/book.json").read_text())
    assert len(accepted["chapters"]) == 2


def test_local_review_pdf_matches_author_review_when_available():
    import hashlib
    import json
    record = json.loads((ROOT / "artifacts/deep/ch04-review.json").read_text())
    path = ROOT / record["pdf"]
    if not path.exists():
        pytest.skip("Review PDF is a generated, gitignored artifact")
    assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"]


def test_minimal_budget():
    assert M.required_copies(".04", ".01") == 113
    assert M.miss(112, ".04") > 0.01 >= M.miss(113, ".04")
    for p in (".1", ".25", ".5", ".9"):
        for d in (".01", ".1", ".5"):
            n = M.required_copies(p, d)
            assert M.miss(n, p) <= float(d) + 1e-15
            assert M.miss(n - 1, p) > float(d) - 1e-15


def test_uniform_coverage_by_enumerating_all_draws():
    cases = list(product(range(4), repeat=4))
    actual = sum(len(set(v)) for v in cases) / len(cases)
    assert actual == M.expected_distinct(4, 4) == 2.734375
    missing = sum(len(set(v)) < 4 for v in cases) / len(cases)
    assert missing <= M.all_species_bound(4, 4)
    assert M.all_species_bound(21, 4) < 0.01


def test_sampling_without_replacement_against_subsets():
    outcomes = list(combinations(range(10), 3))
    absent = sum(not (set(s) & {0, 1}) for s in outcomes)
    assert (
        M.finite_pool_miss(10, 2, 3)
        == Fraction(absent, len(outcomes))
        == Fraction(7, 15)
    )
    assert float(M.finite_pool_miss(10, 2, 3)) < M.miss(3, 0.2)


def test_probability_boundary_cases():
    assert M.miss(0, 1) == 1
    assert M.miss(10, 0) == 1
    assert M.miss(10, 1) == 0
    assert M.required_copies(1, 0.01) == 1
    assert M.expected_distinct(0, 4) == 0
    assert M.expected_distinct(0, 1) == 0
    assert M.expected_distinct(5, 1) == 1
    assert M.finite_pool_miss(0, 0, 0) == 1
    assert M.finite_pool_miss(10, 2, 9) == 0


@pytest.mark.parametrize("p", [-0.1, 1.1, "NaN", "Infinity"])
def test_invalid_probabilities(p):
    with pytest.raises(ValueError):
        M.miss(3, p)


@pytest.mark.parametrize(
    "p,d", [(0, 0.01), (".0001", 0), (".1", 1), ("1e-60", ".01")]
)
def test_unattainable_or_unsupported_budget(p, d):
    with pytest.raises(ValueError):
        M.required_copies(p, d)


@pytest.mark.parametrize("n", [-1, True, 1.5])
def test_invalid_copy_count(n):
    with pytest.raises(ValueError):
        M.miss(n, 0.1)


def test_large_budget_is_not_rounded_to_binary_float():
    n = M.required_copies("1e-20", ".01")
    assert isinstance(n, int) and n > 2**53
    assert M.miss(n, "1e-20") == pytest.approx(0.01, rel=1e-14)


def test_shared_failure_floor_and_degenerate_cases():
    assert M.shared_failure(0, 0.04, 0.1) == 1
    assert M.shared_failure(100000, 0.04, 0.1) == pytest.approx(0.1)
    assert M.shared_failure(100, 0.04, 0) == M.miss(100, 0.04)
    assert M.shared_failure(100, 0.04, 1) == 1


def test_inventory_dimensions_and_dilution():
    count = 602214076
    one = M.inventory(count, "1e-9")
    ten = M.inventory(count, "1e-8")
    assert one["moles"] == pytest.approx(1e-15)
    assert one["litres"] == pytest.approx(1e-6)
    assert one["litres"] == pytest.approx(10 * ten["litres"])
    assert one["grams_ssdna_approx"] == pytest.approx(
        ten["grams_ssdna_approx"]
    )
    assert M.half_time(1e6, 1e-9) == pytest.approx(log(2) * 1000)


def test_bayes_readout_is_not_sensitivity():
    assert M.positive_predictive_value(0.01, 0.9, 0.05) == pytest.approx(
        2 / 13
    )
    with pytest.raises(ValueError):
        M.positive_predictive_value(0, 0, 0)


@pytest.mark.parametrize("args", [(10, 11, 2), (10, 2, 11), (-1, 0, 0)])
def test_finite_pool_invalid(args):
    with pytest.raises(ValueError):
        M.finite_pool_miss(*args)


def test_generated_results_reproduce():
    import json

    assert (
        json.loads((ROOT / "drafts/ch04/results.json").read_text())
        == M.results()
    )


def test_precision_contract_rejects_silent_cancellation():
    with pytest.raises(ValueError):
        M.miss(10**90, "1e-90")
    with pytest.raises(ValueError):
        M.expected_distinct(100, 10**90)
