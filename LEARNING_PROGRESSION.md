# DNA Computing: deep technical edition

Status: canonical deep Chapters 1–2 are internally reviewed development manuscripts; Chapter 3 onward remains planned. Prior editions and the Chapter 1-only PDF are preserved. No new wet-lab result, trained model or engine benchmark is delivered. See [Chapter 2 production report](DEEP_CHAPTER_2_REPORT.md).

DOGMA = non-Transformer DNA-native model + DOGMA Engine; Hermon DNA = Transformer-based DNA model + Hermon DNA Engine; Evolutor = broader genomic computation theory, research and eventual runtime above both.

## Mathematics, implementation and evidence

Motivate the problem → explain the mechanism → define the abstraction → derive → interpret → work an example → implement → test → examine limits. This is a reasoning discipline, not a rigid chapter template. Basic programming is assumed; library-specific and domain-specific semantics are taught. Proofs, differential equations and formal systems are welcome.

### DNAD-01

Define G=(V,E), specified endpoints and a permutation witness; distinguish formal acceptance from physical recovery.

Verify a nontrivial directed path and identify a filter-surviving invalid candidate.

### DNAD-02

Derive ideal filter soundness and list physical completeness assumptions without inventing historical measurements.

Reconstruct each operation from the primary paper; simulate filter losses and missing witnesses.

### DNAD-03

Distinguish decision from search; prove a verifier bound and explain NP-completeness without claiming P differs from NP.

Build an exhaustive oracle and a polynomial witness checker; compare search and verification counts.

### DNAD-04

Derive miss probability (1-p)^M under declared independent sampling; separate factorial candidate space from physical yield.

Estimate a declared sampling budget and sensitivity to bias; do not assume uniform generation.

### DNAD-05

Map an oriented molecular diagram to strings without treating symbolic complementarity as binding prediction.

Implement reverse complement and test orientation, ambiguity and involution.

### DNAD-06

Derive equilibrium occupancy from a stated binding model with units and standard-state conventions.

Compare symbolic matches with parameterized free-energy predictions; record parameter provenance.

### DNAD-07

Derive rate equations from reaction stoichiometry; separate deterministic concentration from molecule counts.

Simulate association; check conservation, units and stochastic versus deterministic limits.

### DNAD-08

Give typed input/output abstractions and chemical preconditions; distinguish catalysis from information creation.

Trace ligation and restriction cases including incompatible ends and incomplete reactions.

### DNAD-09

Derive N_k=N_0(1+e)^k for constant efficiency and explain plateau and selection bias.

Compute amplification with variable efficiency and adversarial primer placement.

### DNAD-10

Model retention and detection separately; distinguish evidence of presence from evidence of absence.

Interpret a synthetic gel with declared uncertainty and design positive/negative controls.

### DNAD-11

Formulate design constraints and demonstrate why pairwise sequence distance is insufficient.

Construct an encoding and test orientation, off-target overlaps and hairpin risks.

### DNAD-12

Prove an ideal filtering invariant; extend it with stage-specific false-positive and false-negative events.

Compare a symbolic filter simulator with an independent graph oracle.

### DNAD-13

Derive how a clause predicate acts on assignment encodings and account for exponential material.

Implement a small SAT oracle and molecular abstraction; expose unsound or incomplete filters.

### DNAD-14

Specify a chosen sticker-model variant and its allowed operations before any power claim.

Execute a small register program and count operations, species and memory.

### DNAD-15

Define rule application precisely; separate formal closure results from realizable enzyme operations.

Write a bounded rewrite enumerator and verify hand-derived reachable strings.

### DNAD-16

Develop formal definitions and a recognition example before molecular implementations.

Build a finite-state recognizer and map its transitions to a proposed molecular scheme.

### DNAD-17

Distinguish mathematical automaton variants and finite experimental implementations.

Trace acceptance on paired inputs; audit what the biochemical experiment actually implements.

### DNAD-18

State model assumptions and sketch a valid simulation proof; no finite experiment proves unbounded universality.

Critique a universality argument by finding missing resources or illegal operations.

### DNAD-19

Introduce domain notation, conservation and kinetic abstractions after oriented strand frames.

Simulate a gate with explicit fuel and waste; test leak pathways.

### DNAD-20

Derive deterministic and stochastic semantics, then explain DNA implementation assumptions.

Implement a small CRN with independent conservation and nonnegativity checks.

### DNAD-21

Derive signal conventions and explain when isolated gate behavior fails under composition.

Compare a truth table with concentration trajectories and resource depletion.

### DNAD-22

Define tile attachment threshold and legal assembly; separate geometry, addressability and computation.

Enumerate a small tile assembly and test illegal attachments and alternative growth orders.

### DNAD-23

Compose error channels only under justified dependence assumptions.

Inject correlated faults into a filter or circuit model; quantify robust and fragile regimes.

### DNAD-24

Build a multidimensional cost model with declared system boundaries.

Compare two algorithms at matched success probability, not only reaction-step count.

### DNAD-25

Derive a toy coding overhead and error model without conflating stored bits with executed operations.

Recover a synthetic message under insertion/deletion/substitution errors.

### DNAD-26

Connect operational checklists to statistical inference and measurement uncertainty.

Design a documented non-operational experiment plan with controls and failure interpretation.

### DNAD-27

Specify interpreter semantics and prove a small invariant before optimization.

Build a tested symbolic core shared by graph filters and rewriting systems.

### DNAD-28

Derive event propensities and discuss stiffness, identifiability and approximation error.

Compare deterministic and stochastic trajectories under reproducible seeds and fitted uncertainty.

### DNAD-29

Derive a simple differentiable objective and distinguish surrogate accuracy from physical validation.

Use NumPy or PyTorch only where gradients or tensors serve the model; check finite differences.

### DNAD-30

Separate molecular mechanisms, dynamical state, parameter change and population evolution.

Analyze a small regulatory model and identify what it omits about a living system.

### DNAD-31

Reconstruct selected primary results with assumptions, controls, resources and uncertainty.

Produce a reproducible evidence comparison; refresh literature at drafting time.

### DNAD-32

Define cross-layer mappings and identify which properties survive abstraction.

Complete the Book II handoff by formalizing one mechanism and rejecting an unsupported analogy.
