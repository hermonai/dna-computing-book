"""Independent laws and deliberately broken alternatives for DNAD-28."""

import importlib.util
import math
from pathlib import Path
import random
import sys

import pytest

p = Path(__file__).parents[1] / "drafts/ch28/reference.py"
spec = importlib.util.spec_from_file_location("dna28", p)
r = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = r
spec.loader.exec_module(r)


@pytest.mark.parametrize("t", [0, 0.001, 1, 5, 100])
def test_closed_form_oracle(t):
    a0, b0, kf, kr = 17, 9, 0.4, 0.1
    equilibrium = kr * (a0 + b0) / (kf + kr)
    expected = equilibrium + (a0 - equilibrium) * math.exp(-(kf + kr) * t)
    assert r.analytic_a(t, a0, b0, kf, kr) == pytest.approx(expected, abs=1e-13)


def test_zero_rates_and_stable_small_time():
    assert r.analytic_a(10, 7, 3, 0, 0) == 7
    assert r.exact_moments(7, 3, 0, 0, 10) == (7.0, 0.0)
    assert r.analytic_a(1e-16, 0, 1, 0, 1) == pytest.approx(1e-16, rel=1e-15, abs=0)


def test_euler_independent_geometric_oracle():
    tr = r.euler(100, 0, 0.4, 0.1, 0.1, 50)
    for n, (t, a, b) in enumerate(tr):
        assert t == pytest.approx(n * 0.1)
        assert a == pytest.approx(20 + 80 * 0.95**n)
        assert a + b == pytest.approx(100)


def test_first_order_convergence():
    errors = [
        abs(
            r.euler(100, 0, 0.4, 0.1, dt, round(5 / dt))[-1][1]
            - (20 + 80 * math.exp(-2.5))
        )
        for dt in (0.1, 0.05, 0.025)
    ]
    assert 1.99 < errors[0] / errors[1] < 2.01
    assert 1.99 < errors[1] / errors[2] < 2.01


def test_stability_does_not_imply_universal_positivity():
    # lambda=.5, dt=3 => stable eigenvalue -.5, but A1=1-3*.4 < 0.
    assert abs(1 - 3 * (0.4 + 0.1)) < 1
    assert 1 - 3 * 0.4 < 0
    with pytest.raises(ValueError, match="positivity"):
        r.euler(1, 0, 0.4, 0.1, 3, 1)


def test_euler_positive_boundary_and_zero_steps():
    assert r.euler(1, 0, 0.4, 0.1, 2.5, 1)[-1][1:] == (0.0, 1.0)
    assert len(r.euler(1, 0, 0.4, 0.1, 0.1, 0)) == 1


@pytest.mark.parametrize("bad", [True, -1, 0.5, float("nan"), float("inf")])
def test_count_not_truncated(bad):
    with pytest.raises(ValueError):
        r.ssa(bad, 0, 0.4, 0.1, 1)


@pytest.mark.parametrize("bad", [True, -1, float("nan"), float("inf")])
def test_rate_domain(bad):
    with pytest.raises(ValueError):
        r.ode_rhs(1, 0, bad, 0.1)


def test_clock_and_seed_domains():
    for kwargs in ({"event_limit": 1.5}, {"event_limit": True}, {"seed": True}):
        with pytest.raises(ValueError):
            r.ssa(1, 0, 0.4, 0.1, 1, **kwargs)
    with pytest.raises(ValueError):
        r.euler(1, 0, 0.4, 0.1, 0, 1)


def test_inverse_transform_and_reaction_threshold():
    tau, j = r.event_draw(3, 1, math.exp(-2), 0.74)
    assert tau == pytest.approx(0.5)
    assert j == 0
    assert r.event_draw(3, 1, 0.5, 0.75)[1] == 1
    assert r.event_draw(0, 1, 0.5, 0)[1] == 1
    assert r.event_draw(1, 0, 0.5, 0.999)[1] == 0


@pytest.mark.parametrize("u", [0, 1, -0.1, float("nan"), True])
def test_no_uniform_epsilon_clamp(u):
    with pytest.raises(ValueError):
        r.event_draw(1, 2, u, 0.5)


