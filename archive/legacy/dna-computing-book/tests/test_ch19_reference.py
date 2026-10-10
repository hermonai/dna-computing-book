from pathlib import Path
import importlib.util
import json
import math
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna19", ROOT / "drafts/ch19/reference.py"
)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_reproducible_results():
    assert m.results() == json.loads((ROOT / "drafts/ch19/results.json").read_text())


@pytest.mark.parametrize("length", [1, 2, 4, 12])
@pytest.mark.parametrize("detach", [0, 0.01, 1, 10])
def test_closed_form_success_and_generator_balance(length, detach):
    q, rp = m.branch_chain(length, 2, 2, detach)
    rd = np.zeros(length)
    rd[0] = detach
    assert np.allclose(q.sum(axis=1) + rp + rd, 0)
    p = np.linalg.solve(-q, rp)
    expected = (1 + np.arange(length) * detach / 2) / (1 + length * detach / 2)
    assert p == pytest.approx(expected)
    assert m.first_passage(length, 2, 2, detach)[0] == pytest.approx(expected[0])
    if detach == 0:
        assert m.first_passage(length, 2, 2, detach)[1] == pytest.approx(
            length * (length + 1) / 4
        )


@pytest.mark.parametrize(
    "forward,backward,detach", [(2, 2, 1), (3, 0.5, 4), (1, 0, 0.1)]
)
def test_first_passage_against_uniformized_paths(forward, backward, detach):
    q, rp = m.branch_chain(4, forward, backward, detach)
    # Uniformization sums discrete path masses, independently of linear solves.
    # Conditional on n Poisson events, the mean elapsed time is n / frequency.
    frequency = max(-q.diagonal())
    transition = np.eye(len(q)) + q / frequency
    mass = np.zeros(len(q))
    mass[0] = 1
    probability = moment = mean = 0.0
    for step in range(1, 200001):
        mean += mass.sum() / frequency
        released = mass @ rp / frequency
        probability += released
        moment += step / frequency * released
        mass = mass @ transition
        if mass.sum() < 1e-14:
            break
    else:
        pytest.fail("uniformized path sum did not converge")
    got = m.first_passage(4, forward, backward, detach)
    assert got == pytest.approx((probability, mean, moment / probability))
    scaled = m.first_passage(4, forward * 7, backward * 7, detach * 7)
    assert scaled == pytest.approx((got[0], got[1] / 7, got[2] / 7))


@pytest.mark.parametrize(
    "length,rates",
    [
        (0, (1, 1, 1)),
        (True, (1, 1, 1)),
        (1, (0, 1, 1)),
        (2, (1, -1, 1)),
        (2, (1, 1, math.nan)),
    ],
)
def test_bad_walk_parameters(length, rates):
    with pytest.raises(ValueError):
        m.first_passage(length, *rates)


@pytest.mark.parametrize(
    "input0,gate0",
    [(100, 100), (30, 100), (100, 30), (0, 100), (100, 100.00001)],
)
def test_conversion_against_independent_ode_and_inventory(input0, gate0):
    k = 0.0001
    # Fixed-step RK4 is an independent numerical oracle for the exact formula.
    step_size = 0.1
    output = 0.0
    samples = [(0, output)]

    def velocity(extent):
        return k * (input0 - extent) * (gate0 - extent)

    for step in range(1, 5001):
        k1 = velocity(output)
        k2 = velocity(output + step_size * k1 / 2)
        k3 = velocity(output + step_size * k2 / 2)
        k4 = velocity(output + step_size * k3)
        output += step_size * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        if step in (100, 1000, 5000):
            samples.append((step * step_size, output))
    for time, output in samples:
        x = m.conversion(input0, gate0, k, time)
        assert x == pytest.approx(output, abs=1e-7)
        assert 0 <= x <= min(input0, gate0)
        assert (input0 - x) + x == pytest.approx(input0)
        assert (gate0 - x) + x == pytest.approx(gate0)
        assert m.conversion(gate0, input0, k, time) == pytest.approx(x)
    assert m.conversion(input0, gate0, 0, 100) == 0


def test_half_conversion_and_leak_window():
    # Avoid subtracting nearly equal numbers at very small reaction extent.
    assert m.conversion(100, 100, 1e-22, 1) == pytest.approx(1e-18, rel=1e-12, abs=0)
    assert m.conversion(100, 100, 0.0001, 100) == pytest.approx(50)
    start = math.log(2) / 0.011
    end = math.log(2) / 0.001
    assert m.reporter(start)[0] == pytest.approx(0.5)
    assert m.reporter(end)[1] == pytest.approx(0.5)
    assert m.reporter(100)[0] > 0.5 > m.reporter(100)[1]
    assert m.reporter(1000)[1] > 0.5
    assert m.reporter(100, 0)[0] == m.reporter(100, 0)[1]
    assert m.reporter(100, leak_hazard=0)[1] == 0


@pytest.mark.parametrize(
    "values", [(-1, 100, 0.1, 1), (1, 1, math.inf, 1), (1, 1, 0.1, -1)]
)
def test_invalid_batch(values):
    with pytest.raises(ValueError):
        m.conversion(*values)
