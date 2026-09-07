# DNA Computing: deep technical edition

Status: canonical deep Chapter 1 is an internally reviewed prototype; all later chapters remain plans. The undergraduate edition is frozen. No trained model, engine or wet-lab result is delivered. See [production report](DEEP_CHAPTER_1_REPORT.md) and [edition strategy](CANONICAL_EDITION_STRATEGY.md).

DOGMA = non-Transformer DNA-native model + DOGMA Engine; Hermon DNA = Transformer-based DNA model + Hermon DNA Engine; Evolutor = broader genomic computation theory, research and eventual runtime above both.

## Chapter dependencies, mechanisms and exit tasks

Entry assumptions: Basic programming and algorithmic reasoning; Algebra, functions, sets and discrete mathematical maturity; Basic probability, vectors, matrices and first-year calculus.

### DNAD-01 — Computing with DNA

**Required earlier chapters:** Declared entry assumptions.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** molecular computation; Hamiltonian witness; encoding and selection.

**Formal/mathematical development:** Define G=(V,E), specified endpoints and a permutation witness; distinguish formal acceptance from physical recovery.

**Implementation / assessment:** Verify a nontrivial directed path and identify a filter-surviving invalid candidate.

**Enables:** DNAD-02, DNAD-03, DNAD-05.

### DNAD-02 — Adleman's experiment: a mechanistic reconstruction

**Required earlier chapters:** DNAD-01.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** vertex and edge oligos; annealing and ligation; endpoint PCR; length and affinity selection; historical readout.

**Formal/mathematical development:** Derive ideal filter soundness and list physical completeness assumptions without inventing historical measurements.

**Implementation / assessment:** Reconstruct each operation from the primary paper; simulate filter losses and missing witnesses.

**Enables:** DNAD-04, DNAD-12.

### DNAD-03 — Combinatorial search and complexity

**Required earlier chapters:** DNAD-01.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** directed graphs; Hamiltonian paths; SAT; P; NP; reductions; verification.

**Formal/mathematical development:** Distinguish decision from search; prove a verifier bound and explain NP-completeness without claiming P differs from NP.

**Implementation / assessment:** Build an exhaustive oracle and a polynomial witness checker; compare search and verification counts.

**Enables:** DNAD-04, DNAD-11, DNAD-13, DNAD-16.

### DNAD-04 — Molecular parallelism and resource accounting

**Required earlier chapters:** DNAD-02, DNAD-03.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** sampling; material; concentration; reaction depth; readout; energy boundaries.

**Formal/mathematical development:** Derive miss probability (1-p)^M under declared independent sampling; separate factorial candidate space from physical yield.

**Implementation / assessment:** Estimate a declared sampling budget and sensitivity to bias; do not assume uniform generation.

**Enables:** DNAD-18, DNAD-24.

### DNAD-05 — DNA chemistry and sequence geometry

**Required earlier chapters:** DNAD-01.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** nucleotide; phosphodiester backbone; stacking; antiparallel duplex; reverse complement.

**Formal/mathematical development:** Map an oriented molecular diagram to strings without treating symbolic complementarity as binding prediction.

**Implementation / assessment:** Implement reverse complement and test orientation, ambiguity and involution.

**Enables:** DNAD-06, DNAD-07, DNAD-08, DNAD-17, DNAD-22, DNAD-25, DNAD-30.

### DNAD-06 — Hybridization thermodynamics

**Required earlier chapters:** DNAD-05.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** free energy; nearest-neighbor models; salt; concentration; melting; mismatch.

**Formal/mathematical development:** Derive equilibrium occupancy from a stated binding model with units and standard-state conventions.

**Implementation / assessment:** Compare symbolic matches with parameterized free-energy predictions; record parameter provenance.

**Enables:** DNAD-07, DNAD-09, DNAD-11, DNAD-19, DNAD-29.

### DNAD-07 — Reaction kinetics and stochastic chemistry

**Required earlier chapters:** DNAD-05, DNAD-06.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** mass action; stoichiometry; ODEs; stochastic trajectories; diffusion limits.

