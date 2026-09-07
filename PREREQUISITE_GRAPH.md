# DNA Computing: deep technical edition

Status: architecture and detailed outlines only; no new manuscript, final figures, animation frames, models, engines or experiments are delivered. Canonical source: [deep curriculum](pedagogy/deep-curriculum.json). Prior editions remain historical references, not the active teaching level.

DOGMA = non-Transformer DNA-native model + DOGMA Engine; Hermon DNA = Transformer-based DNA model + Hermon DNA Engine; Evolutor = broader genomic computation theory, research and eventual runtime above both.

## Semantic TXT prerequisite graph

A → B means that A supplies knowledge required by B; all incoming edges are required. It is not a molecular causal arrow. ENTRY is the explicit technical entry contract. Chapter 1 roadmaps preview later material without requiring it. DNAD imports are one-way from Book I; no reverse dependencies exist.

ENTRY → DNAD-01 : prerequisite for Computing with DNA

DNAD-01 → DNAD-02 : prerequisite for Adleman's experiment: a mechanistic reconstruction

DNAD-01 → DNAD-03 : prerequisite for Combinatorial search and complexity

DNAD-02 → DNAD-04 : prerequisite for Molecular parallelism and resource accounting

DNAD-03 → DNAD-04 : prerequisite for Molecular parallelism and resource accounting

DNAD-01 → DNAD-05 : prerequisite for DNA chemistry and sequence geometry

DNAD-05 → DNAD-06 : prerequisite for Hybridization thermodynamics

DNAD-05 → DNAD-07 : prerequisite for Reaction kinetics and stochastic chemistry

DNAD-06 → DNAD-07 : prerequisite for Reaction kinetics and stochastic chemistry

DNAD-05 → DNAD-08 : prerequisite for Enzymes as molecular operators

DNAD-07 → DNAD-08 : prerequisite for Enzymes as molecular operators

DNAD-06 → DNAD-09 : prerequisite for PCR, amplification and selection bias

DNAD-08 → DNAD-09 : prerequisite for PCR, amplification and selection bias

DNAD-08 → DNAD-10 : prerequisite for Separation, detection and experimental logic

DNAD-09 → DNAD-10 : prerequisite for Separation, detection and experimental logic

DNAD-03 → DNAD-11 : prerequisite for Sequence design and graph encoding

DNAD-06 → DNAD-11 : prerequisite for Sequence design and graph encoding

DNAD-10 → DNAD-11 : prerequisite for Sequence design and graph encoding

DNAD-02 → DNAD-12 : prerequisite for Generate–filter–verify algorithms

DNAD-11 → DNAD-12 : prerequisite for Generate–filter–verify algorithms

DNAD-03 → DNAD-13 : prerequisite for SAT and combinatorial constructions

DNAD-12 → DNAD-13 : prerequisite for SAT and combinatorial constructions

DNAD-11 → DNAD-14 : prerequisite for Sticker systems and molecular memory

DNAD-12 → DNAD-14 : prerequisite for Sticker systems and molecular memory

DNAD-08 → DNAD-15 : prerequisite for Splicing and insertion–deletion systems

DNAD-11 → DNAD-15 : prerequisite for Splicing and insertion–deletion systems

DNAD-03 → DNAD-16 : prerequisite for Languages, automata and molecular recognition

DNAD-15 → DNAD-16 : prerequisite for Languages, automata and molecular recognition

DNAD-05 → DNAD-17 : prerequisite for Watson–Crick and biochemical automata

DNAD-08 → DNAD-17 : prerequisite for Watson–Crick and biochemical automata

DNAD-16 → DNAD-17 : prerequisite for Watson–Crick and biochemical automata

DNAD-04 → DNAD-18 : prerequisite for Universality and complexity models

DNAD-14 → DNAD-18 : prerequisite for Universality and complexity models

DNAD-15 → DNAD-18 : prerequisite for Universality and complexity models

DNAD-16 → DNAD-18 : prerequisite for Universality and complexity models

DNAD-17 → DNAD-18 : prerequisite for Universality and complexity models

DNAD-06 → DNAD-19 : prerequisite for Toehold-mediated strand displacement

DNAD-07 → DNAD-19 : prerequisite for Toehold-mediated strand displacement

DNAD-11 → DNAD-19 : prerequisite for Toehold-mediated strand displacement

DNAD-07 → DNAD-20 : prerequisite for Chemical reaction networks as programs

DNAD-18 → DNAD-20 : prerequisite for Chemical reaction networks as programs

