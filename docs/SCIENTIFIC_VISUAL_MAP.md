# Mechanism-first visual production map

Biology uses structures and reaction states; mathematics uses graphs and equations;
software uses UML and explicit state. Every figure needs a semantic TXT companion.
A molecular drawing labels 5′/3′ orientation, covalent backbone versus pairing,
binding/cleavage sites and what changes. Color is redundant with labels and shapes.
These per-chapter entries are plans, not a claim of completed artwork.

## DNAD-01 · Computing with DNA

Graph, strand encoding and selection panels.
State sequence: graph → candidate witness → molecular strategy.
Question/test anchor: Verify a nontrivial directed path and identify a filter-surviving invalid candidate.

## DNAD-02 · Adleman's experiment: from graph to molecules

Oriented oligos, tube ledger and gel interpretation.
State sequence: encoded strands → ligated pool → selected molecules → historical readout.
Question/test anchor: Reconstruct each operation from the primary paper; simulate filter losses and missing witnesses.

## DNAD-03 · Combinatorial search and complexity

Search tree with pruning and witness checks.
State sequence: candidate extension → rejection → surviving witness.
Question/test anchor: Build an exhaustive oracle and a polynomial witness checker; compare search and verification counts.

## DNAD-04 · Molecular parallelism and resource accounting

Resource curves with units and assumptions.
State sequence: candidate space → sampled population → recovered evidence.
Question/test anchor: Estimate a declared sampling budget and sensitivity to bias; do not assume uniform generation.

## DNAD-05 · DNA chemistry and sequence geometry

Chemical zoom and strand orientation.
State sequence: nucleotide → backbone → antiparallel duplex.
Question/test anchor: Implement reverse complement and test orientation, ambiguity and involution.

## DNAD-06 · Hybridization thermodynamics

Duplex populations and energy landscape.
State sequence: separate strands → competing duplexes → equilibrium population.
Question/test anchor: Compare symbolic matches with parameterized free-energy predictions; record parameter provenance.

## DNAD-07 · Reaction kinetics and stochastic chemistry

Reaction events and concentration trajectories.
State sequence: collision opportunity → reaction event → population evolution.
Question/test anchor: Simulate association; check conservation, units and stochastic versus deterministic limits.

## DNAD-08 · Enzymes as molecular operators

Bond-change panels with enzyme identities.
State sequence: substrates → enzyme-mediated change → products.
Question/test anchor: Trace ligation and restriction cases including incompatible ends and incomplete reactions.

## DNAD-09 · PCR, amplification and selection bias

PCR cycle and competing amplicons.
State sequence: denature → anneal → extend → biased population.
Question/test anchor: Compute amplification with variable efficiency and adversarial primer placement.

## DNAD-10 · Separation, detection and experimental logic

Sample provenance, gel lanes and readout.
State sequence: mixed sample → selected fraction → measured signal.
Question/test anchor: Interpret a synthetic gel with declared uncertainty and design positive/negative controls.

## DNAD-11 · Sequence design and graph encoding

Graph edge to antiparallel overlap mapping.
State sequence: graph constraint → sequence constraint → candidate design.
Question/test anchor: Construct an encoding and test orientation, off-target overlaps and hairpin risks.

## DNAD-12 · Generate–filter–verify algorithms

Candidate-survival ledger.
State sequence: generate → endpoint selection → size selection → coverage → verify.
Question/test anchor: Compare a symbolic filter simulator with an independent graph oracle.

## DNAD-13 · SAT and combinatorial constructions

Assignment tree and clause selection.
State sequence: assignment population → clause filters → verified assignment.
Question/test anchor: Implement a small SAT oracle and molecular abstraction; expose unsound or incomplete filters.

## DNAD-14 · Sticker systems and molecular memory

Molecular bit registers.
State sequence: blank register → selective marking → readout.
Question/test anchor: Execute a small register program and count operations, species and memory.

## DNAD-15 · Splicing and insertion–deletion systems

Cut sites and rewrite derivation.
State sequence: input words → permitted cuts → recombined words.
Question/test anchor: Write a bounded rewrite enumerator and verify hand-derived reachable strings.

