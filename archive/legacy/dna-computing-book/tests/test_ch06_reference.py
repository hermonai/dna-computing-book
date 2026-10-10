import importlib.util
from pathlib import Path
import math
import json
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna06", ROOT / "drafts/ch06/reference.py"
)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def test_exact_inventory():
    x = M.duplex_molar(100e-9, 100e-9, 5e-9)
    assert x == pytest.approx(80e-9)
    assert (100e-9 - x) ** 2 / x == pytest.approx(5e-9)
    assert 100 / 105 > x / 100e-9


@pytest.mark.parametrize("a", [1e-15, 1e-9, 1e-3, 1.0])
def test_physical_root_against_independent_bisection(a):
    for b in (1e-15, 1e-8, 0.1):
        for kd in (1e-15, 1e-7, 1e3):
            lo, hi = 0.0, min(a, b)
            for _ in range(180):
                mid = (lo + hi) / 2
                if (a - mid) * (b - mid) > kd * mid:
                    lo = mid
                else:
                    hi = mid
            x = M.duplex_molar(a, b, kd)
            assert x == pytest.approx((lo + hi) / 2, rel=2e-12, abs=1e-40)
            assert 0 <= x <= min(a, b) * (1 + 1e-14)
            assert M.duplex_molar(b, a, kd) == pytest.approx(x)


def test_zero_limits():
    assert M.duplex_molar(0, 1, 2) == 0
    assert M.duplex_molar(2, 3, 0) == pytest.approx(2)
    assert M.duplex_molar(2, 2, 0) == pytest.approx(2)


@pytest.mark.parametrize("v", [-1, float("nan"), float("inf"), True, "1"])
def test_invalid_concentration(v):
    with pytest.raises(ValueError):
        M.duplex_molar(v, 1, 1)


def test_nn_independent_sum_and_orientation():
    p = M.nn_parameters("ACGTCAGT")
    assert p["steps"] == {"GT": 3, "CG": 1, "GA": 1, "CA": 1, "CT": 1}
    assert p["dh_kcal"] == pytest.approx(-55.7)
    assert p["ds_cal"] == pytest.approx(-152.1)
    q = M.nn_parameters(M.reverse_complement("ACGTCAGT"))
    assert q["dh_kcal"] == pytest.approx(p["dh_kcal"])
    assert q["ds_cal"] == pytest.approx(p["ds_cal"])
    assert q["steps"] == p["steps"]


@pytest.mark.parametrize("s", ["A", "ACGT", "AN", "acgt", ""])
def test_reject_unsupported_sequence(s):
    with pytest.raises(ValueError):
        M.nn_parameters(s)


def test_salt_and_temperature_scope():
    with pytest.raises(ValueError):
        M.nn_parameters("ACGTCAGT", 0.05)
    with pytest.raises(ValueError):
        M.kd_from_thermo(-50, -100, 0)


@pytest.mark.parametrize("concentration", [1e-9, 1e-8, 1e-7, 1e-6])
def test_melting_half_bound_identity(concentration):
    p = M.nn_parameters("ACGTCAGT")
    t = M.melting_kelvin(p["dh_kcal"], p["ds_cal"], concentration)
    k = M.kd_from_thermo(p["dh_kcal"], p["ds_cal"], t)
    assert k == pytest.approx(concentration / 2, rel=1e-12)
    assert M.duplex_molar(
        concentration, concentration, k
    ) / concentration == pytest.approx(0.5)


def test_units_and_energy_sensitivity():
    t = 310.15
    ds = -152.1
    k = M.kd_from_thermo(-55.7, ds, t)
    assert k == pytest.approx(math.exp(-8526.185 / (M.R * t)))
    assert M.kd_from_thermo(-54.7, ds, t) / k == pytest.approx(
        math.exp(1000 / (M.R * t))
    )


def test_generated_results():
    assert json.loads(
        (ROOT / "drafts/ch06/results.json").read_text()
    ) == json.loads(json.dumps(M.results()))
