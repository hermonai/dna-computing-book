from pathlib import Path
import importlib.util
import json
import math
import sys
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna20", ROOT / "drafts/ch20/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_results():
    assert m.results() == json.loads(
        (ROOT / "drafts/ch20/results.json").read_text()
    )


def test_strand_inventory_and_enabledness():
    crn = m.network([[1], [1], [0], [0]], [[0], [0], [1], [1]], [0.1])
    inventory = np.array([[1, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1]])
    assert not (inventory @ crn.change).any()
    start = np.array([3, 5, 0, 0])
    state = start.copy()
    for _ in range(3):
        assert inventory @ state == pytest.approx(inventory @ start)
        state = m.fire(crn, state, 0)
    assert state.tolist() == [0, 2, 3, 3]
    assert m.propensities(crn, state)[0] == 0
    with pytest.raises(ValueError):
        m.fire(crn, state, 0)
    assert start.tolist() == [3, 5, 0, 0]


@pytest.mark.parametrize("n", range(8))
def test_identical_reactants_use_pairs_not_squares(n):
    crn = m.network([[2], [0]], [[0], [1]], [3.0])
    assert m.propensities(crn, [n, 0], 10)[0] == pytest.approx(
        0.3 * n * (n - 1)
    )
    assert np.array([1, 2]) @ m.drift(crn, [n / 10, 0]) == pytest.approx(
        0
    )
    if n >= 2:
        assert m.fire(crn, [n, 0], 0).tolist() == [n - 2, 1]
    else:
        with pytest.raises(ValueError):
            m.fire(crn, [n, 0], 0)


def test_zero_order_and_density_limit():
    source = m.network([[0]], [[1]], [2.0])
    assert m.propensities(source, [0], 50)[0] == 100
    crn = m.network([[2], [0]], [[0], [1]], [0.2])
    x = np.array([3.0, 0])
    errors = []
    for omega in (10, 100, 1000):
        counts = (x * omega).astype(int)
        expected_drift = (
            crn.change @ m.propensities(crn, counts, omega) / omega
        )
        errors.append(np.linalg.norm(expected_drift - m.drift(crn, x)))
    assert errors[0] / errors[1] == pytest.approx(10)
    assert errors[1] / errors[2] == pytest.approx(10)


@pytest.mark.parametrize("a,b", [(0, 4), (1, 1), (4, 4), (8, 4), (4, 8)])
def test_completion_against_backward_recursion(a, b):
    # E[T^2] recursion uses E[holding^2]=2/rate^2, no sample estimate.
    mean = second = 0.0
    offset = abs(a - b)
    for n in range(1, min(a, b) + 1):
        hold = 1 / (n * (n + offset))
        second += 2 * hold * hold + 2 * hold * mean
        mean += hold
    got_mean, got_var = m.completion_moments(a, b)
    assert (got_mean, got_var) == pytest.approx(
        (mean, second - mean * mean)
    )
    assert m.completion_moments(a, b, k=2, omega=3) == pytest.approx(
        (1.5 * got_mean, 2.25 * got_var)
    )


def test_stochastic_paths_and_monte_carlo_error_budget():
    rng = np.random.default_rng(2020)
    times = []
    for _ in range(4000):
        path = m.annihilation_path(4, 3, rng)
        assert len(path) == 4
        assert path[-1][1:] == (1, 0)
        assert all(y[0] > x[0] for x, y in zip(path, path[1:]))
        times.append(path[-1][0])
    mean, var = m.completion_moments(4, 3)
    assert abs(np.mean(times) - mean) < 5 * math.sqrt(var / len(times))


@pytest.mark.parametrize(
    "alpha,beta", [(0, 0), (0, 0.3), (0.1, 0), (0.1, 0.3)]
)
def test_shared_fuel_against_rk4(alpha, beta):
    state = np.array([100.0, 0.0, 0.0])

    def rhs(x):
        return np.array(
            [-(alpha + beta) * x[0], alpha * x[0], beta * x[0]]
        )

    dt = 0.01
    for _ in range(1000):
        k1 = rhs(state)
        k2 = rhs(state + dt * k1 / 2)
        k3 = rhs(state + dt * k2 / 2)
        k4 = rhs(state + dt * k3)
        state += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    result = m.shared_fuel(100, alpha, beta, 10)
    assert result == pytest.approx(state, abs=1e-8)
    assert sum(result) == pytest.approx(100)
    assert min(result) >= 0


def test_small_remaining_fuel_survives_cancellation_and_reporting():
    f, y, z = m.shared_fuel(100, 0.1, 0.3, 100)
    assert f > 0
    assert f == pytest.approx(100 * math.exp(-40), rel=1e-14, abs=0)
    assert y + z == pytest.approx(100)
    assert m.results()["fuel"][-1]["fuel"] > 0


def test_bad_network_and_immutable_inputs():
    for r, p, k in [
        ([[1.0]], [[0]], [1]),
        ([[-1]], [[0]], [1]),
        ([[1]], [[0]], [-1]),
        ([[1]], [[0]], [math.nan]),
        ([[1]], [[0, 1]], [1]),
    ]:
        with pytest.raises(ValueError):
            m.network(r, p, k)
    r = np.array([[1], [0]])
    crn = m.network(r, [[0], [1]], [1])
    r[0, 0] = 9
    assert crn.reactants[0, 0] == 1
    with pytest.raises(ValueError):
        crn.reactants[0, 0] = 2
    for n in ([1.5, 0], [-1, 0], [True, False]):
        with pytest.raises(ValueError):
            m.propensities(crn, n)
    with pytest.raises(ValueError):
        m.propensities(crn, [1, 0], 0)
    with pytest.raises(ValueError):
        m.fire(crn, [1, 0], True)
