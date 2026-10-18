# Authoring and production

## One source of truth

`book/main.tex` is the full-volume entry point. `book/book.json` records the
ordered chapter paths. Prose belongs in `book/chapters/chNN/manuscript.tex`;
reference implementations, result fixtures, source notes and figures live
beside it. Chapter 17 is the expanded theory treatment; the shorter version
is archived, not a second active chapter.

Follow the [chapter standard](CHAPTER_STANDARD.md) and
[textbook standard](TEXTBOOK_STANDARD.md): derive, implement, independently
test, expose a failure case and explain what the result establishes.
Abstraction is welcome when its meaning and limits are explicit.

## Assets and references

- Edit original SVG/TikZ, not converted PDFs; retain semantic TXT companions.
- `assets.py` supplies numerical tables, plots and literal function listings;
  it is not another PDF entry point.
- `results.json` is a checked fixture. Intentional changes require numerical
  review and tests, not silently regenerated expected values.
- `build/generated/` holds computed assets.
- `build/book/` holds citation-scoped derived TeX and compiler outputs.
- All references live in one BibTeX database, `book/backmatter/references.bib`,
  with global keys; chapters cite it directly and end with annotated Further
  reading in `sources.tex`. Source-access notes belong in
  `docs/provenance/source-access-notes.md`, not in reader-facing entries.
- New plates use the shared language in `book/visual.tex`; teaching boxes are
  defined in `book/pedagogy.tex`. Inside Chapters 4–32 use `\gref` for
  book-level labels (appendices, Parts, Chapters 1–3).

The opening chapters retain reviewed snippets/tables. Their source closure is
checked separately from historical byte-preservation. Shared pedagogy/evidence
acknowledgments occur once in front matter.

## Verification

Run `make check`, `make pdf` and `make archive-check`. Do not build archived
PDFs while running the historical preservation suite: it snapshots old outputs.
Current tests use the canonical code and independent numerical oracles.
Historical layout/hash checks remain unchanged in the archived suite; they
were not reinterpreted as review of new paths.

Render changed pages with Poppler and inspect figures, captions, code,
references, index and grayscale legibility. Compiler success or path
relocation does not replace visual or scientific review.

## Directory policy

Only the current full-book PDF belongs in `output/pdf/`. Older editions,
chapter PDFs, retired plans and reports belong in `archive/`.
Caches are disposable after evidence is recorded. Use explicit, recoverable
archival moves when provenance is uncertain.

Never author in the archive or alter frozen acceptance records.
Commit scoped changes; push only when requested.
