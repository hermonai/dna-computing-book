"""Independent kinetic, calibration and evidence-scope oracles."""

import importlib.util
from pathlib import Path
import sys
import math
from dataclasses import replace
import pytest

PATH = Path(__file__).resolve().parents[1] / "book/chapters/ch31/reference.py"
spec = importlib.util.spec_from_file_location("dna31", PATH)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def rk4_linear(u, off, cat, horizon, dt=0.001):
    # Independent handwritten linear system, no reference RHS or step calls.
    a, i = 1.0, 0.0

    def f(x, y):
        return -u * x + off * y, u * x - (off + cat) * y

    for _ in range(round(horizon / dt)):
        p = f(a, i)
        q = f(a + dt * p[0] / 2, i + dt * p[1] / 2)
        r = f(a + dt * q[0] / 2, i + dt * q[1] / 2)
        s = f(a + dt * r[0], i + dt * r[1])
        a += dt * (p[0] + 2 * q[0] + 2 * r[0] + s[0]) / 6
        i += dt * (p[1] + 2 * q[1] + 2 * r[1] + s[1]) / 6
    return a, i, 1 - a - i


@pytest.mark.parametrize(
    "u,off,cat",
    [
        (0.0, 1.0, 0.1),
        (0.1, 0.9, 0.1),
        (1.0, 0.0, 1.0),
        (2.0, 1.0, 0.3),
        (0.02, 0.5, 0.0),
    ],
)
@pytest.mark.parametrize("time", [0.0, 0.1, 1.0, 5.0])
def test_exact_poles_against_independent_rk4(u, off, cat, time):
    assert m.held_fuel(1, u, off, cat, time) == pytest.approx(
        rk4_linear(u, off, cat, time), abs=2e-11
    )


@pytest.mark.parametrize("f0", [0.1, 1.0, 10.0])
@pytest.mark.parametrize("dt", [0.01, 0.002, 0.0005])
def test_finite_pools_and_capacity(f0, dt):
    a, f, i, b, w = m.simulate((1.0, f0, 0.0, 0.0, 0.0), m.Rates(0.1, 0.9, 0.1), 20, dt)
    assert min(a, f, i, b, w) >= 0
    assert a + i + b == pytest.approx(1, abs=2e-12)
    assert f + i + w == pytest.approx(f0, abs=2e-12)
    assert b == pytest.approx(w)
    assert b <= min(1, f0)


def test_euler_first_order_convergence():
    # Constant-fuel independent system vs finite-fuel converged RK4 below.
    rates = m.Rates(0.1, 0.9, 0.1)
    initial = (1.0, 1.0, 0.0, 0.0, 0.0)

    def f(y):
        a, fuel, i, b, w = y
        q, r, s = 0.1 * a * fuel, 0.9 * i, 0.1 * i
        return (-q + r, -q + r, q - r - s, s, s)

    y = initial
    dt = 0.0005
    for _ in range(4000):
        p = f(y)
        q = f(tuple(v + dt * d / 2 for v, d in zip(y, p)))
        r = f(tuple(v + dt * d / 2 for v, d in zip(y, q)))
        s = f(tuple(v + dt * d for v, d in zip(y, r)))
        y = tuple(
            v + dt * (x + 2 * z + 2 * k + last) / 6
            for v, x, z, k, last in zip(y, p, q, r, s)
        )
    errors = [
        max(abs(a - b) for a, b in zip(m.simulate(initial, rates, 2, h), y))
        for h in [0.02, 0.01, 0.005]
    ]
    assert 1.9 < errors[0] / errors[1] < 2.1
    assert 1.9 < errors[1] / errors[2] < 2.1


def test_reduced_model_has_wrong_initial_slope():
    h = 0.0001
    exact_b = m.held_fuel(1, 0.1, 0.9, 0.1, h)[2]
    assert abs(exact_b / h) < 1e-5
    assert -math.expm1(-0.01 * h) / h == pytest.approx(0.01, rel=1e-6)


