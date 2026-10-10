from itertools import permutations
import pytest
from minidna.pool_search import chapter_example, enumerate_walks, filter_pool, hamiltonian_filter


def test_chapter_counts_and_witnesses():
    result = chapter_example()
    assert [n for _, n in result.stages] == [45, 5, 3, 2]
    assert result.witnesses == (("s", "u", "v", "t"), ("s", "v", "u", "t"))


def test_all_three_vertex_simple_digraphs_against_permutation_oracle():
    vertices = ("a", "b", "c")
    possible = tuple(permutations(vertices, 2))
    for mask in range(1 << len(possible)):
        edges = frozenset(edge for i, edge in enumerate(possible) if mask & (1 << i))
        for start, end in permutations(vertices, 2):
            expected = {w for w in permutations(vertices) if w[0] == start and w[-1] == end
                        and all(pair in edges for pair in zip(w, w[1:]))}
            actual = hamiltonian_filter(vertices, edges, start, end)
            assert set(actual.witnesses) == expected


def test_incomplete_pool_cannot_prove_nonexistence():
    vertices = ("s", "t")
    edges = frozenset({("s", "t")})
    assert hamiltonian_filter(vertices, edges, "s", "t").witnesses
    assert not filter_pool((("s",),), vertices, edges, "s", "t").witnesses


def test_single_vertex_and_empty_solution():
    assert hamiltonian_filter(("a",), frozenset(), "a", "a").witnesses == (("a",),)
    assert not hamiltonian_filter(("a", "b"), frozenset(), "a", "b").witnesses


def test_invalid_inputs_are_rejected():
    with pytest.raises(ValueError):
        enumerate_walks(("a", "a"), frozenset(), 2)
    with pytest.raises(ValueError):
        enumerate_walks(("a",), frozenset({("a", "b")}), 2)
    with pytest.raises(ValueError):
        enumerate_walks(("a",), frozenset(), 0)
    with pytest.raises(ValueError):
        filter_pool((("a", "b"),), ("a", "b"), frozenset(), "a", "b")
    with pytest.raises(ValueError):
        hamiltonian_filter(("a",), frozenset(), "a", "b")


def test_exercise_counts_and_counterexample():
    vertices = ("s", "u", "v", "t")
    edges = frozenset({("s", "u"), ("s", "v"), ("u", "v"),
                       ("v", "u"), ("u", "t"), ("v", "t")})
    result = hamiltonian_filter(vertices, edges, "s", "t")
    assert [count for _, count in result.stages] == [26, 4, 2, 2]
    counterexample = ("s", "u", "v", "u", "t")
    assert set(counterexample) == set(vertices)
    assert not filter_pool((counterexample,), vertices, edges, "s", "t").witnesses
    complete = frozenset((a, b) for a in ("a", "b", "c") for b in ("a", "b", "c"))
    assert len(enumerate_walks(("a", "b", "c"), complete, 3)) == 39
