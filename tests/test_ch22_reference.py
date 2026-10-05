import importlib.util
import math
import pytest
from pathlib import Path

P = Path(__file__).parents[1] / "drafts/ch22/reference.py"
s = importlib.util.spec_from_file_location("r", P)
r = importlib.util.module_from_spec(s)
s.loader.exec_module(r)


def test_xor_truth_and_oracle():
    A, _ = r.grow(12)
    z = r.oracle(12)
    assert all(A[p].bit == z[p] for p in z if p[0] > 0 and p[1] > 0)


def test_every_reference_attachment_is_unique():
    tiles = r.xor_tiles()
    A = r.seed(6)
    for y in range(1, 7):
        for x in range(1, 7):
            q = r.legal_tiles((x, y), A, tiles)
            assert len(q) == 1
            A[(x, y)] = q[0]


def test_mutant_creates_real_ambiguity():
    assert set(r.ambiguity_example()) == {"X10", "mutant"}


def test_finite_yield_limits():
    assert r.finite_yield(0, 100) == 1
    assert r.finite_yield(1, 1) == 0
    assert r.finite_yield(0.01, 100) < r.finite_yield(0.01, 10)


def test_no_single_input_attachment_at_tau2():
    tiles = r.xor_tiles()
    A = r.seed(3)
    # At (2,1), west neighbor is absent before (1,1) is placed: south support alone is 1.
    assert r.legal_tiles((2, 1), A, tiles) == []


@pytest.mark.parametrize("n", range(5))
def test_all_legal_growth_schedules_have_one_terminal(n):
    count, terminals = r.explore(n)
    assert count == math.comb(2 * n, n)  # independent lower-ideal counting identity
    assert len(terminals) == 1
    expected, _ = r.grow(n)
    assert terminals[0] == expected
    assert not any(
        r.legal_tiles(p, expected, r.xor_tiles()) for p in r.frontier(expected)
    )


@pytest.mark.parametrize("n", range(1, 4))
def test_seed_is_temperature_two_stable(n):
    assert r.minimum_cut(r.seed(n)) == 2


def test_produced_assembly_is_stable():
    a, _ = r.grow(2)
    assert r.minimum_cut(a) >= 2


def test_equal_label_with_unequal_strength_is_not_a_bond():
    assert r.bond(("a", 1), ("a", 2)) == 0
    assert r.bond(("a", 2), ("a", 1)) == 0


def test_mutant_changes_output_not_only_name():
    wrong = r.Tile("mutant", ("v0", 1), ("h0", 1), ("v1", 1), ("h0", 1), 0)
    count, terminals = r.explore(2, r.xor_tiles() + [wrong])
    assert count > math.comb(4, 2)
    assert {a[(1, 1)].bit for a in terminals} == {0, 1}
    assert len(terminals) > 1


@pytest.mark.parametrize("n", [-1, 1.5, True])
def test_invalid_size_is_rejected(n):
    with pytest.raises(ValueError):
        r.seed(n)


@pytest.mark.parametrize("p", [-0.1, 1.1, float("nan"), float("inf")])
def test_invalid_error_probability(p):
    with pytest.raises(ValueError):
        r.finite_yield(p, 4)


def test_empty_object_and_locking_limits():
    assert r.finite_yield(1, 0) == 1
    assert r.trap_probability(9, 1) == 0.1
    assert r.trap_probability(0, 1) == 1
    assert r.trap_probability(1, 0) == 0
    with pytest.raises(ValueError):
        r.trap_probability(0, 0)


def test_exploration_budget_is_not_a_terminal_certificate():
    with pytest.raises(RuntimeError, match="budget"):
        r.explore(4, max_states=3)
