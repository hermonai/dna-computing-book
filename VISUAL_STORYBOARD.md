# DNA Computing: deep technical edition

Status: canonical deep Chapters 1–2 are internally reviewed development manuscripts; Chapter 3 onward remains planned. Prior editions and the Chapter 1-only PDF are preserved. No new wet-lab result, trained model or engine benchmark is delivered. See [Chapter 2 production report](DEEP_CHAPTER_2_REPORT.md).

DOGMA = non-Transformer DNA-native model + DOGMA Engine; Hermon DNA = Transformer-based DNA model + Hermon DNA Engine; Evolutor = broader genomic computation theory, research and eventual runtime above both.

## Figure and animation strategy

Each primary visual below is a production brief, not a finished asset or a one-figure quota. Use oriented molecular illustrations, chemical reaction/energy diagrams, graphs, tensor flows, UML and memory layouts as appropriate. Preserve semantic Unicode TXT companions; no ASCII box art. Create figure-specific frame ledgers before prose: before-state, changed/unchanged objects, movement, creation/consumption, meaning of arrows, caption and scientific risk. Abstraction is allowed, but its relation to the mechanism must be explicit.

### DNAD-01 — Computing with DNA

**DNAD-01-F1 — Computing across three descriptions**. Keep graph constraints, molecular operations and decoded evidence in separate lanes.

1. Specify graph.
2. Encode candidate.
3. Operate on molecules.
4. Observe and verify.

**DNAD-01-F2 — A directed graph with two valid witnesses**. Show six vertices and all nine directed edges; retain node positions across route overlays.

1. Draw vertices.
2. Add directed edges.
3. Highlight a valid route.

**DNAD-01-F3 — Why plausible routes fail**. Compare valid, repeated, missing and illegal-edge candidates with exact rejection reasons.

1. Read route.
2. Check endpoints and length.
3. Check coverage.
4. Verify every edge.

**DNAD-01-F4 — A vertex splint aligns two directed edges**. Draw 5′/3′ edge strands, adjacent domains and an antiparallel splint beneath the nick.

1. Edge into B.
2. Edge out of B.
3. Complementary B splint aligns ends.
4. Ligase closes compatible nick.

**DNAD-01-F5 — One mixture contains many candidate identities**. Use the same route IDs in pool and filtering diagrams; multiplicity is distinct from coverage.

1. Mixed components.
2. Candidate assembly.
3. Repeated identities.
4. Absent or unwanted products.

**DNAD-01-F6 — From graph to a checked witness**. Nine stage panels grouped as design, chemistry and evidence; each panel is labeled by its role.

1. Graph vertices.
2. Vertex codes.
3. Edge overlaps.
4. Mix.
5. Candidate formation.
6. Endpoint selection.
7. Length selection.
8. Vertex selection.
9. Witness check.

**DNAD-01-F7 — Predicates meet laboratory operations**. Map joining, endpoints, size, vertex presence and evidence to operations and failure modes.

1. Join compatible ends.
2. Enrich endpoint-compatible material.
3. Select size.
4. Retain complementary sequence.
5. Interpret measurement.

**DNAD-01-F8 — A length profile is not automatically one route**. Draw schematic graduated-primer lanes for a known teaching route and explain mixture ambiguity.

1. Choose start and internal primer.
2. Predict amplicon length.
3. Read several lanes.
4. Check route ambiguity.

**DNAD-01-F9 — Candidate space becomes a material budget**. Plot log10 factorial candidate counts for fixed endpoints with marked axes; pair with molecule-budget equation.

1. Count internal orders.
2. Specify hit probability.
3. Budget repeated samples.
4. Account for losses and readout.

**DNAD-01-F10 — The field expanded its programming mechanisms**. Map search/filter, automata, CRNs/circuits and self-assembly; keep storage and learned DNA models distinct.

1. Molecular operators.
2. Formal models.
3. Programmable dynamics.
4. Engineering constraints.

### DNAD-02 — Adleman's experiment: from graph to molecules

**DNAD-02-F1 — The historical graph, redrawn**. Seven labeled vertices; fourteen directed edges; start 0 and target 6

1. Read adjacency row by row; trace 0→1→2→3→4→5→6.

**DNAD-02-F2 — Four routes, four logical cases**. Witness; legal short route; repeated-vertex walk; illegal-edge permutation

1. Compare endpoints, adjacency, length and coverage independently.

**DNAD-02-F3 — From a code to an oriented edge**. Historical O2, O3, O4; left/right ten-base domains; O23 and O34