## DNAD-16 · Languages, automata and molecular recognition

Automaton and reaction correspondence.
State sequence: input symbol → transition → acceptance state.
Question/test anchor: Build a finite-state recognizer and map its transitions to a proposed molecular scheme.

## DNAD-17 · Watson–Crick and biochemical automata

Paired inputs and transition reactions.
State sequence: paired input → permitted transition → accepted or rejected.
Question/test anchor: Trace acceptance on paired inputs; audit what the biochemical experiment actually implements.

## DNAD-18 · Universality and complexity models

Simulation map and resource ledger.
State sequence: source machine → molecular encoding → simulated transition.
Question/test anchor: Critique a universality argument by finding missing resources or illegal operations.

## DNAD-19 · Toehold-mediated strand displacement

Six molecular keyframes.
State sequence: gate → encounter → binding → migration → displacement → release.
Question/test anchor: Simulate a gate with explicit fuel and waste; test leak pathways.

## DNAD-20 · Chemical reaction networks as programs

Reaction graph and stoichiometric matrix.
State sequence: reaction specification → rate equations → DNA realization.
Question/test anchor: Implement a small CRN with independent conservation and nonnegativity checks.

## DNAD-21 · Digital and analog DNA circuits

Gate cascade with concentration traces.
State sequence: input concentrations → gate reaction → restored output.
Question/test anchor: Compare a truth table with concentration trajectories and resource depletion.

## DNAD-22 · Self-assembly, tiles and geometry

Tiles, glues and molecular scaffold zoom.
State sequence: seed → legal attachment → growing assembly.
Question/test anchor: Enumerate a small tile assembly and test illegal attachments and alternative growth orders.

## DNAD-23 · Noise, crosstalk and fault models

Fault propagation across layers.
State sequence: local fault → propagated effect → observed error.
Question/test anchor: Inject correlated faults into a filter or circuit model; quantify robust and fragile regimes.

## DNAD-24 · Scaling and resource limits

Resource budget and Pareto frontier.
State sequence: design size → resource demand → feasible regime.
Question/test anchor: Compare two algorithms at matched success probability, not only reaction-step count.

## DNAD-25 · Synthesis, sequencing and DNA storage

Write–store–read channel.
State sequence: encoding → synthesis/storage → noisy readout → decoding.
Question/test anchor: Recover a synthetic message under insertion/deletion/substitution errors.

## DNAD-26 · Laboratory workflows and reproducibility

Sample lineage and instrument workflow.
State sequence: design → prepare → react → separate → measure → interpret.
Question/test anchor: Design a documented non-operational experiment plan with controls and failure interpretation.

## DNAD-27 · Symbolic molecular simulation

Interpreter state and transitions.
State sequence: model → interpreter step → trace → oracle comparison.
Question/test anchor: Build a tested symbolic core shared by graph filters and rewriting systems.

## DNAD-28 · Kinetic and stochastic simulation

Reaction trace and simulation comparison.
State sequence: parameters → simulation → measured discrepancy.
Question/test anchor: Compare deterministic and stochastic trajectories under reproducible seeds and fitted uncertainty.

## DNAD-29 · Differentiable molecular and sequence models

Forward model and gradient path.
State sequence: design parameters → prediction → loss → update.
Question/test anchor: Use NumPy or PyTorch only where gradients or tensors serve the model; check finite differences.

## DNAD-30 · Genomic organization, regulation and development

Genome–expression–phenotype zoom.
State sequence: stored sequence → cellular regulation → expression → phenotype.
Question/test anchor: Analyze a small regulatory model and identify what it omits about a living system.

## DNAD-31 · Modern molecular programming and evidence

Historical mechanism map and evidence comparison.
State sequence: research claim → mechanism → experiment → bounded conclusion.
Question/test anchor: Produce a reproducible evidence comparison; refresh literature at drafting time.

## DNAD-32 · From molecular computation to genomic computation

Four-layer bridge.
State sequence: molecule → formal model → digital implementation → research hypothesis.
Question/test anchor: Complete the Book II handoff by formalizing one mechanism and rejecting an unsupported analogy.
