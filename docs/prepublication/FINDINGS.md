# Findings

Severity: **defect** (wrong or broken), **risk** (likely to mislead), **preference**
(style). Disposition records what this revision did.

| # | Location | Finding | Severity | Disposition | Validation |
|---|---|---|---|---|---|
| 1 | `book/layout.tex`, `style.tex` figure macros | Labels placed after `\captionof` lost the chapter namespace, so figure references could resolve to the wrong chapter or fail on a clean build (the original commit also fails from a clean build directory). | defect | `\FigureLabel` applies the namespace explicitly | clean build, zero undefined references |
| 2 | Bibliography | Same works under several keys (Adleman 1994, Qian–Winfree 2011, Benenson 2001, SantaLucia 1998, Soloveichik 2010, Sterin 2026, ligase page); access notes printed inside entries; order by first appearance | defect | one BibTeX database, alphabetical, notes moved to `docs/provenance/source-access-notes.md` | test: every `\cite` resolves; no duplicate DOI |
| 3 | Ch 18 | Scaffolded DNA computer described as compiling FSMs "into strand-displacement systems"; it uses tile strands competing on a scaffold | defect | rewritten from the paper's description | source check |
| 4 | Ch 1 helix (new plate, first draft) | Drawn left-handed | defect | depth ordering corrected; grooves computed | rendered check |
| 5 | Front matter, Ch 3, Ch 32 | Administrative review text addressed to maintainers in the student narrative | risk | replaced with reader-facing text; ledgers archived | read-through |
| 6 | Ch 1, 2 | Several figures were boxes or tables restating prose | preference | replaced with mechanism plates or LaTeX tables | rendered check |
| 7 | Ch 5 | Nucleotide and pairing plates did not show real chemical structure | risk | redrawn as skeletal structures | chemistry check (see atlas) |
| 8 | Older plates | Uniform stretching to text width enlarged small plates up to 1.8× | preference | at most 1.15× enlargement | measured scales 0.90–1.32 → printed 0.9–1.15 |
| 9 | Boxes | First box design hid titles (hook overwritten) | defect | headings rendered through `\BoxHead` | rendered check |
| 10 | Ch 25 frontier text (new) | "megabyte-scale" overstated early storage demonstrations | risk | reworded | source check |
| 11 | Ch 2, 19, 30, 32 | Sibling research programs named in student prose | preference | kept only where relevant (Ch 32 plate); generic wording elsewhere | read-through |
| 12 | Retained plates | Not yet reviewed at full resolution against the new visual language | open | listed in readiness gates | — |
| 13 | Several bibliography entries | Only first author known for some 2025–2026 papers; full author lists not verified | open | `and others` used rather than guessed names | — |
