# Chapter 6 — Hybridization thermodynamics

Standalone original authored-LaTeX review candidate, 19 September 2026.
Five editable TikZ plates with semantic TXT companions, computed numerical
examples, tested reference code, and twelve worked exercises. Earlier chapters
and accepted editions remain unchanged.

## Reproduce

Run from this repository root:

    python3 drafts/ch06/build.py --render
    python3 drafts/ch06/build.py --check
    python3 -m pytest -o addopts='' -q tests/test_ch06_reference.py

Dependencies: Python 3.10+, pytest, Pillow, XeLaTeX/latexmk,
Poppler, and the fonts declared in review.tex. Generated PDFs live in
output/pdf/dna-computing-ch06-review-v2.pdf; page previews in tmp/pdfs/ch06-review/.

Revision 2 centralizes the recurring pedagogy and review disclosure in
tex/frontmatter/about-this-book.tex. Earlier PDF and review records are retained.
These generated outputs are local and gitignored.

The builder extracts whole tested functions and generates tables/plots; it
never converts Markdown into manuscript prose. See sources.tex for access
depth and limitations. The original teaching sequence draws on the general
implementation-first approach in Raschka's author companion, not copied prose,
figures, or code.

The executable thermodynamic model is restricted to ideal A+B=AB equilibrium
and canonical, perfectly matched, non-self-complementary duplexes at 1 M NaCl.
It is not a validated oligonucleotide design tool, salt/mismatch extrapolator,
or kinetic simulation.

Author review is recorded in artifacts/deep/ch06-review.json. Independent
specialist review, reader feedback, and cumulative acceptance remain open.
Next planned chapter: reaction kinetics and stochastic chemistry.
