"""Bind the separate expanded edition without promoting cumulative acceptance."""

from pathlib import Path
import hashlib
import json
import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_expanded_review_binds_sources_and_preserves_original():
    record = json.loads(
        (ROOT / "artifacts/deep/ch17-theory-review.json").read_text()
    )
    actual = {
        str(p.relative_to(ROOT))
        for p in (ROOT / "drafts/ch17-theory").rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    }
    assert set(record["sources"]) == actual
    for path, digest in record["sources"].items():
        assert (
            hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
        )
    assert record["allPagesInspected"]
    assert record["inspectedPhysicalPages"] == list(
        range(1, record["pages"] + 1)
    )
    assert (record["figures"], record["exercises"]) == (8, 18)
    assert record["status"].endswith("no acceptance promotion")
    assert "independent specialist review" in record["openGates"]
    figures = ROOT / "drafts/ch17-theory/figures"
    assert len(list(figures.glob("*.tex"))) == 8
    assert {p.stem for p in figures.glob("*.tex")} == {
        p.stem for p in figures.glob("*.txt")
    }
    assert (
        len(json.loads((ROOT / "book/book.json").read_text())["chapters"])
        == 2
    )
    original = json.loads(
        (ROOT / "artifacts/deep/ch17-review.json").read_text()
    )
    for path, digest in original["sources"].items():
        assert (
            hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
        )


def test_expanded_local_pdf_matches_review_when_available():
    record = json.loads(
        (ROOT / "artifacts/deep/ch17-theory-review.json").read_text()
    )
    path = ROOT / record["pdf"]
    if not path.exists():
        pytest.skip("Review PDF is generated and gitignored")
    assert hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"]
