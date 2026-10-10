# Chapter 2 development report

> Preserved edition-2 document. This does not describe the active deep technical edition. See [DEEP_REDESIGN.md](DEEP_REDESIGN.md); the deep manuscript has no drafted chapters yet. Historical findings below are unchanged.

Date: 2026-09-06. Publication branch: `astra-rewrite`. This is an internally reviewed two-chapter draft, not a complete or independently peer-reviewed textbook.

## Delivered

[Chapter 2](tex/chapters/ch02.tex): **Molecular structure and strand direction**. Includes a bounded biological account, exact worked example, elementary proof, resource/model limitations, six exercises and solution notes.

[Research review](research/chapter-02-review.md), [canonical scientific graph](book/diagrams/dna-g06.txt), [generated SVG](book/figures/dna-g06.svg), [executed records](book/results/ch02.json), and [claim ledger](research/claims-ledger.md) make the evidence boundaries inspectable. Chapter 1 remains in the manuscript.

## What the example establishes

The paired view is 5′-AACG-3′ above 3′-TTGC-5′. The same partner written 5′ to 3′ is CGTT. Duplex validation rejects an unreversed complement presented as its standard-form partner. Exhaustive tests cover 1364 canonical sequences of lengths one through five. Legacy Strand.complement behavior is unchanged but its symbol-only meaning is explicit; aligned_complement returns a direction-labeled view. No binding or primer-extension success is predicted.

## Verification

The full test suite passes (40 tests), including artifact freshness, canonical graph contracts and executable-example checks. The A4 PDF contains 17 pages and passes the PDF log check with no missing glyphs, undefined references or overfull boxes. All final pages were inspected as rendered contact sheets, with detailed inspection of the new figures, equations, tables and code examples.

Visual review caught a code example split across a figure page; the complete example is now kept together.

Verification used Python 3.13.6, pytest 9.0.2, TeX Live 2025 (XeLaTeX), latexmk 4.86a, rsvg-convert 2.61.1 and Poppler. The output uses PDF 1.7. These internal tests establish the stated computational contracts, not experimental biological validity.

The PDF skill requires rendering and visual inspection, not just compilation. Canonical TXT and accessible SVG descriptions accompany the figures; the PDF is not tagged or PDF/UA-certified. Independent scientific review remains a final-release gate.

## Reproduce

```sh
python3 -m pytest
python3 scripts/chapter02_artifacts.py --check
make pdf check-pdf
```

See PUBLICATION_PLAN.md for the build environment. Public source is on [hermonai/dna-computing-book](https://github.com/hermonai/dna-computing-book/tree/astra-rewrite). PDFs remain local build artifacts; their source, tables and SVGs are versioned. The earlier main branch and archival history are preserved.

## Next

Chapter 3: pairing, free energy and molecular recognition. Establish units, environmental assumptions and a defensible energy model before numerical predictions.
