from pathlib import Path
import importlib.util
import sys
import json
import pytest
from itertools import product

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "ch11_reference_tests", ROOT / "drafts/ch11/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_reverse_complement_is_involution_and_not_plain_complement():
    assert m.revcomp("AACG") == "CGTT"
    for letters in product("ACGT", repeat=4):
        s = "".join(letters)
        assert m.revcomp(m.revcomp(s)) == s


@pytest.mark.parametrize("s", ["", "acgt", "ACGN", "ACGU"])
def test_alphabet_rejected(s):
    with pytest.raises(ValueError):
        m.revcomp(s)


def test_shifted_match_defeats_hamming_only_screen():
    a, b = "ACGTAC", "TACGTA"
    assert m.hamming(a, b) == 6
    assert m.longest_match(a, m.revcomp(b)) == (5, 0, 1)


def test_match_dp_against_bruteforce():
    words = ["".join(p) for p in product("AC", repeat=4)]
    for a in words:
        for b in words:
            oracle = max(
                [0]
                + [
                    j - i
                    for i in range(len(a))
                    for j in range(i + 1, len(a) + 1)
                    if a[i:j] in b
                ]
            )
            size, i, j = m.longest_match(a, b)
            assert size == oracle
            assert a[i : i + size] == b[j : j + size]


def test_hairpin_loop_and_nonoverlap_contract():
    assert m.hairpins("GCGAAACGC") == [(0, 6)]
    assert m.hairpins("GCGAAACGC", loop=4) == []
    assert m.hairpins("GCGCGC", loop=3) == []
    assert m.hairpins("GCGCGC", loop=0) == [(0, 3)]


def test_library_certificate_and_infeasible_case():
    selected = m.results()["selected"]
    assert selected == ["AACGTCAG", "AGCTTCGA", "CCTAGTCA"]
    assert m.choose_library(selected, 3) == tuple(selected)
    assert m.choose_library(["AAAAAAAA", "CCCCCCCC"], 1) is None
    assert m.choose_library(selected, 4) is None
    assert m.choose_library(reversed(selected), 3) == tuple(selected)


def test_directed_edge_encoding_and_roundtrip():
    edge = m.encode_edges(m.CODE, m.EDGES)
    assert edge["B", "C"] == "GTCAGATC"
    assert edge["C", "B"] == "TGACCCTA"
    for length in range(1, 6):
        for path in product(m.CODE, repeat=length):
            if all(e in m.EDGES for e in zip(path, path[1:])):
                encoded = m.assemble(path, m.CODE, m.EDGES)
                assert encoded == "".join(m.CODE[v] for v in path)
                assert m.decode(encoded, m.CODE) == path
                assert len(encoded) == 8 * length


def test_assembly_and_decoder_reject_invalid_contracts():
    with pytest.raises(ValueError):
        m.assemble(("D", "A"), m.CODE, m.EDGES)
    for seq in ["AACG", "AAAAAAAA", m.CODE["A"] + "A"]:
        with pytest.raises(ValueError):
            m.decode(seq, m.CODE)
    with pytest.raises(ValueError):
        m.encode_edges({"A": "AACGTCAG", "B": "AACGTGCA"}, set())


def test_composition_creates_a_new_substring():
    left, right, target = "AACG", "TCAG", "CGTC"
    assert target not in left and target not in right
    assert (left + right).index(target) == 2


def test_generated_results():
    assert m.results() == json.loads(
        (ROOT / "drafts/ch11/results.json").read_text()
    )