DNAD-19 → DNAD-20 : prerequisite for Chemical reaction networks as programs

DNAD-19 → DNAD-21 : prerequisite for Digital and analog DNA circuits

DNAD-20 → DNAD-21 : prerequisite for Digital and analog DNA circuits

DNAD-05 → DNAD-22 : prerequisite for Self-assembly, tiles and geometry

DNAD-18 → DNAD-22 : prerequisite for Self-assembly, tiles and geometry

DNAD-10 → DNAD-23 : prerequisite for Noise, crosstalk and fault models

DNAD-12 → DNAD-23 : prerequisite for Noise, crosstalk and fault models

DNAD-19 → DNAD-23 : prerequisite for Noise, crosstalk and fault models

DNAD-21 → DNAD-23 : prerequisite for Noise, crosstalk and fault models

DNAD-04 → DNAD-24 : prerequisite for Scaling and resource limits

DNAD-18 → DNAD-24 : prerequisite for Scaling and resource limits

DNAD-21 → DNAD-24 : prerequisite for Scaling and resource limits

DNAD-22 → DNAD-24 : prerequisite for Scaling and resource limits

DNAD-23 → DNAD-24 : prerequisite for Scaling and resource limits

DNAD-05 → DNAD-25 : prerequisite for Synthesis, sequencing and DNA storage

DNAD-10 → DNAD-25 : prerequisite for Synthesis, sequencing and DNA storage

DNAD-23 → DNAD-25 : prerequisite for Synthesis, sequencing and DNA storage

DNAD-08 → DNAD-26 : prerequisite for Laboratory workflows and reproducibility

DNAD-09 → DNAD-26 : prerequisite for Laboratory workflows and reproducibility

DNAD-10 → DNAD-26 : prerequisite for Laboratory workflows and reproducibility

DNAD-23 → DNAD-26 : prerequisite for Laboratory workflows and reproducibility

DNAD-24 → DNAD-26 : prerequisite for Laboratory workflows and reproducibility

DNAD-11 → DNAD-27 : prerequisite for Symbolic molecular simulation

DNAD-12 → DNAD-27 : prerequisite for Symbolic molecular simulation

DNAD-15 → DNAD-27 : prerequisite for Symbolic molecular simulation

DNAD-17 → DNAD-27 : prerequisite for Symbolic molecular simulation

DNAD-07 → DNAD-28 : prerequisite for Kinetic and stochastic simulation

DNAD-19 → DNAD-28 : prerequisite for Kinetic and stochastic simulation

DNAD-20 → DNAD-28 : prerequisite for Kinetic and stochastic simulation

DNAD-23 → DNAD-28 : prerequisite for Kinetic and stochastic simulation

DNAD-27 → DNAD-28 : prerequisite for Kinetic and stochastic simulation

DNAD-06 → DNAD-29 : prerequisite for Differentiable molecular and sequence models

DNAD-25 → DNAD-29 : prerequisite for Differentiable molecular and sequence models

DNAD-28 → DNAD-29 : prerequisite for Differentiable molecular and sequence models

DNAD-05 → DNAD-30 : prerequisite for Genomic organization, regulation and development

DNAD-07 → DNAD-30 : prerequisite for Genomic organization, regulation and development

DNAD-08 → DNAD-30 : prerequisite for Genomic organization, regulation and development

DNAD-21 → DNAD-31 : prerequisite for Modern molecular programming and evidence

DNAD-22 → DNAD-31 : prerequisite for Modern molecular programming and evidence

DNAD-24 → DNAD-31 : prerequisite for Modern molecular programming and evidence

DNAD-26 → DNAD-31 : prerequisite for Modern molecular programming and evidence

DNAD-28 → DNAD-31 : prerequisite for Modern molecular programming and evidence

DNAD-29 → DNAD-31 : prerequisite for Modern molecular programming and evidence

DNAD-18 → DNAD-32 : prerequisite for From molecular computation to genomic computation

DNAD-24 → DNAD-32 : prerequisite for From molecular computation to genomic computation

DNAD-29 → DNAD-32 : prerequisite for From molecular computation to genomic computation

DNAD-30 → DNAD-32 : prerequisite for From molecular computation to genomic computation

DNAD-31 → DNAD-32 : prerequisite for From molecular computation to genomic computation

The [deep Book I contract](pedagogy/deep-book-i-contract.json) contains exact exit tasks. A planned link does not establish that a chapter has been taught. Qualified readers may demonstrate equivalent knowledge; otherwise follow the named chapters.
