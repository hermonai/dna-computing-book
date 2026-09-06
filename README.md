# DNA Computing

From Molecules to Algorithms

Active branch: astra-undergraduate-rewrite. **New undergraduate Chapter 1: internally reviewed development draft.** All later units remain planned (36 units in the current full curriculum). This is not a completed textbook or independent pedagogical validation.

Read [the chapter source](tex/undergraduate/ch01.tex), [production report](CHAPTER_1_REPORT.md), [storyboard](research/undergraduate-ch01-storyboard.md), [contents](BOOK_PLAN.md) and [course map](COURSE_MAP.md).


## Reproduce and inspect

[Read the published Chapter 1 PDF](output/pdf/undergraduate-dna-computing.pdf).

Requires Python 3, pytest and the existing project test dependencies; XeLaTeX/latexmk, librsvg's rsvg-convert and Poppler. Pillow is needed only for page contact sheets.

```sh
python3 scripts/build_pedagogy.py --check
python3 scripts/audit_undergraduate.py --check
python3 scripts/build_undergraduate.py --check
python3 -m pytest
make pdf
make check-pdf
python3 scripts/review_undergraduate.py
```

The PDF is generated under output/pdf with a distinct undergraduate filename. Figures retain editable SVG and Unicode TXT sources. Printed code is included directly from the tested example. See [publication instructions](PUBLICATION_PLAN.md) and [chapter standard](CHAPTER_STANDARD.md).

## Preservation

The earlier two-chapter edition remains at astra-rewrite commit a1fb9a6154976f903b39d0f8a26834a8336f2264; main and historical snapshots are unchanged. Old chapter sources remain byte-identical and are excluded from the active manifest. Use the preserved commit to reproduce old PDFs. No force push, deletion, license or authorship change is part of this milestone.

Reports and evidence ledgers distinguish current undergraduate work from earlier editions. Internal role reviews are not external endorsements; no new laboratory or research-model experiment is claimed.
