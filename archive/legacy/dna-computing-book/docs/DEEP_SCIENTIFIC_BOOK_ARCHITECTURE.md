# Deep scientific architecture: refinement proposal

Preserve the current 32 chapters and 7 parts.
No chapter files are moved. Chapters 1–2 retain acceptance; Chapter 3 is the next unfinished chapter.
This source-derived map adds scientific gates; it does not turn planned chapters into manuscripts.

## DNAD-01 · Computing with DNA

- **Central question:** How do molecular computation, Hamiltonian witness, encoding and selection support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** Declared entry assumptions.
- **Book I imports:** None additional.
- **Mathematics:** Define G=(V,E), specified endpoints and a permutation witness; distinguish formal acceptance from physical recovery.
- **Implementation / experiment:** Verify a nontrivial directed path and identify a filter-surviving invalid candidate.
- **Principal figure:** Graph, strand encoding and selection panels.
- **Keyframes:** graph → candidate witness → molecular strategy.
- **Research status:** internally-reviewed-draft in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-02 · Adleman's experiment: from graph to molecules

- **Central question:** How do vertex and edge oligos, annealing and ligation, endpoint PCR, length and affinity selection, historical readout support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-01.
- **Book I imports:** None additional.
- **Mathematics:** Derive ideal filter soundness and list physical completeness assumptions without inventing historical measurements.
- **Implementation / experiment:** Reconstruct each operation from the primary paper; simulate filter losses and missing witnesses.
- **Principal figure:** Oriented oligos, tube ledger and gel interpretation.
- **Keyframes:** encoded strands → ligated pool → selected molecules → historical readout.
- **Research status:** internally-reviewed-draft in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-03 · Combinatorial search and complexity

- **Central question:** How do directed graphs, Hamiltonian paths, SAT, P, NP, reductions, verification support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-01.
- **Book I imports:** None additional.
- **Mathematics:** Distinguish decision from search; prove a verifier bound and explain NP-completeness without claiming P differs from NP.
- **Implementation / experiment:** Build an exhaustive oracle and a polynomial witness checker; compare search and verification counts.
- **Principal figure:** Search tree with pruning and witness checks.
- **Keyframes:** candidate extension → rejection → surviving witness.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-04 · Molecular parallelism and resource accounting

- **Central question:** How do sampling, material, concentration, reaction depth, readout, energy boundaries support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-02, DNAD-03.
- **Book I imports:** None additional.
- **Mathematics:** Derive miss probability (1-p)^M under declared independent sampling; separate factorial candidate space from physical yield.
- **Implementation / experiment:** Estimate a declared sampling budget and sensitivity to bias; do not assume uniform generation.
- **Principal figure:** Resource curves with units and assumptions.
- **Keyframes:** candidate space → sampled population → recovered evidence.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-05 · DNA chemistry and sequence geometry

- **Central question:** How do nucleotide, phosphodiester backbone, stacking, antiparallel duplex, reverse complement support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-01.
- **Book I imports:** None additional.
- **Mathematics:** Map an oriented molecular diagram to strings without treating symbolic complementarity as binding prediction.
- **Implementation / experiment:** Implement reverse complement and test orientation, ambiguity and involution.
- **Principal figure:** Chemical zoom and strand orientation.
- **Keyframes:** nucleotide → backbone → antiparallel duplex.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-06 · Hybridization thermodynamics

- **Central question:** How do free energy, nearest-neighbor models, salt, concentration, melting, mismatch support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-05.
- **Book I imports:** None additional.
- **Mathematics:** Derive equilibrium occupancy from a stated binding model with units and standard-state conventions.
- **Implementation / experiment:** Compare symbolic matches with parameterized free-energy predictions; record parameter provenance.
- **Principal figure:** Duplex populations and energy landscape.
- **Keyframes:** separate strands → competing duplexes → equilibrium population.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-07 · Reaction kinetics and stochastic chemistry

- **Central question:** How do mass action, stoichiometry, ODEs, stochastic trajectories, diffusion limits support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-05, DNAD-06.
- **Book I imports:** None additional.
- **Mathematics:** Derive rate equations from reaction stoichiometry; separate deterministic concentration from molecule counts.
- **Implementation / experiment:** Simulate association; check conservation, units and stochastic versus deterministic limits.
- **Principal figure:** Reaction events and concentration trajectories.
- **Keyframes:** collision opportunity → reaction event → population evolution.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-08 · Enzymes as molecular operators

