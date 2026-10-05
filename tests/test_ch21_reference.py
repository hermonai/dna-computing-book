from pathlib import Path
import importlib.util
import itertools
import json
import math
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna21", ROOT / "drafts/ch21/reference.py"
)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_generated_results():
    assert m.results() == json.loads(
        (ROOT / "drafts/ch21/results.json").read_text()
    )


@pytest.mark.parametrize("kind", ["OR", "AND"])
@pytest.mark.parametrize(
    "bits", list(itertools.product((0, 1), repeat=2))
)
def test_interval_truth_and_all_input_corners(kind, bits):
    lo, hi = m.gate_bounds(bits, kind)
    answer = any(bits) if kind == "OR" else all(bits)
    assert 0 <= lo <= hi <= 1
    assert lo >= 0.9 if answer else hi <= 0.1
    boxes = [(0, 0.1) if b == 0 else (0.9, 1.1) for b in bits]
    theta = 0.3 if kind == "OR" else 1.3
    values = [
        m.restored(x + y, th, 6, leak=leak)
        for x, y, th, leak in itertools.product(
            *boxes, (theta - 0.05, theta + 0.05), (0, 0.001)
        )
    ]
    assert lo == pytest.approx(min(values))
    assert hi == pytest.approx(max(values))


def test_window_boundaries_and_no_window_counterexample():
    first, last = m.read_window(0.45)
    assert first == pytest.approx(math.log(10) / 0.45)
    assert m.restored(0.45, 0, first) == pytest.approx(0.9)
    assert m.restored(0, 0, last, leak=0.001) == pytest.approx(0.1)
    assert first < 6 < last
    first, last = m.read_window(0.001, leak=0.1)
    assert first > last
    assert math.isinf(m.read_window(1, leak=0)[1])


def rk4(rhs, initial, end, steps):
    h = end / steps
    state = np.array(initial, dtype=float)
    for _ in range(steps):
        a = rhs(state)
        b = rhs(state + h * a / 2)
        c = rhs(state + h * b / 2)
        d = rhs(state + h * c)
        state += h * (a + 2 * b + 2 * c + d) / 6
    return state


@pytest.mark.parametrize("capture", [1, 10, 100])
def test_concurrent_race_against_independent_ode(capture):
    def rhs(s):
        x, q, f, y = s
        return np.array(
            [-capture * x * q, -capture * x * q, -x * f, x * f]
        )

    end = 10
    got = rk4(rhs, [0.2, 0.3, 1, 0], end, 10000)
    assert got[3] == pytest.approx(
        m.race_output(0.2, 0.3, capture, 1, end), abs=1e-9
    )
    assert got[1] - got[0] == pytest.approx(0.1)
    assert got[2] + got[3] == pytest.approx(1)
    assert min(got) >= 0


def test_staging_is_not_simultaneous_chemistry():
    assert m.restored(0.2, 0.3, 50) == 0
    assert m.race_output(0.2, 0.3, 1, 1, 50) > 0.6
    assert m.race_output(0.2, 0.3, 100, 1, 50) < 0.02
    assert m.race_output(0, 0.3, 1, 1, 50) == 0


def test_two_layer_composition_at_all_perturbation_corners():
    # (a OR b) AND c; private fuel and staged calls for every gate.
    for bits in itertools.product((0, 1), repeat=3):
        boxes = [(0, 0.1) if b == 0 else (0.9, 1.1) for b in bits]
        for a, b, c, t1, t2, l1, l2 in itertools.product(
            *boxes, (0.25, 0.35), (1.25, 1.35), (0, 0.001), (0, 0.001)
        ):
            y = m.restored(a + b, t1, 6, leak=l1)
            z = m.restored(y + c, t2, 6, leak=l2)
            assert (
                z >= 0.9 if (bits[0] or bits[1]) and bits[2] else z <= 0.1
            )


def test_analog_sensitivity_and_inventory_fanout():
    x, theta, t = 1.8, 1.3, 6
    eps = 1e-6
    slope = (
        m.restored(x + eps, theta, t) - m.restored(x - eps, theta, t)
    ) / (2 * eps)
    assert slope == pytest.approx(
        t * math.exp(-t * (x - theta)), rel=1e-8
    )
    output = m.restored(x, theta, t)
    assert output > 0.9 and output / 3 < 0.9
    assert sum([output / 3] * 3) == pytest.approx(output)
    assert m.loaded_signal(0.5, [1] * 3, 1) == 0.125


@pytest.mark.parametrize("seed", [0, 0.001, 0.1, 1])
def test_feedback_against_ode(seed):
    rhs = lambda s: s * (1 - s)
    got = rk4(rhs, [seed], 5, 2000)[0]
    assert m.feedback(seed, 1, 1, 5) == pytest.approx(got, abs=1e-10)
    assert seed <= got <= 1


def test_validation_and_empty_resources():
    assert m.restored(1, 0, 10, fuel=0) == 0
    assert m.restored(1, 0, 0) == 0
    for bad in (-1, math.nan, math.inf):
        with pytest.raises(ValueError):
            m.restored(bad, 0, 1)
    with pytest.raises(ValueError):
        m.gate_bounds((1, True), "OR")
    with pytest.raises(ValueError):
        m.race_output(1, 1, 1, 1, 1)
    with pytest.raises(ValueError):
        m.feedback(2, 1, 1, 1)