1. Split codes; concatenate R2 L3 and R3 L4; compare with printed figure.

**DNAD-02-F4 — Association is not a backbone bond**. Two edge fragments; antiparallel vertex splint; 3′ OH and 5′ phosphate nick

1. Separated fragments; aligned duplex with nick; continuous ligated upper backbone.

**DNAD-02-F5 — A tube is a multiset, not a search tree**. Digital route enumeration; physical candidate copies; absent witness

1. Enumerate one route at a time; contrast simultaneous unequal molecular copies.

**DNAD-02-F6 — Endpoint amplification and information flow**. Double-stranded template; forward and reverse primers; products

1. Denature; inward-facing annealing; 5′→3′ extension; selected-family enrichment.

**DNAD-02-F7 — Length selects occurrences, not identities**. 120,140,160-bp conceptual products; equal-length correct/repeated routes

1. Separate by size; retain target fraction; compare same-size sequence orders.

**DNAD-02-F8 — Two bead operations, different retained material**. Biotinylated strand; duplex; bead; free strand; sequence probe

1. Immobilize biotin strand then denature/recover other strand; bind target to probe then wash/elute.

**DNAD-02-F9 — Presence filtering consumes uncertainty and material**. Exact route rows; required vertices 1–5; survival counts

1. Apply successive presence predicates and expose every count.

**DNAD-02-F10 — One computation, three representations**. Logical predicate; physical property; laboratory action; failure mode

1. Read aligned rows from preparation through verification.

**DNAD-02-F11 — A lane set is a projection of a population**. Historical witness/short/repeated routes; synthetic expected band sets

1. Map occurrences to 20(j+1) bp; union bands across routes; compare mixtures.

**DNAD-02-F12 — Soundness and survival pull in different directions**. True witness copies; false candidates; conditional retention; no-signal event

1. Propagate expected counts; compute zero-survivor probability under stated independence.

**DNAD-02-F13 — Count materials before celebrating parallelism**. Historical reagent amount; copies; species; volume; fixed-endpoint permutation space

1. Convert units; separate initial oligos from complete routes; expose sampling assumptions.

**DNAD-02-F14 — Several mechanisms grew beyond generate-and-filter**. SAT filtering; formal systems; automata; assembly; strand displacement

1. Compare state, operation and readout across categories without a causal genealogy.

### DNAD-03 — Combinatorial search and complexity

**DNAD-03-F1 — Search tree with pruning and witness checks**. Search tree with pruning and witness checks

1. candidate extension.
2. rejection.
3. surviving witness.

### DNAD-04 — Molecular parallelism and resource accounting

**DNAD-04-F1 — Resource curves with units and assumptions**. Resource curves with units and assumptions

1. candidate space.
2. sampled population.
3. recovered evidence.

### DNAD-05 — DNA chemistry and sequence geometry

**DNAD-05-F1 — Chemical zoom and strand orientation**. Chemical zoom and strand orientation

1. nucleotide.
2. backbone.
3. antiparallel duplex.

### DNAD-06 — Hybridization thermodynamics

**DNAD-06-F1 — Duplex populations and energy landscape**. Duplex populations and energy landscape

1. separate strands.
2. competing duplexes.
3. equilibrium population.

### DNAD-07 — Reaction kinetics and stochastic chemistry

**DNAD-07-F1 — Reaction events and concentration trajectories**. Reaction events and concentration trajectories

1. collision opportunity.
2. reaction event.
3. population evolution.

### DNAD-08 — Enzymes as molecular operators

**DNAD-08-F1 — Bond-change panels with enzyme identities**. Bond-change panels with enzyme identities

1. substrates.
2. enzyme-mediated change.
3. products.

### DNAD-09 — PCR, amplification and selection bias

**DNAD-09-F1 — PCR cycle and competing amplicons**. PCR cycle and competing amplicons

1. denature.
2. anneal.
3. extend.
4. biased population.

### DNAD-10 — Separation, detection and experimental logic

**DNAD-10-F1 — Sample provenance, gel lanes and readout**. Sample provenance, gel lanes and readout

1. mixed sample.
2. selected fraction.
3. measured signal.

### DNAD-11 — Sequence design and graph encoding

**DNAD-11-F1 — Graph edge to antiparallel overlap mapping**. Graph edge to antiparallel overlap mapping

1. graph constraint.
2. sequence constraint.
3. candidate design.

### DNAD-12 — Generate–filter–verify algorithms

**DNAD-12-F1 — Candidate-survival ledger**. Candidate-survival ledger