**Formal/mathematical development:** Derive rate equations from reaction stoichiometry; separate deterministic concentration from molecule counts.

**Implementation / assessment:** Simulate association; check conservation, units and stochastic versus deterministic limits.

**Enables:** DNAD-08, DNAD-19, DNAD-20, DNAD-28, DNAD-30.

### DNAD-08 — Enzymes as molecular operators

**Required earlier chapters:** DNAD-05, DNAD-07.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** polymerase; ligase; restriction; recognition; substrates; cofactors.

**Formal/mathematical development:** Give typed input/output abstractions and chemical preconditions; distinguish catalysis from information creation.

**Implementation / assessment:** Trace ligation and restriction cases including incompatible ends and incomplete reactions.

**Enables:** DNAD-09, DNAD-10, DNAD-15, DNAD-17, DNAD-26, DNAD-30.

### DNAD-09 — PCR, amplification and selection bias

**Required earlier chapters:** DNAD-06, DNAD-08.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** primer orientation; thermal cycling; specificity; efficiency; contamination.

**Formal/mathematical development:** Derive N_k=N_0(1+e)^k for constant efficiency and explain plateau and selection bias.

**Implementation / assessment:** Compute amplification with variable efficiency and adversarial primer placement.

**Enables:** DNAD-10, DNAD-26.

### DNAD-10 — Separation, detection and experimental logic

**Required earlier chapters:** DNAD-08, DNAD-09.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** electrophoresis; affinity purification; fluorescence; sequencing; controls.

**Formal/mathematical development:** Model retention and detection separately; distinguish evidence of presence from evidence of absence.

**Implementation / assessment:** Interpret a synthetic gel with declared uncertainty and design positive/negative controls.

**Enables:** DNAD-11, DNAD-23, DNAD-25, DNAD-26.

### DNAD-11 — Sequence design and graph encoding

**Required earlier chapters:** DNAD-03, DNAD-06, DNAD-10.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** orthogonality; overlaps; reverse-complement constraints; secondary structure.

**Formal/mathematical development:** Formulate design constraints and demonstrate why pairwise sequence distance is insufficient.

**Implementation / assessment:** Construct an encoding and test orientation, off-target overlaps and hairpin risks.

**Enables:** DNAD-12, DNAD-14, DNAD-15, DNAD-19, DNAD-27.

### DNAD-12 — Generate–filter–verify algorithms

**Required earlier chapters:** DNAD-02, DNAD-11.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** candidate multisets; predicates; soundness; completeness; physical loss.

**Formal/mathematical development:** Prove an ideal filtering invariant; extend it with stage-specific false-positive and false-negative events.

**Implementation / assessment:** Compare a symbolic filter simulator with an independent graph oracle.

**Enables:** DNAD-13, DNAD-14, DNAD-23, DNAD-27.

### DNAD-13 — SAT and combinatorial constructions

**Required earlier chapters:** DNAD-03, DNAD-12.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** Lipton encoding; clauses; selection; solution extraction.

**Formal/mathematical development:** Derive how a clause predicate acts on assignment encodings and account for exponential material.

**Implementation / assessment:** Implement a small SAT oracle and molecular abstraction; expose unsound or incomplete filters.

**Enables:** Research synthesis.

### DNAD-14 — Sticker systems and molecular memory

**Required earlier chapters:** DNAD-11, DNAD-12.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** memory strands; stickers; bit operations; register reuse.

**Formal/mathematical development:** Specify a chosen sticker-model variant and its allowed operations before any power claim.

**Implementation / assessment:** Execute a small register program and count operations, species and memory.

**Enables:** DNAD-18.

### DNAD-15 — Splicing and insertion–deletion systems

**Required earlier chapters:** DNAD-08, DNAD-11.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** cut-and-paste rules; context; insertion; deletion; molecular interpretation.

**Formal/mathematical development:** Define rule application precisely; separate formal closure results from realizable enzyme operations.

**Implementation / assessment:** Write a bounded rewrite enumerator and verify hand-derived reachable strings.

**Enables:** DNAD-16, DNAD-18, DNAD-27.

