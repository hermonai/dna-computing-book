# Chapter 22: Self-assembly, tiles and geometry

Local convergence revision, 6 October 2026. Original r01 ZIP and its manifest
are preserved as incoming provenance under research/integration/ch22/incoming.

This chapter defines stable seeded aTAM growth, proves schedule-independent XOR
assembly, exhaustively enumerates small reachable states and checks a separate
cellular-automaton oracle. It corrects the incoming unstable seed, asymmetric
strength check and mutant that originally had unchanged outputs. The seed/type
resource ledger counts preparation separately from computational types.

Six editable TikZ figures have semantic TXT companions: cooperative tile contacts,
a computed XOR grid, a genuinely wrong continuation, polarity-correct sticky-end
association, a competing-clock trap, and scaffold/staple routing. Sixteen exercises
include worked answers. Kinetic rates and yield probabilities are assigned models,
not measured molecular performance.

Run from repository root:

```sh
python3 -m pytest tests/test_ch22_reference.py
python3 drafts/ch22/build.py --assets-only
python3 drafts/ch22/build.py --render
python3 drafts/ch22/build.py --check
```

Requirements: Python 3.10+, pytest, Pillow, XeLaTeX/latexmk, Poppler and the
repository's existing fonts. The builder adds the installed macOS TeX path,
extracts literal reference functions, regenerates tables/grid and rejects
unresolved references, missing glyphs and overfull boxes.

Output: output/pdf/dna-computing-ch22-review.pdf. This remains a standalone
local review candidate, not full-book acceptance or independent specialist review.
Chapter 23 owns fault channels, crosstalk and reliability; Chapter 24 owns scaling.
