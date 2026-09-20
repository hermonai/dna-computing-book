import importlib.util
import json
import math
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna08", ROOT / "drafts/ch08/reference.py"
)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def test_cut_coordinates_and_inventory():
    seq = "CCGAATTCTTGAATTCGG"
    assert M.ecori_cut_sites(seq) == [(3, 7), (11, 15)]
    for top, bottom in M.ecori_cut_sites(seq):
        assert seq[top:bottom] == "AATT"
        assert len(seq[:top]) + len(seq[top:]) == len(seq)
        comp = M.complement(seq)
        assert len(comp[:bottom]) + len(comp[bottom:]) == len(seq)
    assert M.ecori_cut_sites("AAAA") == []
    assert M.ecori_cut_sites("GAATTC") == [(1, 5)]


@pytest.mark.parametrize("flag", ["phosphate", "hydroxyl", "atp"])
def test_nick_terminal_negative_controls(flag):
    assert M.seal_nick("AC", "GT", "TGCA") == "ACGT"
    with pytest.raises(ValueError):
        M.seal_nick("AC", "GT", "TGCA", **{flag: False})


def test_nick_is_not_gap_or_mismatch():
    for template in ["TGACA", "TGCT"]:
        with pytest.raises(ValueError):
            M.seal_nick("AC", "GT", template)


def test_extension_conserves_nucleotides_and_does_not_mutate_pool():
    pool = dict(A=1, C=1, G=1, T=1)
    grown, left, ppi = M.extend_primer("TGCATG", "AC", pool)
    assert grown == "ACGTAC" and ppi == 4
    assert sum(left.values()) == 0 and sum(pool.values()) == 4
    assert len(grown) - 2 == ppi == sum(pool.values()) - sum(left.values())
    assert (
        M.extend_primer("TGCATG", "AC", dict(A=9, C=9, G=0, T=9))[0] == "AC"
    )
    with pytest.raises(ValueError):
        M.extend_primer("TGCATG", "AG", pool)
    with pytest.raises(ValueError):
        M.extend_primer("TGCATG", "AC", pool, hydroxyl=False)


@pytest.mark.parametrize("kcat", [0, 0.1, 3, 20])
def test_mass_action_conservation_and_product_monotonicity(kcat):
    rows = M.integrate(0.02, 1, 2, 1, kcat, 2, 0.001)
    for t, e, s, c, p in rows:
        assert e + c == pytest.approx(0.02, abs=1e-13)
        assert s + c + p == pytest.approx(1, abs=1e-12)
        assert min(e, s, c, p) >= 0
    assert all(b[-1] >= a[-1] for a, b in zip(rows, rows[1:]))
    assert M.rhs((0.02, 1, 0, 0), 2, 1, kcat)[-1] == 0


def test_integrator_convergence_and_bad_step():
    oracle = M.integrate(0.02, 1, 2, 1, 3, 1, 0.0001)[-1]
    errors = []
    for dt in [0.05, 0.025, 0.0125]:
        got = M.integrate(0.02, 1, 2, 1, 3, 1, dt)[-1]
        errors.append(max(abs(a - b) for a, b in zip(got[1:], oracle[1:])))
    assert all(12 < a / b < 22 for a, b in zip(errors, errors[1:]))
    with pytest.raises(ValueError):
        M.integrate(0.02, 1, 2, 1, 3, 5, 5)


@pytest.mark.parametrize("t", [0, 0.01, 0.1, 1])
def test_clamped_independent_integrating_factor(t):
    c, p = M.clamped(0.02, 1, 2, 1, 3, t)
    assert c == pytest.approx(
        (0.02 / 3) * (1 - math.exp(-6 * t)), abs=1e-15
    )
    assert p == pytest.approx(
        0.02 * (t - (1 - math.exp(-6 * t)) / 6), abs=1e-15
    )
    assert c >= 0 and p >= 0


def test_small_enzyme_limit_and_saturation():
    full = M.integrate(1e-5, 1, 2, 1, 3, 1, 0.001)[-1]
    c, p = M.clamped(1e-5, 1, 2, 1, 3, 1)
    assert full[3] == pytest.approx(c, rel=2e-5)
    assert full[4] == pytest.approx(p, rel=2e-5)
    assert M.mm_rate(2, 0.02, 2, 1, 3) == pytest.approx(0.03)
    assert M.mm_rate(0, 0.02, 2, 1, 3) == 0
    assert M.mm_rate(1e9, 0.02, 2, 1, 3) == pytest.approx(0.06)


@pytest.mark.parametrize("bad", ["acgt", "N", ""])
def test_invalid_sequence(bad):
    with pytest.raises(ValueError):
        M.ecori_cut_sites(bad)


def test_record_matches_reference():
    assert json.loads(
        (ROOT / "drafts/ch08/results.json").read_text()
    ) == json.loads(json.dumps(M.results()))
