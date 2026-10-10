# Chapter 17: Watson–Crick and biochemical automata — expanded theory

Standalone authored-LaTeX review candidate. Earlier accepted editions remain unchanged.

The separate expanded edition adds formal definitions, nonregularity and
synchronous-regularity proofs, three determinism notions, a proved normal-form
construction, and explicit description/input complexity. Its biochemical half
specifies reaction-to-reader refinement, material balance, exact renewal branch
and mean-time formulas, a qualified exponential approximation, noisy stochastic
automata, and observable-output identifiability.

Eight editable TikZ figures have semantic TXT companions; eighteen exercises
include worked answers. Tables and plots are generated from reference.py.
Access depth and evidence limits are recorded in sources.tex. This is an
academic teaching expansion, not a claim of new theorems or measured chemistry.
The earlier [Chapter 17 candidate](../ch17/README.md), its review hashes, and all
accepted editions are preserved. No change to Evolutor is part of this revision.

Run from the repository root with Python 3.13 and the project dependencies:

```sh
python3 drafts/ch17-theory/build.py --assets-only
python3 -m pytest tests/test_ch17_theory.py
python3 drafts/ch17-theory/build.py --render
python3 drafts/ch17-theory/build.py --check
```

Local output: output/pdf/dna-computing-ch17-theory-review.pdf. PDFs are generated, not committed.

Tests cover exhaustive paired recognition and normalization, determinism
counterexamples, Markov-generator absorption equations, race conservation and
scaling, and exhaustive error/loss histories checked against closed-form parity.

Independent specialist review, reader feedback and cumulative integration remain open.
