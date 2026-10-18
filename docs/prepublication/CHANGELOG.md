# Changelog: undergraduate textbook revision (October 2026)

Base: `5987341` (review prerelease `dna-review-2026-10-17`, 397 pages).

## Structure and front/back matter
- Eight Parts with orientation openers (`book/parts/`, listed in `book/book.json`).
- New title page, Preface, "How to use this book" (reading map, course plans,
  box legend, visual conventions, notation). The previous administrative
  "Reading and evidence conventions" and "About the examples" pages were removed;
  their substance is in the Preface.
- Epilogue: five research frontiers, cross-cutting open problems, capstone projects.
- Appendices: A molecular biology primer, B mathematical toolkit, C timeline
  1953–2026 (48 cited milestones).
- Glossary: 15 new entries; reader-facing introduction.

## Bibliography
- One BibTeX database `book/backmatter/references.bib`; natbib/plainnat, numeric,
  alphabetical, printed once at the end. Duplicate works merged.
- 123 works cited, including verified 2018–2026 frontier papers (Cherry & Qian
  2018 and 2025; Woods et al. 2019; Xiong et al. 2022; Choi et al. 2022; Lv et
  al. 2023; Evans et al. 2024; Zhang et al. 2024; Song & Qian 2025; Stérin et
  al. 2026) and classics (Watson & Crick, Seeman, Cook, Karp, Bennett, Garey &
  Johnson, Sipser, Saiki et al.).
- Per-chapter "Sources and evidence" access notes archived verbatim in
  `docs/provenance/source-access-notes.md`; chapters end with annotated
  Further reading.

## Teaching apparatus
- `book/pedagogy.tex`: chapter goals, Key ideas, Biology bridge, Computing
  bridge, Common pitfall, Research frontier, Predict first, Worked example.
- All 32 chapters gain goals and key ideas; most gain at least one bridge,
  pitfall, frontier or worked box.

## Content
- Ch 1: DNA primer section; Further reading; modern eras of the field.
- Ch 21: new section "From threshold gates to DNA neural networks".
- Ch 22: new section "Algorithmic self-assembly at scale".
- Ch 13, 14, 19, 20, 25: frontier boxes.
- Ch 18: corrected description of the scaffolded DNA computer.
- Ch 3, 32 and front matter: administrative review text replaced or archived.

## Illustrations
- Shared TikZ visual language `book/visual.tex`; palette harmonised for all plates.
- 21 new or redrawn plates (see `FIGURE_ATLAS.md`); 8 box/table figures removed.
- Figure scaling capped at 1.15× enlargement.

## Build and tests
- `scripts/build_book.py`: Parts; BibTeX; citation map
  (`build/book/citation-map.json`) replaces the key-remapping bibliography;
  BibTeX warnings fail the build.
- Fixed label namespacing after `\captionof` (`\FigureLabel`), and added `\gref`
  for book-level labels.
- `tests/test_repository_layout.py`: bibliography test replaced by a single-
  database, no-duplicate-DOI, all-citations-resolve test; new Parts test.
  Archive and numerical tests unchanged.
