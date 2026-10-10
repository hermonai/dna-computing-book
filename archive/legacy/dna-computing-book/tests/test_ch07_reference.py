import importlib.util
import json
import math
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna07", ROOT / "drafts/ch07/reference.py"
)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def test_equilibrium_flux_and_initial_slope():
    assert M.fluxes(80e-9, 100e-9, 100e-9, 1e6, 0.005) == pytest.approx(
        (4e-10, 4e-10), rel=1e-12, abs=0
    )
    assert M.fluxes(0, 100e-9, 100e-9, 1e6, 0.005) == pytest.approx(
        (1e-8, 0), rel=1e-12, abs=0
    )
    eps = 1e-5
    assert M.equal_pool_exact(
        eps, 100e-9, 1e6, 0.005
    ) / eps == pytest.approx(1e-8, rel=2e-6)


@pytest.mark.parametrize("t", [0, 0.01, 1, 20, 120, 1000])
def test_closed_form_and_time_rescaling(t):
    x = M.equal_pool_exact(t, 100e-9, 1e6, 0.005)
    assert 0 <= x <= 80e-9
    assert M.equal_pool_exact(t, 100e-9, 1e7, 0.05) == pytest.approx(
        M.equal_pool_exact(10 * t, 100e-9, 1e6, 0.005), abs=1e-20
    )
    if t <= 120:
        assert M.rk4(t, 0.1, 100e-9, 100e-9, 1e6, 0.005) == pytest.approx(
            x, abs=1e-15
        )


def test_rk4_convergence_order_and_bad_step():
    errors = [r["error_nm"] for r in M.results()["convergence"]]
    assert all(12 < errors[i] / errors[i + 1] < 22 for i in range(3))
    with pytest.raises(ValueError):
        M.rk4(100, 100, 100e-9, 100e-9, 1e6, 0.005)
    with pytest.raises(ValueError):
        M.rk4(10, 0, 100e-9, 100e-9, 1e6, 0.005)


def test_count_units_and_single_pair():
    volume = 20 / (M.AVOGADRO * 100e-9)
    assert M.propensities(0, 20, 20, volume, 1e6, 0.005) == pytest.approx(
        (2, 0)
    )
    assert M.stationary(1, 1, volume / 20, 1e6, 0.005) == pytest.approx(
        [1 / 21, 20 / 21]
    )


@pytest.mark.parametrize("n", [0, 1, 2, 20, 200])
def test_stationary_detailed_balance(n):
    volume = max(n, 1) / (M.AVOGADRO * 100e-9)
    p = M.stationary(n, n, volume, 1e6, 0.005)
    assert math.fsum(p) == pytest.approx(1)
    assert all(w >= 0 for w in p)
    for d in range(n):
        on, _ = M.propensities(d, n, n, volume, 1e6, 0.005)
        _, off = M.propensities(d + 1, n, n, volume, 1e6, 0.005)
        assert p[d] * on == pytest.approx(p[d + 1] * off, abs=1e-14)


def test_ssa_conservation_event_order_seed_and_zero_rate():
    volume = 20 / (M.AVOGADRO * 100e-9)
    trace = M.ssa(20, 12, volume, 1e6, 0.005, 100, 1701)
    assert trace == M.ssa(20, 12, volume, 1e6, 0.005, 100, 1701)
    for (t0, d0), (t1, d1) in zip(trace, trace[1:]):
        assert 0 <= d1 <= 12 and t0 < t1 <= 100 and abs(d1 - d0) == 1
    assert M.ssa(0, 12, volume, 1e6, 0.005, 100) == [(0.0, 0)]
    assert M.ssa(20, 12, volume, 0, 0, 100) == [(0.0, 0)]
    with pytest.raises(RuntimeError):
        M.ssa(20, 12, volume, 1e6, 0.005, 100, max_events=1)


def test_ssa_against_exact_two_state_transient():
    # Independent exact Bernoulli transient for one A and one B.
    volume = 1 / (M.AVOGADRO * 100e-9)
    horizon = 20
    expected = (0.1 / 0.105) * (1 - math.exp(-0.105 * horizon))
    samples = 4000
    observed = (
        sum(
            M.ssa(1, 1, volume, 1e6, 0.005, horizon, seed=s)[-1][1]
            for s in range(samples)
        )
        / samples
    )
    se = math.sqrt(expected * (1 - expected) / samples)
    assert abs(observed - expected) < 6 * se


@pytest.mark.parametrize("bad", [-1, 0.5, True])
def test_reject_noninteger_inventory(bad):
    with pytest.raises(ValueError):
        M.propensities(bad, 20, 20, 1e-15, 1e6, 0.005)


def test_nonlinear_stationary_mean_is_not_ode_root():
    r = M.results()
    assert r["stationary_mean_nm"] > 80
    # E[(n-D)^2]=(n-E[D])^2+Var[D], independently check balance.
    mean, var = r["mean_count"], r["variance_count"]
    assert 0.005 * ((20 - mean) ** 2 + var) == pytest.approx(0.005 * mean)


def test_results_reproducible():
    assert json.loads(
        (ROOT / "drafts/ch07/results.json").read_text()
    ) == json.loads(json.dumps(M.results()))