- **Central question:** How do polymerase, ligase, restriction, recognition, substrates, cofactors support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-05, DNAD-07.
- **Book I imports:** None additional.
- **Mathematics:** Give typed input/output abstractions and chemical preconditions; distinguish catalysis from information creation.
- **Implementation / experiment:** Trace ligation and restriction cases including incompatible ends and incomplete reactions.
- **Principal figure:** Bond-change panels with enzyme identities.
- **Keyframes:** substrates → enzyme-mediated change → products.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-09 · PCR, amplification and selection bias

- **Central question:** How do primer orientation, thermal cycling, specificity, efficiency, contamination support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-06, DNAD-08.
- **Book I imports:** None additional.
- **Mathematics:** Derive N_k=N_0(1+e)^k for constant efficiency and explain plateau and selection bias.
- **Implementation / experiment:** Compute amplification with variable efficiency and adversarial primer placement.
- **Principal figure:** PCR cycle and competing amplicons.
- **Keyframes:** denature → anneal → extend → biased population.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-10 · Separation, detection and experimental logic

- **Central question:** How do electrophoresis, affinity purification, fluorescence, sequencing, controls support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-08, DNAD-09.
- **Book I imports:** None additional.
- **Mathematics:** Model retention and detection separately; distinguish evidence of presence from evidence of absence.
- **Implementation / experiment:** Interpret a synthetic gel with declared uncertainty and design positive/negative controls.
- **Principal figure:** Sample provenance, gel lanes and readout.
- **Keyframes:** mixed sample → selected fraction → measured signal.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-11 · Sequence design and graph encoding

- **Central question:** How do orthogonality, overlaps, reverse-complement constraints, secondary structure support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-03, DNAD-06, DNAD-10.
- **Book I imports:** None additional.
- **Mathematics:** Formulate design constraints and demonstrate why pairwise sequence distance is insufficient.
- **Implementation / experiment:** Construct an encoding and test orientation, off-target overlaps and hairpin risks.
- **Principal figure:** Graph edge to antiparallel overlap mapping.
- **Keyframes:** graph constraint → sequence constraint → candidate design.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-12 · Generate–filter–verify algorithms

- **Central question:** How do candidate multisets, predicates, soundness, completeness, physical loss support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-02, DNAD-11.
- **Book I imports:** None additional.
- **Mathematics:** Prove an ideal filtering invariant; extend it with stage-specific false-positive and false-negative events.
- **Implementation / experiment:** Compare a symbolic filter simulator with an independent graph oracle.
- **Principal figure:** Candidate-survival ledger.
- **Keyframes:** generate → endpoint selection → size selection → coverage → verify.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-13 · SAT and combinatorial constructions

- **Central question:** How do Lipton encoding, clauses, selection, solution extraction support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-03, DNAD-12.
- **Book I imports:** None additional.
- **Mathematics:** Derive how a clause predicate acts on assignment encodings and account for exponential material.
- **Implementation / experiment:** Implement a small SAT oracle and molecular abstraction; expose unsound or incomplete filters.
- **Principal figure:** Assignment tree and clause selection.
- **Keyframes:** assignment population → clause filters → verified assignment.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-14 · Sticker systems and molecular memory

- **Central question:** How do memory strands, stickers, bit operations, register reuse support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-11, DNAD-12.
- **Book I imports:** None additional.
- **Mathematics:** Specify a chosen sticker-model variant and its allowed operations before any power claim.
- **Implementation / experiment:** Execute a small register program and count operations, species and memory.
- **Principal figure:** Molecular bit registers.
- **Keyframes:** blank register → selective marking → readout.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-15 · Splicing and insertion–deletion systems

- **Central question:** How do cut-and-paste rules, context, insertion, deletion, molecular interpretation support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-08, DNAD-11.
- **Book I imports:** None additional.
- **Mathematics:** Define rule application precisely; separate formal closure results from realizable enzyme operations.
- **Implementation / experiment:** Write a bounded rewrite enumerator and verify hand-derived reachable strings.
- **Principal figure:** Cut sites and rewrite derivation.
- **Keyframes:** input words → permitted cuts → recombined words.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-16 · Languages, automata and molecular recognition

- **Central question:** How do formal languages, grammars, automata, acceptance, transduction support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-03, DNAD-15.
- **Book I imports:** None additional.
- **Mathematics:** Develop formal definitions and a recognition example before molecular implementations.
- **Implementation / experiment:** Build a finite-state recognizer and map its transitions to a proposed molecular scheme.
- **Principal figure:** Automaton and reaction correspondence.
- **Keyframes:** input symbol → transition → acceptance state.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-17 · Watson–Crick and biochemical automata

