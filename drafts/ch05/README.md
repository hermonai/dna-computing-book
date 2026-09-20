# Chapter 5 — DNA chemistry and sequence geometry

Standalone authored-LaTeX review candidate, 15 September 2026. Five original
TikZ mechanism plates with semantic TXT companions, a generated ambiguity
table, tested Python examples, and twelve exercises with worked solutions.
Earlier accepted editions and Chapters 3–4 review sources remain unchanged.

The chapter derives reverse complements and interval transforms from
molecular directionality. It separates covalent connectivity, pairing,
stacking, symbolic uncertainty, and condition-dependent physical behavior.
No hybridization energy, atomistic simulation, or folding prediction is claimed.

## Reproduce

Run from the repository root:

    python3 drafts/ch05/build.py --render
    python3 drafts/ch05/build.py --check
    python3 -m pytest -o addopts='' -q tests/test_ch05_reference.py

Dependencies: Python 3.10+, pytest, Pillow for rendering contact sheets,
XeLaTeX/latexmk, Poppler, and the fonts declared in review.tex.
The build creates output/pdf/dna-computing-ch05-review-v2.pdf and page previews

Revision 2 centralizes the recurring pedagogy and review disclosure in
tex/frontmatter/about-this-book.tex. Earlier PDF and review records are retained.
under tmp/pdfs/ch05-review/; output artifacts are local, not tracked in Git.

The manuscript is authored directly in LaTeX. The builder extracts whole
tested functions into listings and generates results.json and the ambiguity
table. It rejects overflow, missing glyphs, and unresolved references.
Source-access limits are recorded in sources.tex, including the stacking
paper's correction notice and the limited author-companion access to Raschka.

The source-bound author review is artifacts/deep/ch05-review.json.
This is not independent certification, a reader study, or promotion into
the frozen accepted Chapters 1–2. Next planned chapter: hybridization
thermodynamics.
