"""Independent algebra, dense RK4 and exact enumeration checks."""

import importlib.util
import itertools
import math
from pathlib import Path
import random
import sys
import pytest

spec = importlib.util.spec_from_file_location(
    "dnad30", Path(__file__).parents[1] / "drafts/ch30/reference.py"
)
r = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = r
spec.loader.exec_module(r)


@pytest.mark.parametrize("x", [0, 0.1, 0.5, 1, 2, 10, 1e200])
def test_hill_independent_rational(x):
    got = r.hill_activation(x, 1, 2)
    expected = x * x / (1 + x * x) if x < 1e100 else 1.0
    assert got == pytest.approx(expected)
    assert got + r.hill_repression(x) == pytest.approx(1)


@pytest.mark.parametrize(
    "args",
    [
        (-1, 1, 2),
        (1, 0, 2),
        (1, 1, 0),
        (math.nan, 1, 2),
        (1, math.inf, 2),
        (True, 1, 2),
    ],
)
def test_hill_guards(args):
    with pytest.raises(ValueError):
        r.hill_activation(*args)
    with pytest.raises(ValueError):
        r.hill_repression(*args)


def test_cis_trans_accessibility_independent_partition_weights():
    weights = [1, 3]
    occupancy = weights[1] / sum(weights)
    assert r.allele_rates((0.5, 1), (1, 0.25), 3) == (0.5 * occupancy, 0.25 * occupancy)
    assert r.allele_rates((1, 1), (0, 1), 1) == (0, 0.5)


def test_allele_shape_and_domain():
    for args in [((1,), (1, 1), 1), ((1, 1), (2, 0), 1), ((1, -1), (1, 1), 1)]:
        with pytest.raises(ValueError):
            r.allele_rates(*args)


def test_simultaneous_not_sequential():
    got = r.euler_step(0.2, 0.7, 0.1)
    expected = (0.9 * 0.2 + 0.1 * 3 / (1 + 0.7**2), 0.9 * 0.7 + 0.1 * 3 / (1 + 0.2**2))
    assert got == pytest.approx(expected)
    wrong_b = 0.9 * 0.7 + 0.1 * 3 / (1 + got[0] ** 2)
    assert abs(got[1] - wrong_b) > 0.01


@pytest.mark.parametrize("h", [0.01, 0.1, 1])
def test_positivity_without_clipping(h):
    for a, b in itertools.product([0, 0.01, 1, 100], repeat=2):
        assert min(r.euler_step(a, b, h)) >= 0


def test_unstable_step_rejected_not_clipped():
    with pytest.raises(ValueError):
        r.euler_step(10, 10, 2)
    raw = 10 + 2 * (3 / 101 - 10)
    assert raw < 0  # A clipped zero would hide the invalid scheme.


@pytest.mark.parametrize(
    "args",
    [
        {"dt": 0},
        {"dt": 1.1},
        {"steps": -1},
        {"steps": True},
        {"a0": math.inf},
        {"signal": -1},
        {"intervene_a": -1},
    ],
)
def test_simulation_guards(args):
    with pytest.raises(ValueError):
        r.simulate(**args)


@pytest.mark.parametrize("alpha", [0, 1, 2, 3, 8])
def test_fixed_point_and_jacobian_independent(alpha):
    pts = r.fixed_points(alpha)
    assert len(pts) == (3 if alpha > 2 else 1)
    for a, b in pts:
        assert a == pytest.approx(alpha / (1 + b * b), abs=1e-12)
        assert b == pytest.approx(alpha / (1 + a * a), abs=1e-12)
        jac = [
            [-1, -2 * alpha * b / (1 + b * b) ** 2],
            [-2 * alpha * a / (1 + a * a) ** 2, -1],
        ]
        determinant = jac[0][0] * jac[1][1] - jac[0][1] * jac[1][0]
        values = r.eigenvalues(a, b, alpha)
        assert sum(values) == pytest.approx(-2)
        assert math.prod(values) == pytest.approx(determinant)


def test_stability_threshold_exact():
    assert r.eigenvalues(1, 1, 2)[1] == 0
    asym = r.fixed_points(3)[1]
    assert r.eigenvalues(*asym) == pytest.approx((-5 / 3, -1 / 3))
    assert r.eigenvalues(*r.fixed_points(3)[0])[1] > 0
    assert r.eigenvalues(*r.fixed_points(1)[0], alpha=1)[1] < 0


def rk4_oracle(a, b, horizon=10, h=0.001):
    # Independent explicit rational RHS, not r.rhs or r.hill_repression.
    def f(x, y):
        return 3 / (1 + y * y) - x, 3 / (1 + x * x) - y

    for _ in range(round(horizon / h)):
        k1 = f(a, b)
        k2 = f(a + h * k1[0] / 2, b + h * k1[1] / 2)
        k3 = f(a + h * k2[0] / 2, b + h * k2[1] / 2)
        k4 = f(a + h * k3[0], b + h * k3[1])
        a += h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        b += h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
    return a, b


