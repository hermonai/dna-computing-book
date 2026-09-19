import importlib.util
from itertools import product
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_review_record_binds_complete_authored_source_set():
    import hashlib
    import json

    record = json.loads(
        (ROOT / "artifacts/deep/ch05-review.json").read_text()
    )
    actual = {
        str(p.relative_to(ROOT))
        for p in (ROOT / "drafts/ch05").rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    }
    assert set(record["sources"]) == actual
    for path, digest in record["sources"].items():
        assert (
            hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
        )
    assert record["allPagesInspected"]
    assert record["figures"] == 5 and record["exercises"] == 12
    assert record["status"].endswith("no acceptance promotion")
    assert record["openGates"]
    assert (
        len(json.loads((ROOT / "book/book.json").read_text())["chapters"])
        == 2
    )
    figures = ROOT / "drafts/ch05/figures"
    assert len(list(figures.glob("*.tex"))) == 5
    assert {p.stem for p in figures.glob("*.tex")} == {
        p.stem for p in figures.glob("*.txt")
    }


def test_local_pdf_matches_review_when_available():
    import hashlib
    import json

    record = json.loads(
        (ROOT / "artifacts/deep/ch05-review.json").read_text()
    )
    path = ROOT / record["pdf"]
    if not path.exists():
        pytest.skip("Review PDF is generated and gitignored")
    assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"]


spec = importlib.util.spec_from_file_location(
    "dna05", ROOT / "drafts/ch05/reference.py"
)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def test_known_orientation_not_only_involution():
    assert M.complement("ACGTA") == "TGCAT"
    assert M.reverse_complement("ACGTA") == "TACGT"
    assert M.reverse_complement("ACGTA") != "ACGTA"[::-1]
    assert M.compatible_aligned("ACGTA", "TGCAT")
    assert not M.compatible_aligned("ACGTA", "TACGT")


@pytest.mark.parametrize("n", range(7))
def test_exhaustive_canonical_involution_and_palindromes(n):
    count = 0
    for row in product("ACGT", repeat=n):
        s = "".join(row)
        r = M.reverse_complement(s)
        assert M.reverse_complement(r) == s
        count += s == r
    assert count == M.palindrome_count(n)


def test_ambiguity_is_complement_of_sets():
    for symbol, bases in M.SETS.items():
        transformed = M.COMPLEMENT[symbol]
        assert set(M.SETS[transformed]) == {
            dict(A="T", T="A", C="G", G="C")[b] for b in bases
        }
        assert M.COMPLEMENT[transformed] == symbol
    assert M.reverse_complement("ARYN") == "NRYT"
    assert set(M.expansions("ARN")) == {
        "AAA",
        "AAC",
        "AAG",
        "AAT",
        "AGA",
        "AGC",
        "AGG",
        "AGT",
    }
    assert M.compatible_aligned("R", "Y")
    assert not M.compatible_aligned("R", "R")


def test_every_interval_identity_including_empty_and_edges():
    s = "ACGTRYNAC"
    for a in range(len(s) + 1):
        for b in range(a, len(s) + 1):
            c, d = M.reverse_interval(len(s), a, b)
            assert d - c == b - a
            assert M.reverse_complement(s)[c:d] == M.reverse_complement(
                s[a:b]
            )
            assert M.reverse_interval(len(s), c, d) == (a, b)


@pytest.mark.parametrize("s", ["acgt", "AC U", "AC-U", "AX", "AU", None])
def test_invalid_strings_rejected(s):
    with pytest.raises(ValueError):
        M.reverse_complement(s)


@pytest.mark.parametrize(
    "args", [(5, -1, 3), (5, 3, 2), (5, 0, 6), (True, 0, 1), (5, 0.0, 3)]
)
def test_invalid_intervals(args):
    with pytest.raises(ValueError):
        M.reverse_interval(*args)


def test_expansion_budget_and_empty_contract():
    assert M.expansions("") == [""]
    assert M.reverse_complement("") == ""
    with pytest.raises(ValueError):
        M.expansions("N" * 7)


def test_generated_results():
    import json

    assert (
        json.loads((ROOT / "drafts/ch05/results.json").read_text())
        == M.results()
    )


def test_chunk_order_and_nonpalindromic_coordinate_example():
    for x in ("", "AC", "RY", "N"):
        for y in ("GTA", "", "BD"):
            assert M.reverse_complement(x + y) == (
                M.reverse_complement(y) + M.reverse_complement(x)
            )
    r = M.results()["interval"]
    assert r["substring"] == "GTAG" and r["rc_substring"] == "CTAC"
    assert r["reversed"] == [3, 7]


def test_existential_matching_does_not_claim_universal_pairing():
    assert M.compatible_aligned("R", "Y")
    assert not M.compatible_aligned("A", "C")
    assert M.compatible_aligned("", "")
    assert not M.compatible_aligned("A", "")
    assert M.reverse_complement("N") == "N"
    assert M.palindrome_count(1) == 0  # count is canonical-alphabet only
