"""Prepublication Chapter 3 controls; do not activate the draft in the PDF."""
import importlib.util
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import subprocess
import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_working_artifacts_and_diagram_contract():
    import xml.etree.ElementTree as ET
    build_spec = importlib.util.spec_from_file_location("ch03_draft_builder", ROOT / "drafts/ch03/build_assets.py")
    builder = importlib.util.module_from_spec(build_spec)
    build_spec.loader.exec_module(builder)
    for name, content in builder.outputs().items():
        assert (ROOT / "drafts/ch03" / name).read_text() == content, name
    storyboard = json.loads((ROOT / "drafts/ch03/storyboard.json").read_text())
    assert len(storyboard["figures"]) == 12
    produced = [f for f in storyboard["figures"] if f["status"] == "produced-draft-svg-txt"]
    assert len(produced) == 8
    manuscript = (ROOT / "drafts/ch03/manuscript.md").read_text()
    assert manuscript.count("**Solution:**") == 12
    for figure in produced:
        assert "figures/" + figure["id"] + ".svg" in manuscript
        folder = ROOT / "drafts/ch03/figures"
        svg = ET.fromstring((folder / (figure["id"] + ".svg")).read_text())
        assert svg.attrib["aria-labelledby"] == "title desc"
        assert svg.find("{http://www.w3.org/2000/svg}title").text
        assert svg.find("{http://www.w3.org/2000/svg}desc").text
        assert not svg.findall(".//{http://www.w3.org/2000/svg}image")
        text = (folder / (figure["id"] + ".txt")).read_text()
        assert not set("┌└│─") & set(text)
        for section in ("QUESTION", "OBJECTS", "RELATION / MECHANISM", "INFERENCE", "BOUNDARY", "SOURCE"):
            assert section in text


spec = importlib.util.spec_from_file_location("dna_ch03_draft", ROOT / "drafts/ch03/reference.py")
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def all_graphs(n):
    possible = [(u, v) for u in range(n) for v in range(n) if u != v]
    for choices in product((False, True), repeat=len(possible)):
        yield frozenset(e for e, keep in zip(possible, choices) if keep)


def test_subset_search_on_all_4096_four_vertex_graphs():
    for edges in all_graphs(4):
        expected = M.permutation_oracle(4, edges, 0, 3)
        actual = M.subset_search(4, edges, 0, 3)
        assert (actual["route"] is not None) == bool(expected)
        if actual["route"] is not None:
            assert actual["route"] in expected
        assert sum(actual["states_by_cardinality"]) == actual["reachable_states"]


def test_reduction_both_directions_all_three_vertex_graphs_and_pivots():
    for edges in all_graphs(3):
        cycle_exists = any(all(e in edges for e in zip(p, p[1:] + p[:1]))
                           for p in permutations(range(3)))
        for pivot in range(3):
            r = M.cycle_to_path(3, edges, pivot)
            assert len(r["edges"]) == len(edges)
            assert all(v != r["start"] and u != r["end"] for u, v in r["edges"])
            assert bool(M.permutation_oracle(r["n"], r["edges"], r["start"], r["end"])) == cycle_exists


def test_cnf_all_boolean_assignments_not_only_permutations():
    for edges in all_graphs(3):
        clauses = M.path_cnf(3, edges, 0, 2)
        accepted = set()
        for assignment in product((False, True), repeat=9):
            if M.satisfies(clauses, assignment):
                route = M.decode_assignment(3, assignment)
                assert M.verify(3, edges, 0, 2, route)
                accepted.add(route)
        assert accepted == set(M.permutation_oracle(3, edges, 0, 2))


def test_cnf_clause_size_derivation():
    for n in range(2, 7):
        edges = frozenset((v, v + 1) for v in range(n - 1))
        clauses = M.path_cnf(n, edges, 0, n - 1)
        expected = 2 * n + n * n * (n - 1) + 2 + (n - 1) * (n * n - len(edges))
        assert len(clauses) == expected
        assert M.satisfies(clauses, M.encode_route(n, tuple(range(n))))