def test_ssa_conservation_unit_jumps_and_local_rng():
    random.seed(908)
    before = random.getstate()
    tr = r.ssa(20, 3, 0.4, 0.1, 10, seed=7)
    assert random.getstate() == before
    assert tr == r.ssa(20, 3, 0.4, 0.1, 10, seed=7)
    assert tr.complete
    for (t0, a0, b0), (t1, a1, b1) in zip(tr.events, tr.events[1:]):
        assert t1 > t0
        assert (a1 - a0, b1 - b0) in {(-1, 1), (1, -1)}
    assert all(
        type(a) is int and min(a, b) >= 0 and a + b == 23 for _, a, b in tr.events
    )


def test_right_continuous_observation():
    tr = r.ssa(10, 0, 1, 0, 5)
    t, a, b = tr.events[1]
    assert r.sample_at(tr, t) == (a, b)
    assert r.sample_at(tr, math.nextafter(t, -math.inf)) == (10, 0)
    with pytest.raises(ValueError):
        r.sample_at(tr, 5.01)


def test_event_budget_is_censoring_not_a_horizon_value():
    tr = r.ssa(100, 0, 0.4, 0.1, 5, event_limit=2)
    assert not tr.complete and tr.status == "event_budget_exhausted"
    assert len(tr.events) == 3 and tr.simulated_until == tr.events[-1][0]
    assert r.sample_at(tr, tr.simulated_until) == tr.events[-1][1:]
    with pytest.raises(ValueError, match="interval"):
        r.sample_at(tr, 5)


def test_absorbing_state_and_zero_horizon():
    tr = r.ssa(0, 0, 1, 1, 5, event_limit=0)
    assert tr.complete and tr.status == "absorbing"
    assert r.sample_at(tr, 5) == (0, 0)
    assert r.ssa(1, 0, 1, 0, 0, event_limit=0).complete


def test_mixed_initial_moments_independent_convolution():
    # Enumerate Bernoulli configurations without calling analytic_a or SSA.
    import itertools

    pAA = 0.2 + 0.8 * math.exp(-2.5)
    pBA = 0.2 * (1 - math.exp(-2.5))
    probs = [pAA] * 2 + [pBA] * 3
    law = [0.0] * 6
    for bits in itertools.product((0, 1), repeat=5):
        probability = math.prod(p if bit else 1 - p for bit, p in zip(bits, probs))
        law[sum(bits)] += probability
    mean = sum(j * p for j, p in enumerate(law))
    var = sum((j - mean) ** 2 * p for j, p in enumerate(law))
    assert r.exact_moments(2, 3, 0.4, 0.1, 5) == pytest.approx((mean, var))
    # Matching a mean alone does not make the two-group law binomial.
    assert var != pytest.approx(5 * (mean / 5) * (1 - mean / 5))


def test_fixed_ensemble_against_exact_population_not_measurements():
    e = r.ensemble(2000, 100, 0, 0.4, 0.1, 5)
    p = 0.2 + 0.8 * math.exp(-2.5)
    mean, variance = 100 * p, 100 * p * (1 - p)
    assert abs(e["mean"] - mean) < 4 * math.sqrt(variance / e["n"])
    assert abs(e["sample_variance"] - variance) / variance < 0.1
    assert e["mean_se"] == pytest.approx(math.sqrt(e["sample_variance"] / e["n"]))


def test_distinct_and_identical_bimolecular_unit_oracle():
    omega = 6.02214076e23 * 1e-15
    assert r.bimolecular_propensity(1e6, 10, 20, 1e-15) == pytest.approx(
        1e6 * 200 / omega
    )
    identical = r.bimolecular_propensity(1e6, 10, 10, 1e-15, True)
    assert identical == pytest.approx(2e6 / omega * math.comb(10, 2))
    assert identical != pytest.approx(1e6 / omega * math.comb(10, 2))
    assert r.bimolecular_propensity(1e6, 1, 1, 1e-15, True) == 0


def test_volume_scaling_and_nonlinear_mean_closure_counterexample():
    a = r.bimolecular_propensity(1e6, 10, 20, 1e-15)
    assert r.bimolecular_propensity(1e6, 10, 20, 2e-15) == pytest.approx(a / 2)
    # N=0 or 2 equally likely: E[N(N-1)]=1, E[N]*(E[N]-1)=0.
    assert (0.5 * 0 * (-1) + 0.5 * 2 * 1) == 1
    assert 1 * (1 - 1) == 0


def test_identical_mode_and_volume_domain():
    with pytest.raises(ValueError):
        r.bimolecular_propensity(1, 2, 3, 1, True)
    for v in (0, -1, True, float("inf")):
        with pytest.raises(ValueError):
            r.bimolecular_propensity(1, 2, 3, v)
