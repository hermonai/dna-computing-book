# DNA Computing Chapter 22 package

**Chapter:** 22 — Self-assembly, tiles and geometry  
**Stable ID:** DNAD-22  
**Revision:** r01  
**Status:** standalone authored-LaTeX review candidate.

This package connects an explicit seeded abstract Tile Assembly Model (aTAM) variant
to molecular tile and DNA-origami realizations without identifying abstract glue
strength with a measured binding free energy. The executable reference builds a
deterministic XOR/Sierpiński assembly, enumerates legal attachments, detects an
ambiguous counterexample, and computes finite-size and independent cellular-automaton
oracles.

Reproduce:

```sh
python3 drafts/ch22/reference.py > drafts/ch22/results.json
python3 -m pytest -q tests/test_ch22_reference.py
python3 drafts/ch22/build.py
```

Build dependencies: Python 3.11+, pytest, XeLaTeX/latexmk. No wet-lab result is
claimed. Literature access and inspected depth are recorded in
`research/source-ledger.json`.
