"""Canonical deep Chapter 1: exact semantics, assets, and publication checks."""

from fractions import Fraction
from itertools import product
import importlib.util
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]
DNA = ROOT.name == "dna-computing-book"
PREFIX = "DNAD-01" if DNA else "EVOD-01"
NAME = "deep-dna-computing" if DNA else "deep-evolutor"
NAME += "-ch01-02"


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M = module("chapter", "book/chapters/ch01/reference.py")


if DNA:

    @pytest.mark.parametrize(
        "route,valid",
        [
            ("ABCDEF", True),
            ("ACBDEF", True),
            ("ABCBDF", False),
            ("ABDEF", False),
            ("ABECDF", False),
            ("", False),
            ("FABCDE", False),
            ("ABCDEZ", False),
        ],
    )
    def test_hamiltonian_conditions(route, valid):
        assert M.is_hamiltonian(tuple(route)) is valid

    def test_stage_counts_and_independent_permutation_oracle():
        stages = M.filter_pool(M.walks())
        assert [len(p) for _, p in stages] == [106, 14, 4, 2, 2]
        assert (
            set(stages[-1][1])
            == set(M.permutation_oracle())
            == {tuple("ABCDEF"), tuple("ACBDEF")}
        )
        assert all(M.edge_valid(p) for p in stages[0][1])

    def test_fault_injection_preserves_multiplicity_until_verification():
        stages = M.filter_pool(M.walks() + [tuple("ABECDF")] * 10)
        assert [len(p) for _, p in stages] == [116, 24, 14, 12, 2]
        assert len(M.filter_pool([tuple("ABCDEF")] * 3)[-1][1]) == 3

    def test_small_graphs_differential_oracle():
        vertices = tuple("ABC")
        possible = [e for e in product(vertices, repeat=2) if e[0] != e[1]]
        for flags in product((False, True), repeat=len(possible)):
            edges = frozenset(e for e, keep in zip(possible, flags) if keep)
            actual = set(
                M.filter_pool(M.walks(3, vertices, edges), vertices, edges, "A", "C")[
                    -1
                ][1]
            )
            expected = set(M.permutation_oracle(vertices, edges, "A", "C"))
            assert actual == expected

    @pytest.mark.parametrize("bound", [0, -1, 1.5, True, None])
    def test_walk_bound_rejected(bound):
        with pytest.raises(ValueError):
            M.walks(bound)

    @pytest.mark.parametrize(
        "p,delta",
        [(1 / 24, 0.01), (1 / 12, 0.01), (0.2, 0.1), (0.001, 0.05), (0.5, 0.2)],
    )
    def test_sampling_threshold_minimality(p, delta):
        n = M.required_samples(p, delta)
        assert (1 - p) ** n <= delta
        assert (1 - p) ** (n - 1) > delta

    @pytest.mark.parametrize(
        "p,delta",
        [(0, 0.1), (-0.1, 0.1), (1.1, 0.1), (0.5, 0), (0.5, 1), (float("nan"), 0.1)],
    )
    def test_invalid_sampling_domains(p, delta):
        with pytest.raises(ValueError):
            M.required_samples(p, delta)

    def test_boundary_values_and_reverse_complement():
        assert M.required_samples(1, 0.1) == 1
        assert M.required_samples(1 / 24, 0.01) == 109
        assert M.required_samples(1 / 12, 0.01) == 53
        assert M.reverse_complement("ACGA") == "TCGT"
        for letters in product("ACGT", repeat=4):
            s = "".join(letters)
            assert M.reverse_complement(M.reverse_complement(s)) == s
        with pytest.raises(ValueError):
            M.reverse_complement("AN")
else:

    @pytest.mark.parametrize("context", ["bounded", "balanced"])
    def test_exact_baseline_equivalence_and_invariants(context):
        for xs in product(
            [Fraction(-2), Fraction(-1, 2), Fraction(0), Fraction(3, 2)], repeat=3
        ):
            out, trace = M.execute(M.select(context), xs)
            assert out == M.direct_baseline(context, xs)
            assert len(out) == len(xs) and len(trace) == 2
            assert trace[0]["before"] == xs and trace[-1]["after"] == out
            if context == "bounded":
                assert all(x >= 0 for x in out) and all(
                    a <= b for a, b in zip(out, out[1:])
                )
            else:
                assert out[-1] == 0

    def test_expected_traces_and_plan_order():
        assert M.execute(M.select("bounded"), (3, -1, 2))[0] == (3, 3, 5)
        assert M.execute(M.select("balanced"), (3, -1, 2))[0] == (
            Fraction(5, 3),
            Fraction(-2, 3),
            0,
        )
        assert M.execute(("prefix", "clip"), (3, -1, 2))[0] == (3, 2, 4)
        assert M.execute((), (1, 2))[0] == (1, 2)
        with pytest.raises(TypeError):
            M.CATALOG["other"] = M.prefix

    @pytest.mark.parametrize("bad", [0, -1, 1.5, True, None])
    def test_development_domain(bad):
        with pytest.raises(ValueError):
            M.develop(bad)

    def test_development_has_no_learning_and_exact_composition():
        assert M.develop(2) == ("prefix", "prefix")
        assert M.execute(M.develop(2), (3, -1, 2))[0] == (3, 5, 9)
        assert M.execute(M.develop(3), (3, -1, 2))[0] == (3, 8, 17)

    @pytest.mark.parametrize("context", ["", "other", None])
    def test_unknown_context_rejected(context):
        with pytest.raises(ValueError):
            M.select(context)
        with pytest.raises(ValueError):
            M.direct_baseline(context, (1,))

    def test_empty_data_and_unknown_modules_rejected():
        with pytest.raises(ValueError):
            M.execute(("center",), ())
        with pytest.raises(ValueError):
            M.execute(("missing",), (1,))
        with pytest.raises(ValueError):
            M.center(())
        with pytest.raises(ValueError):
            M.direct_baseline("bounded", ())

    @pytest.mark.parametrize("index", range(7))
    def test_memory_dimension_domain(index):
        dims = [1, 24, 4096, 8, 64, 2048, 2]
        dims[index] = 0
        with pytest.raises(ValueError):
            M.memory_bytes(*dims)

    def test_memory_exact_units_and_scaling():
        a = M.memory_bytes(1, 24, 4096, 8, 64, 2048, 2)
        assert a == {"kv": 192 * 1024**2, "fixed_state": 96 * 1024}
        b = M.memory_bytes(1, 24, 8192, 8, 64, 2048, 2)
        c = M.memory_bytes(2, 24, 8192, 8, 64, 2048, 2)
        assert b["kv"] == 2 * a["kv"] and b["fixed_state"] == a["fixed_state"]
        assert c == {k: 2 * v for k, v in b.items()}
