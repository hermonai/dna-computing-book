# Chapter 1 development report

Date: 2026-09-05. Branch: `astra-rewrite`. This is one internally reviewed chapter, not a finished book or an independently peer-reviewed release.

## Delivered

[Canonical manuscript](tex/chapters/ch01.tex), [research and skeptical review](research/chapter-01-review.md), [claim ledger](research/claims-ledger.md), [example records](book/results/ch01.json), [canonical graph](book/diagrams/dna-g05.txt), and [generated SVG](book/figures/dna-g05.svg).

The chapter includes a concrete example, an elementary proposition with explicit premises, resource/evidence boundaries, six exercises and concise solution notes. The active PDF now contains a reader preface and Chapter 1 rather than reset-only typesetting demonstrations. Planned later chapters are not placeholders in the manuscript.

## Result and interpretation

The exact token pool shrinks 45 → 5 → 3 → 2 and returns two Hamiltonian-path witnesses. An independent permutation oracle checks all 64 simple three-vertex directed graphs across six ordered endpoint pairs. An incomplete pool can produce a false negative about solution existence even when all filters are correct. This is an original teaching example, not a molecular simulation or a replication of Adleman's experiment.

## Verification

- **33 tests passed**, including existing regression checks, byte-for-byte historical preservation, active links/manifest, graph contracts, example oracles and generated-record freshness.
- **12-page A4 PDF, version 1.7**, built with XeLaTeX/TeX Live 2025 and latexmk 4.86a. Final log checks passed: no errors, missing glyphs, undefined citations/references or overfull boxes.
- Rendered every final page with Poppler and inspected the complete contact sheet plus full-size proof/table and figure pages. Shortened the ending to eliminate a near-empty spillover page; re-rendered and inspected all 12 final pages. The exercise answer without the self-loop was corrected to 26, 4, 2, 2 after execution and now has a regression test.
- The PDF skill required render-and-review before delivery; log checks alone were not used as visual certification.
- Verified environment: Python 3.13.6, PyTorch 2.10.0, pytest 9.0.2. These tests and exact example counts are not new wet-lab or learned-model results.

The PDF is not tagged or PDF/UA-certified. Canonical TXT and accessible SVG descriptions provide diagram alternatives; final accessibility and independent subject review remain open.

## Reproduce

```sh
python3 -m pytest
python3 scripts/chapter01_artifacts.py --check
make pdf check-pdf
```

Use the documented Python/TeX environment in PUBLICATION_PLAN.md. Generated JSON and LaTeX table sources are committed and freshness-tested; local PDF/build products remain ignored. The reset report is pinned to its original milestone commit.

## Next

Chapter 2: molecular structure and orientation, with source-reviewed scientific illustrations and no conflation of a formal string complement with an antiparallel physical partner.

Public source: [hermonai/dna-computing-book](https://github.com/hermonai/dna-computing-book/tree/astra-rewrite). The earlier default `main` and archival branch are preserved; no force-push, new license or authorship change is part of this milestone.