### DNAD-16 — Languages, automata and molecular recognition

**Required earlier chapters:** DNAD-03, DNAD-15.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** formal languages; grammars; automata; acceptance; transduction.

**Formal/mathematical development:** Develop formal definitions and a recognition example before molecular implementations.

**Implementation / assessment:** Build a finite-state recognizer and map its transitions to a proposed molecular scheme.

**Enables:** DNAD-17, DNAD-18.

### DNAD-17 — Watson–Crick and biochemical automata

**Required earlier chapters:** DNAD-05, DNAD-08, DNAD-16.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** paired-strand automata; complementarity relation; Benenson-style systems.

**Formal/mathematical development:** Distinguish mathematical automaton variants and finite experimental implementations.

**Implementation / assessment:** Trace acceptance on paired inputs; audit what the biochemical experiment actually implements.

**Enables:** DNAD-18, DNAD-27.

### DNAD-18 — Universality and complexity models

**Required earlier chapters:** DNAD-04, DNAD-14, DNAD-15, DNAD-16, DNAD-17.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** Turing completeness; simulations; uniformity; resource vectors.

**Formal/mathematical development:** State model assumptions and sketch a valid simulation proof; no finite experiment proves unbounded universality.

**Implementation / assessment:** Critique a universality argument by finding missing resources or illegal operations.

**Enables:** DNAD-20, DNAD-22, DNAD-24, DNAD-32.

### DNAD-19 — Toehold-mediated strand displacement

**Required earlier chapters:** DNAD-06, DNAD-07, DNAD-11.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** toehold binding; branch migration; release; leakage.

**Formal/mathematical development:** Introduce domain notation, conservation and kinetic abstractions after oriented strand frames.

**Implementation / assessment:** Simulate a gate with explicit fuel and waste; test leak pathways.

**Enables:** DNAD-20, DNAD-21, DNAD-23, DNAD-28.

### DNAD-20 — Chemical reaction networks as programs

**Required earlier chapters:** DNAD-07, DNAD-18, DNAD-19.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** species; stoichiometry; mass action; compositional encodings.

**Formal/mathematical development:** Derive deterministic and stochastic semantics, then explain DNA implementation assumptions.

**Implementation / assessment:** Implement a small CRN with independent conservation and nonnegativity checks.

**Enables:** DNAD-21, DNAD-28.

### DNAD-21 — Digital and analog DNA circuits

**Required earlier chapters:** DNAD-19, DNAD-20.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** logic; thresholds; restoration; feedback; fan-out; depletion.

**Formal/mathematical development:** Derive signal conventions and explain when isolated gate behavior fails under composition.

**Implementation / assessment:** Compare a truth table with concentration trajectories and resource depletion.

**Enables:** DNAD-23, DNAD-24, DNAD-31.

### DNAD-22 — Self-assembly, tiles and geometry

**Required earlier chapters:** DNAD-05, DNAD-18.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** Seeman structures; Wang tiles; aTAM; glue strengths; assembly sequences; origami.

**Formal/mathematical development:** Define tile attachment threshold and legal assembly; separate geometry, addressability and computation.

**Implementation / assessment:** Enumerate a small tile assembly and test illegal attachments and alternative growth orders.

**Enables:** DNAD-24, DNAD-31.

### DNAD-23 — Noise, crosstalk and fault models

**Required earlier chapters:** DNAD-10, DNAD-12, DNAD-19, DNAD-21.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** synthesis error; mismatch; leak; PCR bias; false positives; false negatives.

**Formal/mathematical development:** Compose error channels only under justified dependence assumptions.

**Implementation / assessment:** Inject correlated faults into a filter or circuit model; quantify robust and fragile regimes.

**Enables:** DNAD-24, DNAD-25, DNAD-26, DNAD-28.

### DNAD-24 — Scaling and resource limits

**Required earlier chapters:** DNAD-04, DNAD-18, DNAD-21, DNAD-22, DNAD-23.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** material; species; volume; latency; energy; detection; parallelism.

**Formal/mathematical development:** Build a multidimensional cost model with declared system boundaries.