- **Central question:** How do paired-strand automata, complementarity relation, Benenson-style systems support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-05, DNAD-08, DNAD-16.
- **Book I imports:** None additional.
- **Mathematics:** Distinguish mathematical automaton variants and finite experimental implementations.
- **Implementation / experiment:** Trace acceptance on paired inputs; audit what the biochemical experiment actually implements.
- **Principal figure:** Paired inputs and transition reactions.
- **Keyframes:** paired input → permitted transition → accepted or rejected.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-18 · Universality and complexity models

- **Central question:** How do Turing completeness, simulations, uniformity, resource vectors support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-04, DNAD-14, DNAD-15, DNAD-16, DNAD-17.
- **Book I imports:** None additional.
- **Mathematics:** State model assumptions and sketch a valid simulation proof; no finite experiment proves unbounded universality.
- **Implementation / experiment:** Critique a universality argument by finding missing resources or illegal operations.
- **Principal figure:** Simulation map and resource ledger.
- **Keyframes:** source machine → molecular encoding → simulated transition.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-19 · Toehold-mediated strand displacement

- **Central question:** How do toehold binding, branch migration, release, leakage support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-06, DNAD-07, DNAD-11.
- **Book I imports:** None additional.
- **Mathematics:** Introduce domain notation, conservation and kinetic abstractions after oriented strand frames.
- **Implementation / experiment:** Simulate a gate with explicit fuel and waste; test leak pathways.
- **Principal figure:** Six molecular keyframes.
- **Keyframes:** gate → encounter → binding → migration → displacement → release.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-20 · Chemical reaction networks as programs

- **Central question:** How do species, stoichiometry, mass action, compositional encodings support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-07, DNAD-18, DNAD-19.
- **Book I imports:** None additional.
- **Mathematics:** Derive deterministic and stochastic semantics, then explain DNA implementation assumptions.
- **Implementation / experiment:** Implement a small CRN with independent conservation and nonnegativity checks.
- **Principal figure:** Reaction graph and stoichiometric matrix.
- **Keyframes:** reaction specification → rate equations → DNA realization.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-21 · Digital and analog DNA circuits

- **Central question:** How do logic, thresholds, restoration, feedback, fan-out, depletion support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-19, DNAD-20.
- **Book I imports:** None additional.
- **Mathematics:** Derive signal conventions and explain when isolated gate behavior fails under composition.
- **Implementation / experiment:** Compare a truth table with concentration trajectories and resource depletion.
- **Principal figure:** Gate cascade with concentration traces.
- **Keyframes:** input concentrations → gate reaction → restored output.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-22 · Self-assembly, tiles and geometry

- **Central question:** How do Seeman structures, Wang tiles, aTAM, glue strengths, assembly sequences, origami support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-05, DNAD-18.
- **Book I imports:** None additional.
- **Mathematics:** Define tile attachment threshold and legal assembly; separate geometry, addressability and computation.
- **Implementation / experiment:** Enumerate a small tile assembly and test illegal attachments and alternative growth orders.
- **Principal figure:** Tiles, glues and molecular scaffold zoom.
- **Keyframes:** seed → legal attachment → growing assembly.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-23 · Noise, crosstalk and fault models

- **Central question:** How do synthesis error, mismatch, leak, PCR bias, false positives, false negatives support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-10, DNAD-12, DNAD-19, DNAD-21.
- **Book I imports:** None additional.
- **Mathematics:** Compose error channels only under justified dependence assumptions.
- **Implementation / experiment:** Inject correlated faults into a filter or circuit model; quantify robust and fragile regimes.
- **Principal figure:** Fault propagation across layers.
- **Keyframes:** local fault → propagated effect → observed error.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-24 · Scaling and resource limits

- **Central question:** How do material, species, volume, latency, energy, detection, parallelism support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-04, DNAD-18, DNAD-21, DNAD-22, DNAD-23.
- **Book I imports:** None additional.
- **Mathematics:** Build a multidimensional cost model with declared system boundaries.
- **Implementation / experiment:** Compare two algorithms at matched success probability, not only reaction-step count.
- **Principal figure:** Resource budget and Pareto frontier.
- **Keyframes:** design size → resource demand → feasible regime.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-25 · Synthesis, sequencing and DNA storage

- **Central question:** How do writing, coding, redundancy, access, sequencing channels, storage versus computation support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-05, DNAD-10, DNAD-23.
- **Book I imports:** None additional.
- **Mathematics:** Derive a toy coding overhead and error model without conflating stored bits with executed operations.
- **Implementation / experiment:** Recover a synthetic message under insertion/deletion/substitution errors.
- **Principal figure:** Write–store–read channel.
- **Keyframes:** encoding → synthesis/storage → noisy readout → decoding.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-26 · Laboratory workflows and reproducibility

