# DNA Computing: deep technical edition

Status: architecture and detailed outlines only; no new manuscript, final figures, animation frames, models, engines or experiments are delivered. Canonical source: [deep curriculum](pedagogy/deep-curriculum.json). Prior editions remain historical references, not the active teaching level.

DOGMA = non-Transformer DNA-native model + DOGMA Engine; Hermon DNA = Transformer-based DNA model + Hermon DNA Engine; Evolutor = broader genomic computation theory, research and eventual runtime above both.

## Detailed Chapter 1 outline: Computing with DNA

Next execution writes this chapter; this milestone creates no manuscript, finished artwork or animation frames.

Let the argument determine length; a substantial 30–50-page treatment is acceptable, not a quota. The opening establishes the field and exact worked mechanisms without duplicating later full treatments.

### 1.1 The molecular-computation idea

Begin with Adleman's 1994 Hamiltonian-path demonstration, not elementary arithmetic. Explain instance, physical representation, operation and measured answer; distinguish a molecule, a formal string and a simulator.

**Formal depth:** Define an encoding map and a decoding relation only after the experimental sketch.

**Worked sequence:** Follow one candidate through problem → molecule → observation; mark which assertions are historical and which belong to our simplified teaching model.

**Visual:** DNAD-01-F1 — Adleman's core idea. Three aligned lanes: graph instance, molecular experiment, interpreted witness.

**Evidence gate:** Read relevant primary sources in full for the claims used; distinguish historical details, original teaching examples and research proposals.

### 1.2 A graph problem precise enough to compute

Introduce directed vertices and edges in a nontrivial original graph. Distinguish walk, simple path, Hamiltonian path and specified endpoints. Explain decision versus witness recovery.

**Formal depth:** G=(V,E); P=(v_1,...,v_n); every v_i in V, all distinct, every consecutive pair in E, with declared start/end. Verification can be polynomial without search being known polynomial.

**Worked sequence:** Check one valid route, one nonexistent edge and one repeated vertex. An independent enumeration must verify the chosen teaching graph before illustration.

**Visual:** DNAD-01-F2 — Hamiltonian path and counterexamples. One stable graph with three candidate overlays and a small search tree; edge direction is invariant.

**Evidence gate:** Read relevant primary sources in full for the claims used; distinguish historical details, original teaching examples and research proposals.

### 1.3 From graph edges to oriented DNA

Preview only the chemistry required: sequence identity, antiparallel matching, vertex oligos, overlapping edge encodings and covalent joining. Full chemistry follows in Part II.

**Formal depth:** Specify a symbolic encoding with oriented domains; distinguish complement from reverse complement. Do not transplant the historical oligo sequences without source verification.

**Worked sequence:** Work one edge bridge with 5′/3′ labels and a deliberately reversed incorrect bridge; explain what the symbolic match does not guarantee physically.

**Visual:** DNAD-01-F3 — Graph-to-DNA encoding. Graph above oriented molecular strands; zoom from edge to sequence domains; separate base pairing from backbone bonds.

**Evidence gate:** Read relevant primary sources in full for the claims used; distinguish historical details, original teaching examples and research proposals.

### 1.4 A candidate pool, not an exhaustive oracle

Explain annealing and ligation as probabilistic candidate generation. The mixture contains multiplicities and unwanted products; intended candidates may be absent.

**Formal depth:** Represent the pool as a multiset, not an automatically complete set. Define per-candidate sampling probability without assuming it is uniform.

**Worked sequence:** Trace several intended and unintended walks into a symbolic pool; keep multiplicity distinct from chemical concentration.

**Visual:** DNAD-01-F4 — Candidate molecular pool. Stable candidate identities with differing multiplicities; incomplete generation is visible.

**Evidence gate:** Read relevant primary sources in full for the claims used; distinguish historical details, original teaching examples and research proposals.

### 1.5 Generate, filter and verify

Explain endpoint, length and vertex-coverage predicates and the physical operations intended to implement them. Distinguish ideal predicate correctness from imperfect retention.

**Formal depth:** Prove: n vertex positions plus coverage of all n distinct vertices implies each appears exactly once; adjacency and endpoints are separate conditions.

**Worked sequence:** Carry one repeated-vertex candidate through the filter ledger until the coverage test rejects it; test a true witness lost by imperfect selection.

**Visual:** DNAD-01-F5 — Selection pipeline. Seven static keyframes; candidate identities remain stable; rejection is not creation.

**Evidence gate:** Read relevant primary sources in full for the claims used; distinguish historical details, original teaching examples and research proposals.

### 1.6 What the laboratory actually observes

Relate PCR, electrophoresis, affinity selection and readout to their computational roles. Verify the historical readout method from the paper; do not substitute modern sequencing into the historical narrative.

**Formal depth:** Separate molecule count, length, signal and sequence evidence; distinguish failed detection from proof of no solution.

**Worked sequence:** Read a clearly synthetic gel sketch with controls and uncertainty; label it as teaching data, not a replication.

**Visual:** DNAD-01-F6 — Operations, measurements and inference. Operation-to-predicate table paired with sample lineage and gel lanes.

**Evidence gate:** Read relevant primary sources in full for the claims used; distinguish historical details, original teaching examples and research proposals.

### 1.7 Parallelism and the resources it consumes

Introduce exponential combinatorial growth, NP and NP-completeness at a useful first level. No claim that P differs from NP or that molecular parallelism removes material costs.

**Formal depth:** Under independent draws, miss probability is (1-p)^M; derive required M for a specified tolerance. For fixed endpoints in a complete directed graph there are (n-2)! internal orders; this is not a universal yield model.

**Worked sequence:** Compare a declared uniform toy bound with biased sampling; include species, molecules, volume, reaction stages, loss and readout in the ledger.

**Visual:** DNAD-01-F7 — Scaling challenge. Analytical curves with axes, units and assumptions; a separate physical-resource ledger, no invented measurements.

**Evidence gate:** Read relevant primary sources in full for the claims used; distinguish historical details, original teaching examples and research proposals.

### 1.8 The field after the first experiment

Provide a mechanism-based map: combinatorial selection, molecular automata, reaction networks, strand displacement, circuits, self-assembly and simulation. Place storage and learned DNA models at distinct boundaries.

**Formal depth:** Summarize which abstraction each branch uses and what implementation evidence would support it; leave detailed universality proofs for Part IV.

**Worked sequence:** Compare two research claims by mechanism, resource and evidence rather than a chronology of names; include derivation/coding/experimental-design exercises.

**Visual:** DNAD-01-F8 — Mechanism and history map. Technical field map with source-linked milestones and cross-links to later chapters, not a universal progress arrow.

**Evidence gate:** Read relevant primary sources in full for the claims used; distinguish historical details, original teaching examples and research proposals.

## Executable example scope

Implement a symbolic graph/path checker and filter simulator with an independent exhaustive oracle. Include actual tested files, not elementary Python lessons. No wet-lab experiment or thermodynamic validity is implied.

## Exercises

Include a fully solved technical example, derivation, algorithm or proof task, implementation check, experimental/systems design task and research critique. Open problems get a rubric, not fabricated solutions.

## Acceptance

- Chapter starts with the actual subject, not counters or a thermostat.
- Definitions and abstraction boundaries are explicit; useful abstraction is not prohibited.
- Every displayed formula has defined symbols, assumptions and interpretation.
- Every figure has editable source and a Unicode TXT companion; scientific and final-page reviews remain required.
- No novelty, performance, biomedical or AGI conclusion without corresponding evidence.
