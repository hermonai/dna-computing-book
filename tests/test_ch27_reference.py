"""Independent vector/path oracles for finite multiset transition semantics."""

import importlib.util
import itertools
from pathlib import Path
import sys
import pytest

path = Path(__file__).parents[1] / "drafts/ch27/reference.py"
spec = importlib.util.spec_from_file_location("dna27", path)
r = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = r
spec.loader.exec_module(r)


def vector_oracle(initial, network, bound):
    """Enumerate paths, not a deduplicating BFS; dense integer arithmetic."""
    names = network.species
    start = tuple(initial.get(s, 0) for s in names)
    frontier, found, edges = {start}, {start: 0}, set()
    for step in range(bound):
        following = set()
        for x in frontier:
            for rule in network.rules:
                c = tuple(dict(rule.consume).get(s, 0) for s in names)
                p = tuple(dict(rule.produce).get(s, 0) for s in names)
                if all(a >= b for a, b in zip(x, c)):
                    y = tuple(a - b + d for a, b, d in zip(x, c, p))
                    following.add(y)
                    found.setdefault(y, step + 1)
                    edges.add((x, rule.name, y))
        frontier = following
    return found, edges


def dense(state, network):
    return tuple(dict(state).get(s, 0) for s in network.species)


@pytest.mark.parametrize(
    "value",
    [{"A": -1}, {"A": 1.2}, {"A": True}, (("A", 1), ("A", 0)), {" A": 1}, {"": 1}, []],
)
def test_reject_invalid_multisets(value):
    with pytest.raises(ValueError):
        r.canon(value)


def test_canonical_immutable_zero_removed():
    assert r.canon({"B": 0, "C": 2, "A": 1}) == (("A", 1), ("C", 2))


def test_exact_multiplicity_and_catalyst_precondition():
    rr = r.rule("catalyze", {"A": 2, "E": 1}, {"B": 1, "E": 1})
    assert not r.enabled({"A": 2}, rr)
    assert not r.enabled({"A": 1, "E": 1}, rr)
    assert r.fire({"A": 3, "E": 1}, rr) == (("A", 1), ("B", 1), ("E", 1))
    with pytest.raises(ValueError):
        r.fire({"A": 2}, rr)


@pytest.mark.parametrize(
    "network",
    [
        lambda: r.Network(("A", "A"), ()),
        lambda: r.Network(("A",), (r.rule("x", {}, {"B": 1}),)),
        lambda: r.Network(("A",), (r.rule("x", {}, {}), r.rule("x", {}, {}))),
        lambda: r.Network(["A"], ()),
        lambda: r.Rule("x", (("B", 1), ("A", 1)), ()),
    ],
)
def test_invalid_network_contract(network):
    with pytest.raises(ValueError):
        network()


def test_undeclared_state_rejected():
    with pytest.raises(ValueError):
        r.bounded_reachable({"ghost": 1}, r.assembly(), 2)


@pytest.mark.parametrize(
    "bound,cap", [(-1, 10), (True, 10), (1.5, 10), (2, 0), (2, True)]
)
def test_search_domains(bound, cap):
    with pytest.raises(ValueError):
        r.bounded_reachable({}, r.assembly(), bound, cap)


def test_exhaustive_independent_dense_path_oracle():
    n = r.assembly()
    for counts in itertools.product(range(3), repeat=3):
        initial = dict(zip(("A", "B", "C"), counts))
        for k in range(4):
            expected, _ = vector_oracle(initial, n, k)
            got = r.bounded_reachable(initial, n, k)
            assert {dense(s, n): d for s, d in got.depth.items()} == expected
            for x, label, y in got.edges:
                rr = next(rule for rule in n.rules if rule.name == label)
                # Independently replay with dense consume/produce, not fire().
                c, p = dict(rr.consume), dict(rr.produce)
                assert all(dict(x).get(s, 0) >= c.get(s, 0) for s in n.species)
                assert dense(y, n) == tuple(
                    dict(x).get(s, 0) - c.get(s, 0) + p.get(s, 0) for s in n.species
                )