def test_euler_convergence_to_independent_rk4():
    exact = rk4_oracle(0.11, 0.1)
    errors = []
    for h in [0.04, 0.02, 0.01, 0.005]:
        _, a, b = r.simulate(dt=h, steps=round(10 / h))[-1]
        errors.append(max(abs(a - exact[0]), abs(b - exact[1])))
    assert all(1.8 < errors[i] / errors[i + 1] < 2.2 for i in range(3))


def test_history_bias_exchange_and_symmetry():
    a = r.simulate()[-1][1:]
    b = r.simulate(a0=0.1, b0=0.11)[-1][1:]
    sym = r.simulate(a0=0.1, b0=0.1)[-1][1:]
    assert a == pytest.approx(b[::-1], abs=1e-14)
    assert a[0] - a[1] > 2
    assert sym[0] == sym[1]  # An exact symmetric initial state never chooses a branch.


def test_production_off_not_state_clamp():
    h = 0.01
    path = r.simulate(intervene_a=0)
    assert path[-1][1] == pytest.approx(0.11 * (1 - h) ** 6000, rel=1e-12)
    assert path[1][1] > 0
    assert path[-1][2] > r.simulate()[-1][2]


def test_zero_steps_and_cis_guard():
    assert r.simulate(steps=0) == [(0, 0.11, 0.1)]
    with pytest.raises(ValueError):
        r.Genotype(-1, 3)
    with pytest.raises(ValueError):
        r.fixed_points(101)


@pytest.mark.parametrize("p", [0, 0.25, 0.5, 1])
def test_partition_independent_bitstrings(p):
    probability = [0.0] * 4
    for bits in itertools.product([0, 1], repeat=3):
        probability[sum(bits)] += math.prod(p if b else 1 - p for b in bits)
    assert r.partition_law(3, p) == pytest.approx(probability)
    assert sum(probability) == pytest.approx(1)
    assert sum(k * v for k, v in enumerate(probability)) == pytest.approx(3 * p)


def test_partition_count_and_rng():
    random.seed(998)
    before = random.getstate()
    left, right = r.partition_counts(50, 30)
    assert left + right == 50
    assert r.partition_counts(50, 30) == (left, right)
    assert random.getstate() == before
    assert r.partition_counts(3, 30, 0) == (0, 3)
    assert r.partition_counts(3, 30, 1) == (3, 0)


def test_lineage_not_pseudotime_neighbors():
    cells = [
        r.Cell("root", None, 0, 0.2),
        r.Cell("left", "root", 1, 0.9),
        r.Cell("right", "root", 1, 0.1),
    ]
    assert r.lineage_edges(cells) == (("root", "left"), ("root", "right"))
    ordered = sorted(cells, key=lambda c: c.pseudotime)
    assert [c.name for c in ordered] == ["right", "root", "left"]
    assert (ordered[0].name, ordered[1].name) not in r.lineage_edges(cells)


@pytest.mark.parametrize(
    "cells",
    [
        [],
        [r.Cell("a", None, 0, 0), r.Cell("a", None, 1, 1)],
        [r.Cell("a", "missing", 1, 1)],
        [r.Cell("a", "b", 1, 1), r.Cell("b", "a", 1, 1)],
        [r.Cell("a", None, math.nan, 0)],
    ],
)
def test_invalid_lineage(cells):
    with pytest.raises(ValueError):
        r.lineage_edges(cells)


def test_selection_independent_population_and_closed_form():
    p = r.selection_mutation(0.25, 2, 1)
    assert p == 2 / (2 + 3)  # One type1 parent leaves2 descendants, three type0 leave3.
    for t in range(1, 7):
        p = r.selection_mutation(0.25, 2, 1)
        for _ in range(t - 1):
            p = r.selection_mutation(p, 2, 1)
        assert p == pytest.approx(2**t / (2**t + 3))


def test_selection_scale_neutral_and_mutation_order():
    assert r.selection_mutation(0.25, 2, 1) == r.selection_mutation(0.25, 200, 100)
    assert r.selection_mutation(0.25, 1, 1) == 0.25
    assert r.selection_mutation(0.25, 2, 1, 0.1, 0.2) == pytest.approx(0.48)
    wrong = r.selection_mutation(0.9 * 0.25 + 0.2 * 0.75, 2, 1)
    assert abs(wrong - 0.48) > 0.04


@pytest.mark.parametrize(
    "args",
    [(2, 1, 1), (0.2, 0, 0), (0.2, -1, 1), (0.2, 1, 1, 2), (0.2, 1, 1, 0, math.nan)],
)
def test_selection_guards(args):
    with pytest.raises(ValueError):
        r.selection_mutation(*args)