**Implementation / assessment:** Compare two algorithms at matched success probability, not only reaction-step count.

**Enables:** DNAD-26, DNAD-31, DNAD-32.

### DNAD-25 — Synthesis, sequencing and DNA storage

**Required earlier chapters:** DNAD-05, DNAD-10, DNAD-23.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** writing; coding; redundancy; access; sequencing channels; storage versus computation.

**Formal/mathematical development:** Derive a toy coding overhead and error model without conflating stored bits with executed operations.

**Implementation / assessment:** Recover a synthetic message under insertion/deletion/substitution errors.

**Enables:** DNAD-29.

### DNAD-26 — Laboratory workflows and reproducibility

**Required earlier chapters:** DNAD-08, DNAD-09, DNAD-10, DNAD-23, DNAD-24.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** oligo design; purification; mixing; reaction; controls; measurement; provenance.

**Formal/mathematical development:** Connect operational checklists to statistical inference and measurement uncertainty.

**Implementation / assessment:** Design a documented non-operational experiment plan with controls and failure interpretation.

**Enables:** DNAD-31.

### DNAD-27 — Symbolic molecular simulation

**Required earlier chapters:** DNAD-11, DNAD-12, DNAD-15, DNAD-17.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** strings; multisets; rule interpreters; bounded search; independent oracles.

**Formal/mathematical development:** Specify interpreter semantics and prove a small invariant before optimization.

**Implementation / assessment:** Build a tested symbolic core shared by graph filters and rewriting systems.

**Enables:** DNAD-28.

### DNAD-28 — Kinetic and stochastic simulation

**Required earlier chapters:** DNAD-07, DNAD-19, DNAD-20, DNAD-23, DNAD-27.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** ODE integration; stochastic simulation; parameter fitting; model validation.

**Formal/mathematical development:** Derive event propensities and discuss stiffness, identifiability and approximation error.

**Implementation / assessment:** Compare deterministic and stochastic trajectories under reproducible seeds and fitted uncertainty.

**Enables:** DNAD-29, DNAD-31.

### DNAD-29 — Differentiable molecular and sequence models

**Required earlier chapters:** DNAD-06, DNAD-25, DNAD-28.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** sensitivity; inverse design; tensors; gradients; DNA representations.

**Formal/mathematical development:** Derive a simple differentiable objective and distinguish surrogate accuracy from physical validation.

**Implementation / assessment:** Use NumPy or PyTorch only where gradients or tensors serve the model; check finite differences.

**Enables:** DNAD-31, DNAD-32.

### DNAD-30 — Genomic organization, regulation and development

**Required earlier chapters:** DNAD-05, DNAD-07, DNAD-08.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** genes; RNA; proteins; promoters; regulatory networks; development; inheritance; selection.

**Formal/mathematical development:** Separate molecular mechanisms, dynamical state, parameter change and population evolution.

**Implementation / assessment:** Analyze a small regulatory model and identify what it omits about a living system.

**Enables:** DNAD-32.

### DNAD-31 — Modern molecular programming and evidence

**Required earlier chapters:** DNAD-21, DNAD-22, DNAD-24, DNAD-26, DNAD-28, DNAD-29.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** circuits; assembly; sensing; in-vitro and in-vivo boundaries; current literature.

**Formal/mathematical development:** Reconstruct selected primary results with assumptions, controls, resources and uncertainty.

**Implementation / assessment:** Produce a reproducible evidence comparison; refresh literature at drafting time.

**Enables:** DNAD-32.

### DNAD-32 — From molecular computation to genomic computation

**Required earlier chapters:** DNAD-18, DNAD-24, DNAD-29, DNAD-30, DNAD-31.

**Book I imports:** None. DNAD-01 is prototype-available; later imports remain future teaching dependencies, not completed outcomes.

**Mechanisms and concepts:** physical molecule; formal string; simulator; learned representation; computational analogy.

**Formal/mathematical development:** Define cross-layer mappings and identify which properties survive abstraction.

**Implementation / assessment:** Complete the Book II handoff by formalizing one mechanism and rejecting an unsupported analogy.

**Enables:** Research synthesis.
