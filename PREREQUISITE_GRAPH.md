# DNA Computing: undergraduate-first architecture

Status: Chapter 1 internally reviewed development draft; all later units remain planned. No learner study, independent expert certification or new research-model experiment is claimed. Generated from [pedagogy/curriculum.json](pedagogy/curriculum.json). See [Chapter 1 storyboard](research/undergraduate-ch01-storyboard.md) for the six produced figures.

## Canonical Unicode TXT dependency graph

Read A → B as: teach A before requiring it in B. Multiple incoming arrows mean all listed prerequisites. ENTRY means only the declared entry assumptions. Book I IDs are explicitly prefixed DNAU; they describe planned teaching, not competence already delivered by the old draft.

```text
ENTRY → DNAU-01 : prerequisite for What does it mean to compute?
DNAU-01 → DNAU-02 : prerequisite for Symbols, information and representations
DNAU-01 → DNAU-03 : prerequisite for Algorithms, decisions and remembered state
DNAU-02 → DNAU-03 : prerequisite for Algorithms, decisions and remembered state
DNAU-03 → DNAU-04 : prerequisite for Your first small Python programs
DNAU-02 → DNAU-05 : prerequisite for Cities, roads, graphs and paths
DNAU-03 → DNAU-05 : prerequisite for Cities, roads, graphs and paths
DNAU-04 → DNAU-05 : prerequisite for Cities, roads, graphs and paths
DNAU-03 → DNAU-06 : prerequisite for Search, counting and growing work
DNAU-04 → DNAU-06 : prerequisite for Search, counting and growing work
DNAU-05 → DNAU-06 : prerequisite for Search, counting and growing work
DNAU-01 → DNAU-07 : prerequisite for Atoms, molecules and different kinds of bonds
DNAU-02 → DNAU-07 : prerequisite for Atoms, molecules and different kinds of bonds
DNAU-03 → DNAU-08 : prerequisite for Solutions, amounts, temperature and change
DNAU-07 → DNAU-08 : prerequisite for Solutions, amounts, temperature and change
DNAU-02 → DNAU-09 : prerequisite for Cells, chromosomes, genes and genomes
DNAU-07 → DNAU-09 : prerequisite for Cells, chromosomes, genes and genomes
DNAU-07 → DNAU-10 : prerequisite for From a nucleotide to a DNA strand
DNAU-09 → DNAU-10 : prerequisite for From a nucleotide to a DNA strand
DNAU-02 → DNAU-11 : prerequisite for Direction, pairing and reverse complement
DNAU-04 → DNAU-11 : prerequisite for Direction, pairing and reverse complement
DNAU-10 → DNAU-11 : prerequisite for Direction, pairing and reverse complement
DNAU-03 → DNAU-12 : prerequisite for Chance, encounters and repeated trials
DNAU-08 → DNAU-12 : prerequisite for Chance, encounters and repeated trials
DNAU-09 → DNAU-13 : prerequisite for From DNA to RNA and proteins
DNAU-10 → DNAU-13 : prerequisite for From DNA to RNA and proteins
DNAU-11 → DNAU-13 : prerequisite for From DNA to RNA and proteins
DNAU-08 → DNAU-14 : prerequisite for Enzymes and DNA replication in six frames
DNAU-11 → DNAU-14 : prerequisite for Enzymes and DNA replication in six frames
DNAU-13 → DNAU-14 : prerequisite for Enzymes and DNA replication in six frames
DNAU-08 → DNAU-15 : prerequisite for What a laboratory operation actually does
DNAU-12 → DNAU-15 : prerequisite for What a laboratory operation actually does
DNAU-14 → DNAU-15 : prerequisite for What a laboratory operation actually does
DNAU-08 → DNAU-16 : prerequisite for Hybridization as molecular recognition
DNAU-11 → DNAU-16 : prerequisite for Hybridization as molecular recognition
DNAU-12 → DNAU-16 : prerequisite for Hybridization as molecular recognition
DNAU-15 → DNAU-16 : prerequisite for Hybridization as molecular recognition
DNAU-14 → DNAU-17 : prerequisite for Cutting and joining strands
DNAU-15 → DNAU-17 : prerequisite for Cutting and joining strands
DNAU-16 → DNAU-17 : prerequisite for Cutting and joining strands
DNAU-14 → DNAU-18 : prerequisite for Copying selected DNA with PCR
DNAU-15 → DNAU-18 : prerequisite for Copying selected DNA with PCR
DNAU-16 → DNAU-18 : prerequisite for Copying selected DNA with PCR
DNAU-15 → DNAU-19 : prerequisite for Separating molecules and retaining candidates
DNAU-17 → DNAU-19 : prerequisite for Separating molecules and retaining candidates
DNAU-18 → DNAU-19 : prerequisite for Separating molecules and retaining candidates
DNAU-15 → DNAU-20 : prerequisite for Detecting and reading a result
DNAU-18 → DNAU-20 : prerequisite for Detecting and reading a result
DNAU-19 → DNAU-20 : prerequisite for Detecting and reading a result
DNAU-05 → DNAU-21 : prerequisite for Hamiltonian paths: a visual mini-course
DNAU-06 → DNAU-21 : prerequisite for Hamiltonian paths: a visual mini-course
DNAU-11 → DNAU-22 : prerequisite for Adleman's idea: encode a graph in DNA
DNAU-17 → DNAU-22 : prerequisite for Adleman's idea: encode a graph in DNA
DNAU-20 → DNAU-22 : prerequisite for Adleman's idea: encode a graph in DNA
DNAU-21 → DNAU-22 : prerequisite for Adleman's idea: encode a graph in DNA
DNAU-12 → DNAU-23 : prerequisite for Generate, filter and read the candidates
DNAU-18 → DNAU-23 : prerequisite for Generate, filter and read the candidates
DNAU-19 → DNAU-23 : prerequisite for Generate, filter and read the candidates
DNAU-20 → DNAU-23 : prerequisite for Generate, filter and read the candidates
DNAU-22 → DNAU-23 : prerequisite for Generate, filter and read the candidates
DNAU-06 → DNAU-24 : prerequisite for What the experiment proved, and what it did not
DNAU-12 → DNAU-24 : prerequisite for What the experiment proved, and what it did not
DNAU-23 → DNAU-24 : prerequisite for What the experiment proved, and what it did not
DNAU-03 → DNAU-25 : prerequisite for Languages, machines and computational models
DNAU-05 → DNAU-25 : prerequisite for Languages, machines and computational models
DNAU-06 → DNAU-25 : prerequisite for Languages, machines and computational models
DNAU-21 → DNAU-25 : prerequisite for Languages, machines and computational models
DNAU-24 → DNAU-25 : prerequisite for Languages, machines and computational models
DNAU-11 → DNAU-26 : prerequisite for Strand, sticker and paired-strand models
DNAU-23 → DNAU-26 : prerequisite for Strand, sticker and paired-strand models
DNAU-25 → DNAU-26 : prerequisite for Strand, sticker and paired-strand models
DNAU-17 → DNAU-27 : prerequisite for Splicing and rewriting strings
DNAU-25 → DNAU-27 : prerequisite for Splicing and rewriting strings
DNAU-08 → DNAU-28 : prerequisite for Reaction networks and changing amounts
DNAU-12 → DNAU-28 : prerequisite for Reaction networks and changing amounts
DNAU-25 → DNAU-28 : prerequisite for Reaction networks and changing amounts
DNAU-16 → DNAU-29 : prerequisite for Strand displacement in slow motion
DNAU-28 → DNAU-29 : prerequisite for Strand displacement in slow motion
DNAU-03 → DNAU-30 : prerequisite for Digital and analog molecular circuits
DNAU-28 → DNAU-30 : prerequisite for Digital and analog molecular circuits
DNAU-29 → DNAU-30 : prerequisite for Digital and analog molecular circuits
DNAU-11 → DNAU-31 : prerequisite for Local assembly, tiles and DNA origami
DNAU-16 → DNAU-31 : prerequisite for Local assembly, tiles and DNA origami
DNAU-25 → DNAU-31 : prerequisite for Local assembly, tiles and DNA origami
DNAU-30 → DNAU-31 : prerequisite for Local assembly, tiles and DNA origami
DNAU-09 → DNAU-32 : prerequisite for Genes, regulation, development and evolution
DNAU-13 → DNAU-32 : prerequisite for Genes, regulation, development and evolution
DNAU-14 → DNAU-32 : prerequisite for Genes, regulation, development and evolution
DNAU-28 → DNAU-32 : prerequisite for Genes, regulation, development and evolution
DNAU-30 → DNAU-32 : prerequisite for Genes, regulation, development and evolution
DNAU-02 → DNAU-33 : prerequisite for DNA storage, codes and recovery
DNAU-04 → DNAU-33 : prerequisite for DNA storage, codes and recovery
DNAU-11 → DNAU-33 : prerequisite for DNA storage, codes and recovery
DNAU-12 → DNAU-33 : prerequisite for DNA storage, codes and recovery
DNAU-20 → DNAU-33 : prerequisite for DNA storage, codes and recovery
DNAU-02 → DNAU-34 : prerequisite for Many numbers at once: vectors, matrices and DNA data
DNAU-03 → DNAU-34 : prerequisite for Many numbers at once: vectors, matrices and DNA data
DNAU-04 → DNAU-34 : prerequisite for Many numbers at once: vectors, matrices and DNA data
DNAU-12 → DNAU-34 : prerequisite for Many numbers at once: vectors, matrices and DNA data
DNAU-33 → DNAU-34 : prerequisite for Many numbers at once: vectors, matrices and DNA data
DNAU-24 → DNAU-35 : prerequisite for Resources, energy, reliability and design tools
DNAU-28 → DNAU-35 : prerequisite for Resources, energy, reliability and design tools
DNAU-30 → DNAU-35 : prerequisite for Resources, energy, reliability and design tools
DNAU-33 → DNAU-35 : prerequisite for Resources, energy, reliability and design tools
DNAU-34 → DNAU-35 : prerequisite for Resources, energy, reliability and design tools
DNAU-26 → DNAU-36 : prerequisite for A measured frontier and the bridge to Evolutor
DNAU-27 → DNAU-36 : prerequisite for A measured frontier and the bridge to Evolutor
DNAU-31 → DNAU-36 : prerequisite for A measured frontier and the bridge to Evolutor
DNAU-32 → DNAU-36 : prerequisite for A measured frontier and the bridge to Evolutor
DNAU-34 → DNAU-36 : prerequisite for A measured frontier and the bridge to Evolutor
DNAU-35 → DNAU-36 : prerequisite for A measured frontier and the bridge to Evolutor
```

## Cross-book handoff

The versioned [Book I exit contract](pedagogy/book-i-contract.json) lists chapter-specific terms and exit tasks. Evolutor imports only those explicit chapter outcomes, and recalls them in a short bridge before use. Its present status is planned-not-yet-taught. Neither unit tests nor this graph activate that contract. If an imported outcome is removed, either restore it in Book I or teach it locally before use in Book II.
