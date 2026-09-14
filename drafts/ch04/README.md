# Chapter 4 review candidate

**Molecular parallelism and resource accounting**

This standalone chapter is authored directly in [LaTeX](manuscript.tex), following
the repository's textbook standard. It does not regenerate prose from Markdown,
change accepted Chapters 1-2, or promote Chapter 3 to cumulative acceptance.
The curriculum's cumulative progression remains gated; this directory records
the separate Chapter 4 production candidate requested by the author.

The chapter develops independent and finite-pool sampling, represented diversity,
shared failure floors, molecular inventory and concentration, conditional reaction
success, readout selection, and dimensioned resource accounting. Its factorial
example is explicitly limited to a uniform generate-and-test proposal, not a
lower bound on all DNA algorithms. The kinetic constant and probabilities are
declared teaching assumptions, not empirical DNA performance measurements.

Five editable native TikZ plates include antiparallel nick sealing, molecule
populations, concentration, sampling/readout, and computed reliability curves.
[Semantic TXT companions](figures/semantic-descriptions.txt) explain their objects,
transitions, inferences, and limits. Twelve exercises have worked answers or a
scoring rubric. The [reference module](reference.py) and [recorded results](results.json)
provide the executable numerical evidence; [sources](sources.tex) identify primary
support and its boundaries.

## Reproduce

The checked environment uses Python 3.13.6, TeX Live 2025 with XeLaTeX/latexmk and
makeindex, Poppler, and Pillow for page rendering. The reference calculation itself
uses the Python standard library. Fonts: TeX Gyre Pagella (body and mathematics),
TeX Gyre Heros (headings), and DejaVu Sans Mono (code).

From the repository root, with those dependencies available:

```sh
python3 drafts/ch04/reference.py
python3 drafts/ch04/build.py --assets-only
python3 drafts/ch04/build.py --check
python3 -m pytest -o addopts='' -q tests/test_ch04_reference.py
python3 drafts/ch04/build.py --render
```

The builder writes `output/pdf/dna-computing-ch04-review.pdf`, data tables and
literal code excerpts under `build/ch04/`, and all page renders plus color and
grayscale contact sheets under `tmp/pdfs/ch04-review/`. Run full-repository tests
after PDF builds finish, because preservation tests must not race output writes.
Build outputs remain generated artifacts, consistent with the repository's ignore rules.

## Review status

The 15-page candidate received author technical, editorial, and all-page visual
review, including grayscale inspection, on 14 September 2026. This is not
independent specialist review. Compilation has no overfull boxes, missing glyphs,
or unresolved references. The tests include small-space enumeration, boundary
and precision rejection, the adjacent-integer 113-copy check, and dimensioned
conversions. The full repository suite also passes its preservation contracts.

See the [source-bound review record](../../artifacts/deep/ch04-review.json).
Open gates: independent scientific review, reader feedback, and cumulative
integration with consistent cross-chapter numbering/index/bibliography. Those
gates remain open for prior review candidates too.
