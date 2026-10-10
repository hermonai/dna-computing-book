# Current manuscript and repository guide

Updated 10 October 2026. Active content reaches Chapter 32, the final planned
DNA chapter. This is a complete authoring spine, not an accepted publication.

## Start here

- [Chapter 31 — Modern molecular programming and evidence](drafts/ch31/README.md)
- [Chapter 32 — From molecular computation to genomic computation](drafts/ch32/README.md)
- [Editorial architecture and release gates](EDITORIAL_ARCHITECTURE.md)
- [Package convergence matrix](research/integration/chapter-convergence-matrix.md)
- [Continuous PDF hash, review scope and open release gates](research/integration/continuous-through32-review.json)
- [Textbook standard](TEXTBOOK_STANDARD.md) and [chapter standard](CHAPTER_STANDARD.md)

## One manuscript, explicit stages

| Material | Active location | Status |
|---|---|---|
| Opening Chapters 1–3 | tex/ and TEXTBOOK_REVISION.md | Textbook review candidate |
| Chapters 4–21 | drafts/ch04/ through drafts/ch21/ | Authored standalone candidates |
| Expanded Chapter 17 | drafts/ch17-theory/ | Preferred theory extension; original retained |
| Chapters 22–32 | drafts/ch22/ through drafts/ch32/ | Source-bound locally reviewed candidates |
| Continuous Chapters 1–32 | output/pdf/dna-computing-convergence.pdf | Authored-source cumulative review candidate |
| Accepted Chapters 1–2 | book/book.json and acceptance records | Frozen, not superseded acceptance |
| Historical editions | Existing sources and preservation tests | Archives, not parallel authoring |

All dna-computing-ch22-r01.zip through dna-computing-ch32-r01.zip packages are
inventoried and semantically integrated. In particular, the requested Chapter
30/31/32 ZIPs were used; preserved incoming metadata is provenance, not local proof.
Review records bind authored source, PDF hashes and regression evidence.

## Build and verify

Use Python 3.13.6 at /Users/wenyan/.pyenv/versions/3.13.6/bin/python3.

- Chapter builders: drafts/chNN/build.py --render; --check verifies computed assets.
- Continuous build: scripts/build-convergence.py --through 32 --refresh-assets.
- Regression: python -m pytest -q -o addopts=''.
- Do not build PDFs concurrently with preservation tests in the same repository.

The continuous builder assembles authored LaTeX with reconciled bibliography,
global glossary, index and chapter references. The pedagogical acknowledgment
appears once in front matter. A successful build is not cumulative visual review.

## Folder and cleanup policy

Authored drafts/, tex/, figures/, examples/ and tests/ are source, not cache.
research/integration/ contains durable provenance and local evidence.
output/pdf/ holds readable review PDFs and preserved editions; inspect provenance
before removing anything. build/ contains generated tables, listings, compiler
outputs and logs. tmp/pdfs/ contains regenerable visual-review pages.

On 27 September 2026, the books' legacy build trees (1,148 files, about 102 MB
combined) were moved to a dated macOS Trash archive with a recovery receipt.
Authored files, review records, accepted PDFs and historical editions were retained.
Future cleanup must resolve exact targets and archive rather than delete broadly.

## DNA release work remains

The content spine closes with finite-fuel realization and scoped evidence (31),
then constructive information-loss proofs and molecular/genomic synthesis (32).
Full regression: 1,400 passed, 2 skipped. New standalone PDFs: 15 and 14 pages;
each has six vector/TXT plates and twenty worked exercises.

Remaining gates: cumulative line-by-line scientific/editorial review, complete
continuous-edition visual QA, bibliography/notation/index reconciliation beyond
automated closure, independent specialist review and real-reader evaluation.
Chapter acceptance and full-book convergence remain false in the inventory.
BOOK_PLAN.md stays the generated frozen acceptance snapshot, not a live progress
counter. Do not regenerate legacy editions or promote their acceptance records.
