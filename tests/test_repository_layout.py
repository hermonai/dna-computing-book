"""Canonical source closure and byte-preserving archival boundaries."""

import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from textwrap import dedent

import pytest

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "archive/legacy/dna-computing-book"
MANIFEST = json.loads((ROOT / "book/book.json").read_text())


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


B = load("canonical_builder", "scripts/build_book.py")
V = load("archive_verifier", "scripts/verify_archive.py")
REVIEW = load("pdf_review_tool", "scripts/review_pdf.py")


def test_one_current_edition_and_exact_order():
    chapters = MANIFEST["chapters"]
    assert [c["number"] for c in chapters] == list(range(1, 33))
    assert [c["source"] for c in chapters] == [
        f"book/chapters/ch{n:02d}/manuscript.tex" for n in range(1, 33)
    ]
    assert MANIFEST["main"] == "book/main.tex"
    assert "review pending" in MANIFEST["status"]
    assert not (ROOT / "tex").exists() and not (ROOT / "drafts").exists()
    assert not (ROOT / "book/chapters/ch17-theory").exists()
    assert [p.name for p in (ROOT / "scripts").glob("build*.py")] == ["build_book.py"]


@pytest.mark.parametrize(
    "entry", MANIFEST["chapters"], ids=lambda e: f"ch{e['number']:02d}"
)
def test_relocated_numerical_source_is_byte_identical(entry):
    reference = Path(entry["reference"])
    if entry["number"] <= 2:
        previous = f"examples/deep/ch{entry['number']:02d}.py"
    else:
        previous = str(Path(entry["previous_source"]).with_name("reference.py"))
        if entry["number"] == 3:
            previous = "drafts/ch03/reference.py"
    assert (ROOT / reference).read_bytes() == (LEGACY / previous).read_bytes()
    assert (ROOT / entry["source"]).is_file()


@pytest.mark.parametrize("n", range(4, 33))
def test_current_generated_values_and_listings(n):
    for path, expected in B.generated_assets(n).items():
        assert path.read_text() == expected
    source = (B.chapter_dir(n) / "reference.py").read_text()
    # Whole generated functions/classes are literal fragments of tested code.
    lines = source.splitlines()
    generated = ROOT / f"build/generated/ch{n:02d}"
    for listing in generated.glob("*.py"):
        assert listing.read_text().strip() in source
        ast.parse(dedent(listing.read_text()))
    assert lines


def test_all_original_archived_bytes_and_release_records():
    result = V.verify()
    assert result["verified_entries"] >= 1135
    manifest = json.loads((ROOT / "archive/manifest.json").read_text())
    assert len(manifest["legacy_tracked_files"]) == 1135
    assert len(manifest["legacy_pdf_hashes"]) == 40
    assert manifest["baseline_commit"].startswith("6bc4259")
    for p in ("artifacts/deep/ch01-review.json", "artifacts/deep/ch02-review.json"):
        record = json.loads((LEGACY / p).read_text())
        for relative, digest in record["reviewedSources"].items():
            assert (
                hashlib.sha256((LEGACY / relative).read_bytes()).hexdigest() == digest
            )


def test_single_bibliography_resolves_every_citation():
    """One authored BibTeX database; every \\cite resolves; no duplicate works."""
    keys = B.bib_keys()
    assert len(keys) >= 100
    with pytest.raises(ValueError, match="Duplicate"):
        B.bib_keys("@article{x,\n title={A}}\n@book{x,\n title={B}}\n")
    assert B.cited_keys(r"\cite{a, b}\citep[p.~3]{c}") == ["a", "b", "c"]
    cmap = B.citation_map()
    assert set(cmap) <= keys and len(cmap) >= 100
    text = B.BIB.read_text()
    dois = [d.lower() for d in re.findall(r"doi = \{([^}]+)\}", text)]
    assert len(dois) == len(set(dois)), "the same DOI appears in two records"
    # Chapter sources no longer carry private bibliographies.
    for path in (ROOT / "book").rglob("*.tex"):
        assert "\\begin{thebibliography}" not in path.read_text(), path


def test_parts_cover_the_chapter_sequence():
    parts = MANIFEST["parts"]
    firsts = [p["first_chapter"] for p in parts]
    assert firsts == sorted(firsts) and firsts[0] == 1 and len(parts) == 8
    for p in parts:
        assert (ROOT / p["source"]).is_file()
    for item in MANIFEST["frontmatter"] + MANIFEST["backmatter"]:
        assert (ROOT / item).is_file(), item


def test_svg_names_are_unique_and_tex_sources_are_local():
    paths = list((ROOT / "book/chapters").rglob("*.svg"))
    assert len(paths) == len({p.stem for p in paths})
    for p in paths:
        assert p.with_suffix(".txt").exists()
    for n in range(4, 33):
        figures = ROOT / f"book/chapters/ch{n:02d}/figures"
        assert {p.stem for p in figures.glob("*.tex")} == {
            p.stem for p in figures.glob("*.txt")
        }
    inputs = []
    for p in (ROOT / "book").rglob("*.tex"):
        for target in re.findall(
            r"\\(?:input|VerbatimInput)(?:\[[^]]*\])?\{([^}]+)\}", p.read_text()
        ):
            inputs.append(target)
            assert "archive/" not in target
    assert inputs


def test_default_build_is_full_book_not_frozen_edition():
    make = (ROOT / "Makefile").read_text()
    assert ".DEFAULT_GOAL := pdf" in make
    recipe = make.split("pdf:\n")[1].split("\n\n")[0]
    assert "scripts/build_book.py" in recipe
    assert "legacy" not in recipe and "deep-dna" not in recipe


def test_manuscript_has_no_retired_chapter_build_commands():
    for chapter in MANIFEST["chapters"]:
        prose = (ROOT / chapter["source"]).read_text()
        assert "build.py" not in prose
        assert "--assets-only" not in prose
        assert "drafts/" not in prose


def test_page_range_parser_and_invalid_scope():
    assert REVIEW.selected_pages("1-3,2,398", 398) == [1, 2, 3, 398]
    assert REVIEW.selected_pages("all", 3) == [1, 2, 3]
    for value in ("0", "399", "4-1", "1-2-3", ""):
        with pytest.raises(ValueError):
            REVIEW.selected_pages(value, 398)


def test_shared_contract_still_matches_actual_evolutor_checkout():
    sibling = ROOT.parent / "evolutor-book/pedagogy"
    if not sibling.is_dir():
        pytest.skip("Sibling checkout is not part of this repository")
    for name in ("book-i-contract.json", "deep-book-i-contract.json"):
        assert json.loads((LEGACY / "pedagogy" / name).read_text()) == json.loads(
            (sibling / name).read_text()
        )
