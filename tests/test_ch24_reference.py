import importlib.util
from pathlib import Path
import math
import itertools
import pytest

spec = importlib.util.spec_from_file_location(
    "dna24", Path(__file__).parents[1] / "book/chapters/ch24/reference.py"
)
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def test_exact_si_copy_conversion_and_dilution():
    assert r.molecule_expectation(1e-9, 1e-6) == pytest.approx(602214076)
    assert r.dilution_volume(10, 1, 100) == 10
    with pytest.raises(ValueError):
        r.dilution_volume(1, 2, 100)


@pytest.mark.parametrize("bits", [0, 1, 10, 60])
def test_enumeration_is_not_polynomial(bits):
    assert r.candidates(bits) == 2**bits
    assert r.candidates(bits + 1) == 2 * r.candidates(bits)


@pytest.mark.parametrize("species", [1, 8, 1024, 2**60])
def test_poisson_required_coverage_inversion(species):
    mu = r.coverage_copies(species, 0.05)
    assert r.poisson_complete(species, mu) == pytest.approx(0.95, abs=1e-14)
    assert r.coverage_union_copies(species, 0.05) >= mu
    assert (
        r.poisson_complete(species, r.coverage_union_copies(species, 0.05))
        >= 0.95 - 1e-14
    )


def test_poisson_tiny_mean_no_cancellation():
    assert r.poisson_complete(1, 1e-20) == pytest.approx(1e-20, rel=1e-12, abs=0)
    assert r.poisson_complete(10, 0) == 0
    assert r.poisson_complete(10, 1000) == 1


def test_volume_mass_balance_and_scaling():
    m = 1024
    volume = r.coverage_volume(m, 0.05, 1e-6)
    assert r.molecule_expectation(1e-6, volume) == pytest.approx(
        m * r.coverage_copies(m, 0.05)
    )
    assert r.coverage_volume(m, 0.05, 2e-6) == volume / 2


def test_fixed_draw_independent_exhaustive_oracle():
    for m in (2, 3):
        for draws in range(1, 6):
            values = list(itertools.product(range(m), repeat=draws))
            probability = sum(len(set(v)) == m for v in values) / len(values)
            assert r.fixed_draw_complete(m, draws) == pytest.approx(probability)
    assert r.fixed_draw_complete(1, 0) == 0


def test_poisson_monte_carlo_is_distinct_from_fixed_draws():
    result = r.poisson_coverage_monte_carlo(8, 3)
    assert result == r.poisson_coverage_monte_carlo(8, 3)
    assert abs(result - r.poisson_complete(8, 3)) < 0.04
    assert abs(r.fixed_draw_complete(8, 24) - r.poisson_complete(8, 3)) > 0.01


@pytest.mark.parametrize("time", [0, 0.001, 1, 10, 100])
def test_erlang_independent_depth_two_closed_form(time):
    x = 0.1 * time
    # Integral/original algebraic formula; expm1 stabilizes small x.
    oracle = -math.expm1(-x) - x * math.exp(-x)
    assert r.erlang_complete(2, 0.1, time) == pytest.approx(oracle, abs=1e-15)
    assert r.erlang_complete(0, 0.1, time) == 1


def test_latency_serial_and_parallel_contracts():
    assert r.serial_mean(4, 0.1) == 40
    assert r.parallel_complete(4, 0.1, 40, 100) < r.erlang_complete(4, 0.1, 40)
    assert r.parallel_complete(4, 0.1, 40, 0) == 1
    assert r.erlang_complete(256, 1, 1e6) == 1


def test_concentration_and_transport_counterexamples():
    assert r.species_wait(20, 1e-6, 1e6) == 2 * r.species_wait(10, 1e-6, 1e6)
    assert r.diffusion_time(2e-3, 1e-10) == 4 * r.diffusion_time(1e-3, 1e-10)
    assert r.diffusion_time(1e-3, 1e-10, 1) == 3 * r.diffusion_time(1e-3, 1e-10, 3)


def test_detection_boundary_and_inversion():
    for efficiency in (1, 0.1, 0.01):
        copies = r.required_detectable_copies(0.05, efficiency)
        assert r.detection_probability(copies, efficiency) == pytest.approx(0.95)
    assert r.detection_probability(100, 0) == 0
    assert r.detection_probability(0, 1) == 0
    assert r.detection_probability(1e-20, 1) == pytest.approx(1e-20, abs=0)


def test_readout_and_ideal_erasure_units():
    assert r.readout_time(1_000_000, 100_000) == 10
    assert r.erasure_lower_bound(1, 300) == pytest.approx(2.870978885078724e-21)
    assert r.erasure_lower_bound(0, 300) == 0


@pytest.mark.parametrize(
    "call,args",
    [
        ("candidates", (-1,)),
        ("candidates", (True,)),
        ("coverage_copies", (0, 0.05)),
        ("coverage_copies", (2, 0)),
        ("coverage_copies", (2, 1)),
        ("coverage_copies", (2, float("nan"))),
        ("coverage_volume", (2, 0.05, 0)),
        ("molecule_expectation", (float("inf"), 1)),
        ("detection_probability", (1, 1.1)),
        ("required_detectable_copies", (0.05, 0)),
        ("species_wait", (2, 1, -1)),
        ("diffusion_time", (1, 1, 4)),
        ("erlang_complete", (257, 1, 1)),
        ("fixed_draw_complete", (129, 1)),
    ],
)
def test_declared_invalid_domains(call, args):
    with pytest.raises(ValueError):
        getattr(r, call)(*args)