- **Central question:** How do oligo design, purification, mixing, reaction, controls, measurement, provenance support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-08, DNAD-09, DNAD-10, DNAD-23, DNAD-24.
- **Book I imports:** None additional.
- **Mathematics:** Connect operational checklists to statistical inference and measurement uncertainty.
- **Implementation / experiment:** Design a documented non-operational experiment plan with controls and failure interpretation.
- **Principal figure:** Sample lineage and instrument workflow.
- **Keyframes:** design → prepare → react → separate → measure → interpret.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-27 · Symbolic molecular simulation

- **Central question:** How do strings, multisets, rule interpreters, bounded search, independent oracles support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-11, DNAD-12, DNAD-15, DNAD-17.
- **Book I imports:** None additional.
- **Mathematics:** Specify interpreter semantics and prove a small invariant before optimization.
- **Implementation / experiment:** Build a tested symbolic core shared by graph filters and rewriting systems.
- **Principal figure:** Interpreter state and transitions.
- **Keyframes:** model → interpreter step → trace → oracle comparison.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-28 · Kinetic and stochastic simulation

- **Central question:** How do ODE integration, stochastic simulation, parameter fitting, model validation support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-07, DNAD-19, DNAD-20, DNAD-23, DNAD-27.
- **Book I imports:** None additional.
- **Mathematics:** Derive event propensities and discuss stiffness, identifiability and approximation error.
- **Implementation / experiment:** Compare deterministic and stochastic trajectories under reproducible seeds and fitted uncertainty.
- **Principal figure:** Reaction trace and simulation comparison.
- **Keyframes:** parameters → simulation → measured discrepancy.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-29 · Differentiable molecular and sequence models

- **Central question:** How do sensitivity, inverse design, tensors, gradients, DNA representations support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-06, DNAD-25, DNAD-28.
- **Book I imports:** None additional.
- **Mathematics:** Derive a simple differentiable objective and distinguish surrogate accuracy from physical validation.
- **Implementation / experiment:** Use NumPy or PyTorch only where gradients or tensors serve the model; check finite differences.
- **Principal figure:** Forward model and gradient path.
- **Keyframes:** design parameters → prediction → loss → update.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-30 · Genomic organization, regulation and development

- **Central question:** How do genes, RNA, proteins, promoters, regulatory networks, development, inheritance, selection support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-05, DNAD-07, DNAD-08.
- **Book I imports:** None additional.
- **Mathematics:** Separate molecular mechanisms, dynamical state, parameter change and population evolution.
- **Implementation / experiment:** Analyze a small regulatory model and identify what it omits about a living system.
- **Principal figure:** Genome–expression–phenotype zoom.
- **Keyframes:** stored sequence → cellular regulation → expression → phenotype.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-31 · Modern molecular programming and evidence

- **Central question:** How do circuits, assembly, sensing, in-vitro and in-vivo boundaries, current literature support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-21, DNAD-22, DNAD-24, DNAD-26, DNAD-28, DNAD-29.
- **Book I imports:** None additional.
- **Mathematics:** Reconstruct selected primary results with assumptions, controls, resources and uncertainty.
- **Implementation / experiment:** Produce a reproducible evidence comparison; refresh literature at drafting time.
- **Principal figure:** Historical mechanism map and evidence comparison.
- **Keyframes:** research claim → mechanism → experiment → bounded conclusion.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.

## DNAD-32 · From molecular computation to genomic computation

- **Central question:** How do physical molecule, formal string, simulator, learned representation, computational analogy support this chapter's stated mechanism?
- **Scientific context:** Molecular interpretation and limitations must accompany the formal object.
- **Prerequisites:** DNAD-18, DNAD-24, DNAD-29, DNAD-30, DNAD-31.
- **Book I imports:** None additional.
- **Mathematics:** Define cross-layer mappings and identify which properties survive abstraction.
- **Implementation / experiment:** Complete the Book II handoff by formalizing one mechanism and rejecting an unsupported analogy.
- **Principal figure:** Four-layer bridge.
- **Keyframes:** molecule → formal model → digital implementation → research hypothesis.
- **Research status:** planned-not-drafted in canonical metadata; Chapter 3 has a separate working draft.
- **Acceptance:** source-level evidence, stated assumptions, independent numerical/logic check, failure case and every-page visual review.