def test_decision_self_reduction_all_small_graphs():
    for edges in all_graphs(3):
        result = M.search_via_decision(3, edges, 0, 2)
        expected = M.permutation_oracle(3, edges, 0, 2)
        if expected:
            assert result["route"] in expected
            assert len(result["kept_edges"]) == 2
            assert result["oracle_calls"] == len(edges) + 1
        else:
            assert result["route"] is None and result["oracle_calls"] == 1


def test_self_reduction_trace_against_independent_enumeration():
    for edges in all_graphs(4):
        result = M.search_via_decision(4, edges, 0, 3)
        if not M.permutation_oracle(4, edges, 0, 3):
            assert result["trace"] == []
            continue
        kept = set(edges)
        assert len(result["trace"]) == len(edges)
        for query, (edge, row) in enumerate(zip(sorted(edges), result["trace"]), 2):
            assert tuple(row["edge"]) == edge and row["query"] == query
            trial = kept - {edge}
            yes = bool(M.permutation_oracle(4, trial, 0, 3))
            assert row["trial_has_path"] == yes
            assert row["action"] == ("delete" if yes else "retain")
            if yes:
                kept = trial
            assert set(map(tuple, row["kept_edges"])) == kept
            assert M.permutation_oracle(4, kept, 0, 3)
        assert kept == set(zip(result["route"], result["route"][1:]))


def test_dense_state_counts_have_independent_closed_form():
    for n in range(3, 9):
        edges = [(u, v) for u in range(n) for v in range(n) if u != v]
        result = M.subset_search(n, edges, 0, n - 1)
        # Start + terminal + (chosen last interior, arbitrary other interior subset).
        assert result["reachable_states"] == 2 + (n - 2) * 2 ** (n - 3)
    assert M.subset_search(2, [(0, 1)], 0, 1)["reachable_states"] == 2


@pytest.mark.parametrize("n,edges", [(1, []), (True, []), (3, [(0, 3)]),
    (3, [(1, 1)]), (3, [(False, 1)]), (3, [(0, 1, 2)])])
def test_invalid_graphs(n, edges):
    with pytest.raises(ValueError):
        M.graph(n, edges)


@pytest.mark.parametrize("route", [(), (0, 1), (0, 1, 1, 3), (0, 1, 2, 4),
    (0, True, 2, 3), (3, 2, 1, 0), (0, 2, 1, 3)])
def test_invalid_certificates(route):
    assert not M.verify(4, [(0, 1), (1, 2), (2, 3)], 0, 3, route)


@pytest.mark.parametrize("endpoints", [(0, 0), (-1, 2), (0, 3), (False, 2)])
def test_invalid_endpoints(endpoints):
    with pytest.raises(ValueError):
        M.subset_search(3, [], *endpoints)


def test_assignment_boundary_checks():
    with pytest.raises(ValueError):
        M.decode_assignment(3, (False,) * 9)
    with pytest.raises(ValueError):
        M.satisfies([(0,)], [False])
    with pytest.raises(ValueError):
        M.satisfies([(2,)], [False])
    assert M.satisfies([], [True])
    assert not M.satisfies([()], [True])


def test_published_release_is_untouched():
    release = "aa0bb1fa7c7320ece08cd177a4ba59c03507eba7"
    review = json.loads((ROOT / "artifacts/deep/ch02-review.json").read_text())
    for path, digest in review["reviewedSources"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    for path in ("artifacts/deep/ch02-review.json", "output/pdf/deep-dna-computing-ch01-02.pdf"):
        assert (ROOT / path).read_bytes() == subprocess.check_output(["git", "show", release + ":" + path], cwd=ROOT)
    assert len(json.loads((ROOT / "book/book.json").read_text())["chapters"]) == 2
