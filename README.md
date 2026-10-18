# DNA Computing

**Molecular mechanisms, algorithms and evidence**

An undergraduate textbook in 32 chapters and eight parts, connecting molecular
biology, formal computation, reaction-network programming, simulation and
genomic representations. Each chapter opens with learning goals and closes with
key ideas, exercises and worked solutions; tested reference code, original
molecular and algorithmic illustrations, a unified bibliography, an epilogue on
research frontiers and three appendices (molecular biology primer, mathematical
toolkit, timeline 1953–2026) accompany the text.

The manuscript is a **review edition**, not an independently reviewed
publication or a demonstration of industrial or genomic capability.

## Read the book

The earlier 397-page review candidate remains available from the
[public review prerelease](https://github.com/hermonai/dna-computing-book/releases/tag/dna-review-2026-10-17).
The current 442-page edition is built from this branch with `make pdf`.

Build the current edition with `make pdf`. The only current full-book output is
[`output/pdf/dna-computing.pdf`](output/pdf/dna-computing.pdf).
All 32 chapters are included; Chapter 17 uses the expanded Watson–Crick and
biochemical automata treatment.

See the [chapter map](book/README.md), [authoring guide](docs/AUTHORING.md)
and [editorial architecture](docs/EDITORIAL_ARCHITECTURE.md).

The October 2026 undergraduate revision followed the
[textbook review and illustration brief](docs/CLAUDE_PREPUBLICATION_REVIEW_PROMPT.md).
Its plan, findings, figure atlas, validation and remaining gates are in
[`docs/prepublication/`](docs/prepublication/).

## Repository layout

```text
book/
  main.tex                 Full-book LaTeX entry point
  style.tex, layout.tex    Shared typography, figure and reference conventions
  book.json                Ordered current chapter manifest
  visual.tex, pedagogy.tex Shared illustration language and teaching boxes
  frontmatter/             Preface, how to use the book, reading map, conventions
  parts/                   Eight part openers
  chapters/ch01–ch32/       Canonical prose, further reading, figures and companion code
  backmatter/              Epilogue, appendices, glossary and references.bib
code/minidna/              Reusable executable teaching library and its tests
docs/                     Authoring standards, architecture and provenance
scripts/                  Current build and archive-verification tools
tests/                    Current numerical and repository checks
output/pdf/               One generated full-book PDF
build/                    Disposable compiler and computed-asset cache
archive/                  Preserved earlier editions, reports and review PDFs
```

There is no active `tex/` or `drafts/` tree. Edit prose in
`book/chapters/chNN/manuscript.tex`, not in generated TeX or archived material.
Figures and their semantic TXT companions live beside their chapter.

## Build and test

Requirements: Python 3.11+, NumPy, PyTorch and pytest; XeLaTeX, latexmk,
makeindex, Poppler (`pdfinfo`, `pdftoppm`) and librsvg (`rsvg-convert`).
Fonts: TeX Gyre Pagella/Heros and DejaVu Sans Mono.
Install Python dependencies with `python3 -m pip install -e '.[dev]'`.

```sh
make pdf           # full book, bibliography, glossary and index
make check         # generate assets, verify values and run current tests
make archive-check # verify preserved source/PDF checksums
make legacy-test   # unchanged historical regression suite
make review        # render all pages and color/grayscale contact sheets
```

Select Python with `make pdf PYTHON=/path/to/python3`.
`make` defaults to the complete book, not the earlier two-chapter edition.
Missing glyphs, unresolved references/citations, duplicate labels and overfull
boxes fail the build. Code listings come from tested chapter implementations.
Build evidence lives in `build/book/build-record.json`, `warning-audit.json`
and `bibliography-map.json`. Generated outputs are ignored by Git.

## Earlier editions and recovery

The [archive guide](archive/README.md) explains what was retained and why.
The previous layout is preserved under `archive/legacy/dna-computing-book/`,
including the old `book/`, `tex/chapters/`, standalone review PDFs and
historical acceptance records. The [migration manifest](archive/manifest.json)
binds those bytes to the pre-reorganization commit.

The archive is historical evidence, not a second authoring tree. Intermediate
render images and old build caches are retained locally there for recovery and
excluded from Git. Original review records do not imply acceptance of relocated
sources. Do not copy a previous PDF back into the current output folder.

## Scientific and editorial status

The 32-chapter authoring plan is complete. Full-volume scientific/editorial
review, comprehensive visual/accessibility QA, bibliography/index reconciliation,
independent specialist review and reader evaluation remain publication gates.
See [current release status](docs/STATUS.md).

Numerical results are model computations unless identified as measurements.
DOGMA denotes the non-Transformer research branch; Hermon DNA the Transformer
branch; Evolutor the broader research/runtime program. Biological analogies
and working reference components do not establish novelty, trained-model
quality, production readiness or general intelligence.
