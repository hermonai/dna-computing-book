import importlib.util
import pytest
from pathlib import Path

P = Path(__file__).parents[1] / "drafts/ch23/reference.py"
s = importlib.util.spec_from_file_location("r", P)
r = importlib.util.module_from_spec(s)
s.loader.exec_module(r)


def test_repetition_one_is_raw_error():
    assert abs(r.majority_failure(0.07, 1) - 0.07) < 1e-15


def test_repetition_reduces_iid_error_below_half():
    assert r.majority_failure(0.01, 5) < r.majority_failure(0.01, 3) < 0.01


def test_closed_form_three():
    p = 0.13
    assert abs(r.majority_failure(p, 3) - (3 * p * p * (1 - p) + p**3)) < 1e-15


def test_simulation_is_independent_oracle():
    exact = r.majority_failure(0.02, 5)
    sim = r.simulate_repetition(0.02, 5, 80000, 8)
    assert abs(sim - exact) < 0.001


def test_yield_limits():
    assert r.object_yield_independent(0, 100) == 1
    assert r.object_yield_independent(1, 1) == 0


def test_positive_correlation_changes_object_yield():
    # Correlation invalidates simply substituting mean p into the IID law.
    iid = r.object_yield_independent(0.01, 100)
    corr = r.all_correct_beta_binomial(100, 0.99, 98.01)
    assert abs(corr - iid) > 0.01


def test_wilson_contains_observed_fraction():
    lo, hi = r.wilson(10, 1000)
    assert lo < 0.01 < hi


@pytest.mark.parametrize("n", [0, 1, 5, 20])
def test_beta_uniform_count_oracle(n):
    # Integrating q^k(1-q)^(n-k) over Uniform(0,1) gives 1/(n+1).
    values = [r.beta_binomial_pmf(k, n, 1, 1) for k in range(n + 1)]
    assert values == pytest.approx([1 / (n + 1)] * (n + 1), abs=2e-14)
    assert sum(values) == pytest.approx(1)
    assert r.all_correct_beta_binomial(n, 1, 1) == pytest.approx(1 / (n + 1))


@pytest.mark.parametrize("copies", [1, 3, 5, 7, 9])
def test_majority_endpoints_symmetry(copies):
    assert r.majority_failure(0, copies) == 0
    assert r.majority_failure(1, copies) == 1
    assert r.majority_failure(0.5, copies) == pytest.approx(0.5)
    assert r.majority_failure(0.27, copies) + r.majority_failure(
        0.73, copies
    ) == pytest.approx(1)
    assert r.correlated_majority_failure(copies, 1, 1) == pytest.approx(0.5)


@pytest.mark.parametrize("p", [-0.1, 1.1, float("nan"), float("inf"), True])
def test_invalid_probability(p):
    with pytest.raises(ValueError):
        r.object_yield_independent(p, 10)
    with pytest.raises(ValueError):
        r.majority_failure(p, 3)


@pytest.mark.parametrize("n", [-1, 0.5, True])
def test_invalid_count(n):
    with pytest.raises(ValueError):
        r.object_yield_independent(0.1, n)
    with pytest.raises(ValueError):
        r.wilson(0, n)


def test_wilson_zero_defect_is_not_zero_uncertainty():
    lo, hi = r.wilson(0, 20)
    assert lo == 0 and hi == pytest.approx(1.96**2 / (20 + 1.96**2))
    assert r.wilson(20, 20)[1] == 1
    with pytest.raises(ValueError):
        r.wilson(21, 20)
    with pytest.raises(ValueError):
        r.wilson(1, 20, 0)


def test_measurement_channel_roundtrip_and_nonidentifiability():
    for p in (0, 0.01, 0.4, 1):
        obs = r.observed_defect_probability(p, 0.02, 0.1)
        assert r.infer_defect_probability(obs, 0.02, 0.1) == pytest.approx(p)
    assert r.observed_defect_probability(0.01, 0.02, 0.1) == pytest.approx(0.0288)
    with pytest.raises(ValueError):
        r.infer_defect_probability(0.5, 0.5, 0.5)
    with pytest.raises(ValueError):
        r.infer_defect_probability(0, 0.02, 0.1)


def test_correlated_repetition_is_not_iid_substitution():
    assert r.correlated_majority_failure(5, 0.99, 98.01) > r.majority_failure(0.01, 5)
    # Perfect common-mode errors leave logical failure p, regardless of copies.
    assert r.yield_bounds(0.01, 100) == pytest.approx((0, 0.99))
    assert r.yield_bounds(0.01, 0) == (1, 1)


def test_probability_model_rejects_invalid_beta_and_trials():
    for a, b in ((0, 1), (1, 0), (float("inf"), 1)):
        with pytest.raises(ValueError):
            r.all_correct_beta_binomial(10, a, b)
    with pytest.raises(ValueError):
        r.beta_binomial_pmf(11, 10, 1, 1)
    with pytest.raises(ValueError):
        r.simulate_repetition(0.1, 3, 0)


def test_extreme_beta_ratio_does_not_round_to_illegal_log():
    assert r.all_correct_beta_binomial(1, 1e30, 1) == pytest.approx(1e-30)


def test_amplification_odds_identity_and_limits():
    f = 0.1
    n = 20
    p = r.amplification_fraction(f, 2, 1.8, n)
    assert p / (1 - p) == pytest.approx(f / (1 - f) * (2 / 1.8) ** n)
    assert r.amplification_fraction(f, 2, 2, n) == pytest.approx(f)
    assert r.amplification_fraction(f, 2, 1.8, 0) == pytest.approx(f)
    assert r.amplification_fraction(0, 2, 1.8, n) == 0
    assert r.amplification_fraction(1, 2, 1.8, n) == 1
    assert r.amplification_fraction(0.5, 2, 1, 100000) == 1
    assert r.amplification_fraction(0.5, 1, 2, 100000) == 0
    with pytest.raises(ValueError):
        r.amplification_fraction(0.1, 0, 1, 20)
