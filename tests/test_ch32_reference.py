import importlib.util
import itertools
from pathlib import Path
import sys
import math
import pytest

spec = importlib.util.spec_from_file_location(
    "dna32", Path(__file__).parents[1] / "book/chapters/ch32/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_exhaustive_short_strings():
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    for length in range(6):
        for chars in itertools.product("ACGT", repeat=length):
            s = "".join(chars)
            expected = "".join(complement[b] for b in reversed(s))
            assert m.rc(s) == expected and m.rc(m.rc(s)) == s
            assert m.decode_one_hot(m.one_hot(s)) == s


@pytest.mark.parametrize("s", ["N", "a", "AU", "AC GN", 1, None])
def test_canonical_rejection(s):
    with pytest.raises(ValueError):
        m.one_hot(s)


@pytest.mark.parametrize(
    "row",
    [
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0],
        [True, 0, 0, 0],
        [1.0, 0, 0, 0],
        [float("nan"), 0, 0, 1],
    ],
)
def test_strict_integer_encoding(row):
    with pytest.raises(ValueError):
        m.decode_one_hot([row])


def test_constructive_concentration_counterexample():
    x = m.Molecule("ACGT", "forward", 1.0, "buffer")
    y = m.Molecule("ACGT", "forward", 10.0, "buffer")
    assert m.sequence_projection(x) == m.sequence_projection(y)
    assert m.collision_witness(
        [x, y], m.sequence_projection, lambda z: z.concentration
    ) == (x, y)
    # bimolecular capture with k=.1, A=.2: velocities differ tenfold.
    assert 0.1 * 0.2 * y.concentration == pytest.approx(
        10 * 0.1 * 0.2 * x.concentration
    )


def test_no_finite_witness_is_not_universal_proof():
    x = m.Molecule("A", "forward", 1.0, "b")
    assert (
        m.collision_witness([x], m.sequence_projection, lambda z: z.concentration)
        is None
    )


@pytest.mark.parametrize("concentration", [-1, float("nan"), float("inf"), True])
def test_sample_domain(concentration):
    with pytest.raises(ValueError):
        m.Molecule("A", "forward", concentration, "b")


def test_frame_cannot_disappear_in_lossless_encoding():
    x = m.Molecule("A", "forward", 1.0, "b")
    y = m.Molecule("A", "reverse", 1.0, "b")
    assert m.sequence_projection(x) != m.sequence_projection(y)
    assert m.one_hot(x.bases) == m.one_hot(y.bases)  # naked tensor loses external frame


def test_property_gate_does_not_create_metadata():
    source = m.Representation("molecule", frozenset({"base", "frame", "concentration"}))
    sequence = m.project(source, "sequence", {"base", "frame"})
    assert m.supports(sequence, {"base", "frame"})
    assert not m.supports(sequence, {"concentration"})
    with pytest.raises(ValueError):
        m.project(sequence, "kinetics", {"base", "concentration"})


@pytest.mark.parametrize("n", [1, 2, 4, 10])
def test_paired_statistics_independent_formula(n):
    a = [0.1 * i for i in range(n)]
    d = [0.01 * (i + 1) for i in range(n)]
    b = [x + y for x, y in zip(a, d)]
    result = m.paired_effect(a, b)
    mean = sum(d) / n
    assert result["mean"] == pytest.approx(mean)
    if n == 1:
        assert result["sample_sd"] is None and result["standard_error"] is None
    else:
        sd = math.sqrt(sum((x - mean) ** 2 for x in d) / (n - 1))
        assert result["sample_sd"] == pytest.approx(sd)
        assert result["standard_error"] == pytest.approx(sd / math.sqrt(n))


def test_factorial_interaction_manual():
    r = m.results()["factorial"]
    assert r["transplant"]["mean"] == pytest.approx(0.0275)
    assert r["ablation"]["mean"] == pytest.approx(0.0375)
    assert r["interaction"]["mean"] == pytest.approx(0.01)


@pytest.mark.parametrize("args", [([], []), ([1], [1, 2]), ([1], [float("nan")])])
def test_bad_pairs(args):
    with pytest.raises(ValueError):
        m.paired_effect(*args)


def test_mismatched_seed_panels():
    with pytest.raises(ValueError):
        m.factorial_effect([1], [2], [1, 2], [2, 3])


def test_full_model_gain_does_not_imply_mechanism_gain():
    r = m.factorial_effect([0.5, 0.5], [0.5, 0.5], [0.8, 0.8], [0.8, 0.8])
    assert r["transplant"]["mean"] == r["ablation"]["mean"] == 0
