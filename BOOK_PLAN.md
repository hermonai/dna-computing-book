# DNA Computing: deep technical edition

Status: architecture and detailed outlines only; no new manuscript, final figures, animation frames, models, engines or experiments are delivered. Canonical source: [deep curriculum](pedagogy/deep-curriculum.json). Prior editions remain historical references, not the active teaching level.

DOGMA = non-Transformer DNA-native model + DOGMA Engine; Hermon DNA = Transformer-based DNA model + Hermon DNA Engine; Evolutor = broader genomic computation theory, research and eventual runtime above both.

## Macro table of contents

### I · Origins and computational strategy

1. **Computing with DNA** (DNAD-01). molecular computation; Hamiltonian witness; encoding and selection.

2. **Adleman's experiment: a mechanistic reconstruction** (DNAD-02). vertex and edge oligos; annealing and ligation; endpoint PCR; length and affinity selection; historical readout.

3. **Combinatorial search and complexity** (DNAD-03). directed graphs; Hamiltonian paths; SAT; P; NP; reductions; verification.

4. **Molecular parallelism and resource accounting** (DNAD-04). sampling; material; concentration; reaction depth; readout; energy boundaries.

### II · Molecular foundations and operators

5. **DNA chemistry and sequence geometry** (DNAD-05). nucleotide; phosphodiester backbone; stacking; antiparallel duplex; reverse complement.

6. **Hybridization thermodynamics** (DNAD-06). free energy; nearest-neighbor models; salt; concentration; melting; mismatch.

7. **Reaction kinetics and stochastic chemistry** (DNAD-07). mass action; stoichiometry; ODEs; stochastic trajectories; diffusion limits.

8. **Enzymes as molecular operators** (DNAD-08). polymerase; ligase; restriction; recognition; substrates; cofactors.

9. **PCR, amplification and selection bias** (DNAD-09). primer orientation; thermal cycling; specificity; efficiency; contamination.

10. **Separation, detection and experimental logic** (DNAD-10). electrophoresis; affinity purification; fluorescence; sequencing; controls.

### III · Encoding and molecular algorithms

11. **Sequence design and graph encoding** (DNAD-11). orthogonality; overlaps; reverse-complement constraints; secondary structure.

12. **Generate–filter–verify algorithms** (DNAD-12). candidate multisets; predicates; soundness; completeness; physical loss.

13. **SAT and combinatorial constructions** (DNAD-13). Lipton encoding; clauses; selection; solution extraction.

14. **Sticker systems and molecular memory** (DNAD-14). memory strands; stickers; bit operations; register reuse.

15. **Splicing and insertion–deletion systems** (DNAD-15). cut-and-paste rules; context; insertion; deletion; molecular interpretation.

### IV · Formal molecular computation

16. **Languages, automata and molecular recognition** (DNAD-16). formal languages; grammars; automata; acceptance; transduction.

17. **Watson–Crick and biochemical automata** (DNAD-17). paired-strand automata; complementarity relation; Benenson-style systems.

18. **Universality and complexity models** (DNAD-18). Turing completeness; simulations; uniformity; resource vectors.

### V · Molecular programming

19. **Toehold-mediated strand displacement** (DNAD-19). toehold binding; branch migration; release; leakage.

20. **Chemical reaction networks as programs** (DNAD-20). species; stoichiometry; mass action; compositional encodings.

21. **Digital and analog DNA circuits** (DNAD-21). logic; thresholds; restoration; feedback; fan-out; depletion.

22. **Self-assembly, tiles and geometry** (DNAD-22). Seeman structures; Wang tiles; aTAM; glue strengths; assembly sequences; origami.

### VI · Engineering and evidence

23. **Noise, crosstalk and fault models** (DNAD-23). synthesis error; mismatch; leak; PCR bias; false positives; false negatives.

24. **Scaling and resource limits** (DNAD-24). material; species; volume; latency; energy; detection; parallelism.

25. **Synthesis, sequencing and DNA storage** (DNAD-25). writing; coding; redundancy; access; sequencing channels; storage versus computation.

26. **Laboratory workflows and reproducibility** (DNAD-26). oligo design; purification; mixing; reaction; controls; measurement; provenance.

### VII · Executable models and modern research

27. **Symbolic molecular simulation** (DNAD-27). strings; multisets; rule interpreters; bounded search; independent oracles.

28. **Kinetic and stochastic simulation** (DNAD-28). ODE integration; stochastic simulation; parameter fitting; model validation.

29. **Differentiable molecular and sequence models** (DNAD-29). sensitivity; inverse design; tensors; gradients; DNA representations.

30. **Genomic organization, regulation and development** (DNAD-30). genes; RNA; proteins; promoters; regulatory networks; development; inheritance; selection.

31. **Modern molecular programming and evidence** (DNAD-31). circuits; assembly; sensing; in-vitro and in-vivo boundaries; current literature.

32. **From molecular computation to genomic computation** (DNAD-32). physical molecule; formal string; simulator; learned representation; computational analogy.

32 substantial chapters; counts follow coherent arguments rather than fixed page or lecture quotas. Chapter 1 previews the field; later chapters reconstruct mechanisms and proofs in depth. See DEEP_REDESIGN.md for assumed knowledge and reading routes.