@pytest.mark.parametrize("bad", [-1, float("nan"), float("inf"), True])
def test_rate_input_rejected(bad):
    with pytest.raises(ValueError):
        m.Rates(bad, 0.1, 0.1)


@pytest.mark.parametrize("dt", [0.0, 2.0, float("inf"), -1.0])
def test_unsafe_step_rejected(dt):
    with pytest.raises(ValueError):
        m.euler_step((1.0, 1.0, 0.0, 0.0, 0.0), m.Rates(1.0, 0.9, 0.1), dt)


@pytest.mark.parametrize("y", [(0.48, 0.52), (0.02, 0.08), (0.15, 0.15)])
def test_calibration_corners(y):
    offset = (0.01, 0.1)
    gain = (0.9, 1.1)
    lo, hi = m.calibrated_interval(y, offset, gain)
    feasible = [(yy - oo) / gg for yy in y for oo in offset for gg in gain if yy >= oo]
    assert lo <= min(feasible) + 1e-12 and hi >= max(feasible) - 1e-12
    if y[0] <= offset[1]:
        assert lo == 0


@pytest.mark.parametrize(
    "args",
    [
        ((1, 0), (0, 1), (1, 2)),
        ((0, 1), (0, 0), (0, 1)),
        ((0, 1), (2, 3), (1, 2)),
        ((0, float("nan")), (0, 0), (1, 2)),
    ],
)
def test_bad_calibration(args):
    with pytest.raises(ValueError):
        m.calibrated_interval(*args)


@pytest.mark.parametrize("L", [0.0, 0.01, 0.2])
def test_error_envelope_against_quadrature(L):
    t, initial, eta = 2.0, 0.1, 0.03
    n = 10000
    integral = sum(math.exp(L * (t - (k + 0.5) * t / n)) * t / n for k in range(n))
    assert m.error_bound(initial, eta, L, t) == pytest.approx(
        initial * math.exp(L * t) + eta * integral, rel=1e-9
    )


def test_unit_not_technical_sample_count():
    r = m.summarize_units({"u1": [0.4, 0.42], "u2": [0.1, 0.12], "u3": [0.38, 0.4]})
    assert r["units"] == 3 and r["technical_reads"] == 6
    assert r["mean"] == pytest.approx((0.41 + 0.11 + 0.39) / 3)
    assert m.summarize_units({"u": [1, 2, 3]})["sample_sd"] is None


@pytest.mark.parametrize("reads", [{}, {"x": []}, {"": [1]}, {"x": [float("nan")]}])
def test_invalid_reads(reads):
    with pytest.raises(ValueError):
        m.summarize_units(reads)


def fixture():
    e = m.Evidence(
        "measured",
        "buffer-A",
        "reporter-v1",
        frozenset({"blank"}),
        frozenset({"B"}),
        ("a", "b", "c"),
        "doi:example",
    )
    c = m.Claim(
        "measured", "buffer-A", "reporter-v1", frozenset({"blank"}), frozenset({"B"}), 3
    )
    return e, c


def test_valid_metadata_does_not_encode_outcome():
    e, c = fixture()
    assert m.admissible(e, c)  # No claim of a positive effect is made here.


@pytest.mark.parametrize(
    "change",
    [
        {"context": "cell"},
        {"kind": "formal"},
        {"protocol": "reporter-v2"},
        {"controls": frozenset()},
        {"observables": frozenset({"fluorescence"})},
        {"unit_ids": ("a", "a", "c")},
        {"unit_ids": ("a",)},
        {"source": ""},
    ],
)
def test_scope_and_coverage_falsifiers(change):
    e, c = fixture()
    assert not m.admissible(replace(e, **change), c)


def test_observation_nonidentifiability():
    # y=B+I cannot distinguish these two nonnegative states.
    assert 0.4 + 0.1 == pytest.approx(0.2 + 0.3)
    assert 0.4 != 0.2
