# MiniDNA reference-stack redesign

## Audit of every implementation module

| Module | Classification | Decision and observed limitation |
| --- | --- | --- |
| alphabet.py | teaching reference | Retain concept; normalization removes Unicode whitespace despite an ASCII-only docstring. Clarify policy later. |
| complement.py | symbolic/tensor teaching reference | Exact permutation and reverse-complement operations; 22-test repository baseline includes unfinished extensions. Formal strings may be empty while current API rejects them. |
| strand.py | prototype representation | Orientation ambiguity: complement() returns a 5′→3′-labeled Strand without reversal. Do not teach this as the physical partner. |
| hybridization.py | toy alignment model | Correctly disclaims thermodynamic prediction; keep as a contrast example. |
| reactions.py | symbolic prototype | Cut may produce empty fragments that ligate then rejects; repair domain contract before exercises. |
| splicing.py | formal crossover toy | Suffix exchange is not a complete splicing-system semantics or biochemical simulation. |
| regulation.py / expression.py | generic callable execution toy | Context gates and ordered execution do not model gene regulation kinetics. Move concept to advanced comparison if useful. |
| __init__.py | package interface | Re-evaluate exported names after domain contracts are fixed. |

Existing tests are regression evidence, not a physical validation set. Keep code in place during the reset; no broad rewrite is justified yet.

## New reference curriculum

Canonical alphabet and polarity → typed sequence/duplex views → exact operations with empty-string contracts → finite-state/pool algorithms → explicit rewrite models → CRN count/concentration semantics → displacement-domain simulation → comparison against published measurements.

Start with Python when strings are clearest. Use PyTorch for tensor semantics and differentiable models where it clarifies the idea. Require symbolic/tensor parity. Add uncertainty and units before thermodynamic claims. A future simulator must not inherit physical credibility from a familiar module name.

## Acceptance tests

Property tests for involutions; orientation examples with asymmetric strands; cut/join round trips at every boundary; invalid alphabet/shape cases; enumerated small-model oracles; conservation and nonnegative species checks for numerical reactions. Do not import a differentiable or neural model into the molecular curriculum merely to satisfy a technology preference.