1. generate.
2. endpoint selection.
3. size selection.
4. coverage.
5. verify.

### DNAD-13 — SAT and combinatorial constructions

**DNAD-13-F1 — Assignment tree and clause selection**. Assignment tree and clause selection

1. assignment population.
2. clause filters.
3. verified assignment.

### DNAD-14 — Sticker systems and molecular memory

**DNAD-14-F1 — Molecular bit registers**. Molecular bit registers

1. blank register.
2. selective marking.
3. readout.

### DNAD-15 — Splicing and insertion–deletion systems

**DNAD-15-F1 — Cut sites and rewrite derivation**. Cut sites and rewrite derivation

1. input words.
2. permitted cuts.
3. recombined words.

### DNAD-16 — Languages, automata and molecular recognition

**DNAD-16-F1 — Automaton and reaction correspondence**. Automaton and reaction correspondence

1. input symbol.
2. transition.
3. acceptance state.

### DNAD-17 — Watson–Crick and biochemical automata

**DNAD-17-F1 — Paired inputs and transition reactions**. Paired inputs and transition reactions

1. paired input.
2. permitted transition.
3. accepted or rejected.

### DNAD-18 — Universality and complexity models

**DNAD-18-F1 — Simulation map and resource ledger**. Simulation map and resource ledger

1. source machine.
2. molecular encoding.
3. simulated transition.

### DNAD-19 — Toehold-mediated strand displacement

**DNAD-19-F1 — Six molecular keyframes**. Six molecular keyframes

1. gate.
2. encounter.
3. binding.
4. migration.
5. displacement.
6. release.

### DNAD-20 — Chemical reaction networks as programs

**DNAD-20-F1 — Reaction graph and stoichiometric matrix**. Reaction graph and stoichiometric matrix

1. reaction specification.
2. rate equations.
3. DNA realization.

### DNAD-21 — Digital and analog DNA circuits

**DNAD-21-F1 — Gate cascade with concentration traces**. Gate cascade with concentration traces

1. input concentrations.
2. gate reaction.
3. restored output.

### DNAD-22 — Self-assembly, tiles and geometry

**DNAD-22-F1 — Tiles, glues and molecular scaffold zoom**. Tiles, glues and molecular scaffold zoom

1. seed.
2. legal attachment.
3. growing assembly.

### DNAD-23 — Noise, crosstalk and fault models

**DNAD-23-F1 — Fault propagation across layers**. Fault propagation across layers

1. local fault.
2. propagated effect.
3. observed error.

### DNAD-24 — Scaling and resource limits

**DNAD-24-F1 — Resource budget and Pareto frontier**. Resource budget and Pareto frontier

1. design size.
2. resource demand.
3. feasible regime.

### DNAD-25 — Synthesis, sequencing and DNA storage

**DNAD-25-F1 — Write–store–read channel**. Write–store–read channel

1. encoding.
2. synthesis/storage.
3. noisy readout.
4. decoding.

### DNAD-26 — Laboratory workflows and reproducibility

**DNAD-26-F1 — Sample lineage and instrument workflow**. Sample lineage and instrument workflow

1. design.
2. prepare.
3. react.
4. separate.
5. measure.
6. interpret.

### DNAD-27 — Symbolic molecular simulation

**DNAD-27-F1 — Interpreter state and transitions**. Interpreter state and transitions

1. model.
2. interpreter step.
3. trace.
4. oracle comparison.

### DNAD-28 — Kinetic and stochastic simulation

**DNAD-28-F1 — Reaction trace and simulation comparison**. Reaction trace and simulation comparison

1. parameters.
2. simulation.
3. measured discrepancy.

### DNAD-29 — Differentiable molecular and sequence models

**DNAD-29-F1 — Forward model and gradient path**. Forward model and gradient path

1. design parameters.
2. prediction.
3. loss.
4. update.

### DNAD-30 — Genomic organization, regulation and development

**DNAD-30-F1 — Genome–expression–phenotype zoom**. Genome–expression–phenotype zoom

1. stored sequence.
2. cellular regulation.
3. expression.
4. phenotype.

### DNAD-31 — Modern molecular programming and evidence

**DNAD-31-F1 — Historical mechanism map and evidence comparison**. Historical mechanism map and evidence comparison

1. research claim.
2. mechanism.
3. experiment.
4. bounded conclusion.

### DNAD-32 — From molecular computation to genomic computation

**DNAD-32-F1 — Four-layer bridge**. Four-layer bridge

1. molecule.
2. formal model.
3. digital implementation.
4. research hypothesis.