def test_boundary_not_global_unreachability():
    n = r.assembly()
    got = r.bounded_reachable({"A": 1, "B": 1, "C": 1}, n, 1)
    assert got.complete_within_depth and not got.exhaustive_closure
    assert got.outside_successors == 1
    with pytest.raises(ValueError):
        r.witness(got, {"ABC": 1})


def test_closure_and_shortest_replay():
    initial = {"A": 1, "B": 1, "C": 1}
    got = r.bounded_reachable(initial, r.assembly(), 2)
    assert got.exhaustive_closure and len(got.terminals) == 1
    assert r.witness(got, {"ABC": 1}) == ("bind_AB", "bind_C")
    assert sorted(got.depth.values()) == [0, 1, 2]


def test_parallel_labels_self_loop_and_cycle_retained():
    n = r.Network(
        ("A", "B"),
        (
            r.rule("first", {"A": 1}, {"B": 1}),
            r.rule("second", {"A": 1}, {"B": 1}),
            r.rule("loop", {"A": 1}, {"A": 1}),
            r.rule("return", {"B": 1}, {"A": 1}),
        ),
    )
    got = r.bounded_reachable({"A": 1}, n, 2)
    assert len(got.depth) == 2 and len(got.edges) == 4
    assert {edge[1] for edge in got.edges} == {"first", "second", "loop", "return"}
    assert got.exhaustive_closure and not got.terminals
    assert r.witness(got, {"B": 1}) == ("first",)


def test_budget_has_unknown_boundary_and_sound_partial_witness():
    n = r.Network(
        ("A", "B", "C"),
        (r.rule("b", {"A": 1}, {"B": 1}), r.rule("c", {"A": 1}, {"C": 1})),
    )
    got = r.bounded_reachable({"A": 1}, n, 2, 2)
    assert got.status == "state_budget_exhausted"
    assert not got.complete_within_depth and not got.exhaustive_closure
    assert got.outside_successors is None
    assert r.witness(got, {"B": 1}) == ("b",)


def test_empty_rules_terminal_at_bound_zero():
    got = r.bounded_reachable({}, r.Network(("A",), ()), 0)
    assert got.exhaustive_closure and got.terminals == ((),)


def test_stoichiometry_and_left_nullspace_independent():
    n = r.assembly()
    expected = ((-1, 0), (-1, 0), (0, -1), (1, -1), (0, 1))
    assert r.stoichiometry(n) == expected
    weights = (1, 1, 1, 2, 3)
    assert all(
        sum(weights[i] * expected[i][j] for i in range(5)) == 0 for j in range(2)
    )
    got = r.bounded_reachable({"A": 1, "B": 1, "C": 1}, n, 2)
    assert all(
        sum(weights[i] * dense(s, n)[i] for i in range(5)) == 3 for s in got.depth
    )


def test_state_equation_is_not_sufficient():
    # Delta creates D, but the unchanged B catalyst is absent.
    n = r.Network(("A", "B", "D"), (r.rule("catalyst", {"B": 1}, {"B": 1, "D": 1}),))
    assert r.stoichiometry(n) == ((0,), (0,), (1,))
    target = (("A", 1), ("D", 1))  # x0 + S*1 is nonnegative.
    assert target not in r.bounded_reachable({"A": 1}, n, 5).depth


def test_missing_invariant_weight_is_not_silently_zero():
    with pytest.raises(ValueError):
        r.weighted_total({"A": 1}, {})
    assert not r.invariant_preserved(
        r.rule("magic", {"A": 1}, {"B": 2}), {"A": 1, "B": 1}
    )


def test_divergent_terminals_are_counterexample_not_acceptance():
    n = r.Network(
        ("A", "B", "C"),
        (r.rule("b", {"A": 1}, {"B": 1}), r.rule("c", {"A": 1}, {"C": 1})),
    )
    got = r.bounded_reachable({"A": 1}, n, 1)
    assert got.exhaustive_closure and set(got.terminals) == {(("B", 1),), (("C", 1),)}


def test_corrupt_predecessor_cycle_rejected():
    got = r.bounded_reachable({"A": 1}, r.Network(("A",), ()), 0)
    start = (("A", 1),)
    got.predecessor[start] = (start, "loop")
    with pytest.raises(ValueError):
        r.witness(got, start)
