# DNA Computing: deep technical edition

Status: architecture and detailed outlines only; no new manuscript, final figures, animation frames, models, engines or experiments are delivered. Canonical source: [deep curriculum](pedagogy/deep-curriculum.json). Prior editions remain historical references, not the active teaching level.

DOGMA = non-Transformer DNA-native model + DOGMA Engine; Hermon DNA = Transformer-based DNA model + Hermon DNA Engine; Evolutor = broader genomic computation theory, research and eventual runtime above both.

## Knowledge organization and reading routes

### I · Origins and computational strategy

DNAD-01 → DNAD-02 → DNAD-03 → DNAD-04

- DNAD-01: molecular computation; Hamiltonian witness; encoding and selection.
- DNAD-02: vertex and edge oligos; annealing and ligation; endpoint PCR; length and affinity selection; historical readout.
- DNAD-03: directed graphs; Hamiltonian paths; SAT; P; NP; reductions; verification.
- DNAD-04: sampling; material; concentration; reaction depth; readout; energy boundaries.

### II · Molecular foundations and operators

DNAD-05 → DNAD-06 → DNAD-07 → DNAD-08 → DNAD-09 → DNAD-10

- DNAD-05: nucleotide; phosphodiester backbone; stacking; antiparallel duplex; reverse complement.
- DNAD-06: free energy; nearest-neighbor models; salt; concentration; melting; mismatch.
- DNAD-07: mass action; stoichiometry; ODEs; stochastic trajectories; diffusion limits.
- DNAD-08: polymerase; ligase; restriction; recognition; substrates; cofactors.
- DNAD-09: primer orientation; thermal cycling; specificity; efficiency; contamination.
- DNAD-10: electrophoresis; affinity purification; fluorescence; sequencing; controls.

### III · Encoding and molecular algorithms

DNAD-11 → DNAD-12 → DNAD-13 → DNAD-14 → DNAD-15

- DNAD-11: orthogonality; overlaps; reverse-complement constraints; secondary structure.
- DNAD-12: candidate multisets; predicates; soundness; completeness; physical loss.
- DNAD-13: Lipton encoding; clauses; selection; solution extraction.
- DNAD-14: memory strands; stickers; bit operations; register reuse.
- DNAD-15: cut-and-paste rules; context; insertion; deletion; molecular interpretation.

### IV · Formal molecular computation

DNAD-16 → DNAD-17 → DNAD-18

- DNAD-16: formal languages; grammars; automata; acceptance; transduction.
- DNAD-17: paired-strand automata; complementarity relation; Benenson-style systems.
- DNAD-18: Turing completeness; simulations; uniformity; resource vectors.

### V · Molecular programming

DNAD-19 → DNAD-20 → DNAD-21 → DNAD-22

- DNAD-19: toehold binding; branch migration; release; leakage.
- DNAD-20: species; stoichiometry; mass action; compositional encodings.
- DNAD-21: logic; thresholds; restoration; feedback; fan-out; depletion.
- DNAD-22: Seeman structures; Wang tiles; aTAM; glue strengths; assembly sequences; origami.

### VI · Engineering and evidence

DNAD-23 → DNAD-24 → DNAD-25 → DNAD-26

- DNAD-23: synthesis error; mismatch; leak; PCR bias; false positives; false negatives.
- DNAD-24: material; species; volume; latency; energy; detection; parallelism.
- DNAD-25: writing; coding; redundancy; access; sequencing channels; storage versus computation.
- DNAD-26: oligo design; purification; mixing; reaction; controls; measurement; provenance.

### VII · Executable models and modern research

DNAD-27 → DNAD-28 → DNAD-29 → DNAD-30 → DNAD-31 → DNAD-32

- DNAD-27: strings; multisets; rule interpreters; bounded search; independent oracles.
- DNAD-28: ODE integration; stochastic simulation; parameter fitting; model validation.
- DNAD-29: sensitivity; inverse design; tensors; gradients; DNA representations.
- DNAD-30: genes; RNA; proteins; promoters; regulatory networks; development; inheritance; selection.
- DNAD-31: circuits; assembly; sensing; in-vitro and in-vivo boundaries; current literature.
- DNAD-32: physical molecule; formal string; simulator; learned representation; computational analogy.

Arrows here indicate reading order, not extra hard prerequisites. Use PREREQUISITE_GRAPH.md for minimal dependency closure. Domain abstractions are deliberate: explain the mapping, preserved properties and omitted phenomena.
