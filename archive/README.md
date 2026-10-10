# Archive — earlier editions and production history

This is separate from the active `book/` manuscript. The 11 October 2026
reorganization moved the previous working tree here without deleting its
sources, review records or PDFs.

## Locations

- `legacy/dna-computing-book/`: self-contained previous repository layout.
- `legacy/dna-computing-book/output/pdf/`: all 40 previous PDFs, including the
  earlier cumulative candidate, standalone chapter reviews and frozen editions.
- `legacy/dna-computing-book/build/` and `tmp/`: locally retained intermediate
  compiler artifacts and rendered pages, ignored by Git.
- `manifest.json`: SHA-256 digests for 1,135 previously tracked files and all
  40 PDFs, with the original commit and historical test inventory.

Three previously tracked release PDFs remain tracked in this archive. Other
generated PDFs remain available locally, as before; this repository does not
pretend they are downloadable from a fresh Git clone.

## What the old folders meant

The old `book/` held edition metadata, planning snapshots, figures, diagrams and
early chapter materials. It was not the complete current manuscript.
The old `tex/` held several editions and shared opening assets.
`tex/chapters/ch01.tex` and `ch02.tex` were the original edition; the later
continuous candidate combined `tex/deep/`, `tex/textbook/` and `drafts/`.
The active manuscript now has one entry point and one numbered chapter tree.

## Recovery and verification

Run `make archive-check` from the root. It verifies archived bytes without
changing historical review records. `make legacy-test` runs the complete
unchanged historical suite.

Old review hashes resolve relative to `legacy/dna-computing-book/`, not the
current root. Historical Git references still identify original paths/commits.
Restore individual files only to a separate temporary directory or as an
explicitly reviewed change; do not overwrite the canonical manuscript.

This is a frozen snapshot. Do not edit archived source, weaken its tests or
turn old acceptance flags into acceptance of the current edition.
