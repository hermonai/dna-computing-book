# Editorial architecture and release roadmap

Updated 25 September 2026. This is the current execution map, not a claim
that every planned chapter is written or independently reviewed.

## One manuscript, distinct review stages

Retain the 32-chapter spine in BOOK_PLAN.md. Its generated status describes
the frozen canonical acceptance snapshot; use this map and the root README
for current authoring progress. Do not regenerate archived editions merely
to change their progress labels.

Chapters 1-2 retain their internal acceptance records. Chapter 3 has standalone
and combined LaTeX review candidates. Chapters 4-16 have isolated authored-LaTeX
review candidates with code, vector figures, and worked solutions.
Chapter 17 is the next unwritten chapter. Chapters 11-16 were authored at the
reader's explicit request while the Chapters 1-10 integration milestone remains
pending. These standalone candidates do not substitute for that integration.
Independent specialist review and cumulative integration are still open.

## Give each return to a topic a new job

| Chapter group | Primary question and owned deliverable | What belongs later |
|---|---|---|
| 1-4: origins and resource accounting | What is computed, and where is its cost paid? Separate formal problem, molecule inventory, and measured evidence. | Detailed chemistry and numerical solvers |
| 5-7: molecular foundations | What can pair, what equilibrium is allowed, and how does a finite population get there? Sequence geometry, finite-pool thermodynamics, exact and stochastic binding references. | General reaction-network software and fitted rates |
| 8-10: operators and observations | How do enzymes transform substrates, amplification change populations, and instruments expose imperfect evidence? Substrate-to-product mechanisms with controls. | A complete universal laboratory protocol |
| 11-18: representation and formal models | Which encoding and permitted operations implement a computation? Explicit semantics, constructive examples, and limits. | Experimental feasibility inferred solely from universality |
| 19-22: engineered molecular systems | How do local strand, reaction, and assembly mechanisms compose? Interfaces, leakage paths, conservation, and composition failures. | General-purpose simulation infrastructure |
| 23-26: reliability and practice | What survives noise, scale, storage, and reproducibility demands? Error budgets and auditable experimental evidence. | Unmeasured industrial performance claims |
| 27-29: executable modeling | How do we build reusable symbolic, kinetic, and differentiable tools? Chapter 28 extends Chapter 7 to networks, solver diagnostics, stiffness, parameter inference, and uncertainty. | Re-teaching the same two-species derivation |
| 30-32: connection and synthesis | Where does molecular regulation inform computation, and where does the analogy fail? Research questions with falsifiable tests. | Treating Evolutor software states as literal molecules |

The prerequisite chain for the next milestone is sequence polarity (5),
binding free energy and mass balance (6), reaction rates and molecule-count
noise (7), then catalytic substrate transformation (8). Chapter 9 can then
explain amplification without confusing copying, equilibrium binding, and
computational search.

## Chapter 8 scope (standalone candidate): enzymes as molecular operators

Begin with one chemically explicit substrate-to-product transformation.
Show recognition, binding, catalytic action, product release, and a failure
or competing substrate. Label strand polarity and the bond or substrate
feature that changes. Separate enzyme specificity from perfect recognition.

Derive a minimal catalytic rate model and state its assumptions before
using it. Tie each computational operator to physical prerequisites and
what it cannot do. Provide executable inventory checks and a limiting-case
oracle; distinguish simulated behavior from measured enzyme activity.
Use original biology/biochemistry mechanism plates, not a generic flowchart
with biological names substituted into boxes.

## Chapter 9 scope (standalone candidate): amplification and copy-number evidence

Begin with one primer-extension event and track how two primers define an
amplifiable interval across repeated cycles. Separate strand count, duplex
count, and sequence-defined product count. Derive ideal doubling, then a
cycle-dependent efficiency model with finite resources and background.
Explain why amplification copies existing information and can magnify bias
or contamination without solving an arbitrary search problem.

Provide polarity-correct mechanism plates, explicit inventory checks,
limiting-case oracles, and an observation model that distinguishes threshold
crossing from absolute initial abundance. Assigned efficiencies must remain
separate from measured assay performance.

## Chapter 10 scope (standalone candidate): separation, readout, and measurement

Start with a mixture of target and off-target products, and ask which physical
property an instrument actually separates or measures. Explain electrophoretic
migration and fluorescence readout without treating band intensity as exact
molecule identity. Build an observation model with background, overlapping
species, calibration, and uncertainty. Provide controls and a counterexample
in which two distinct molecular mixtures produce the same observed signal.

## Chapter 11 scope (standalone candidate): sequence design and graph encoding

Derive reverse complements, offset complementarity, hairpin constraints and
code-distance bounds before constructing an injective graph encoding. Test
all short walks, deliberately expose a seam-created recognition site, and keep
combinatorial screening distinct from thermodynamic or laboratory validation.

## Chapter 12 scope (standalone candidate): generate-filter-verify algorithms

Build exact multiset filters and an independent witness verifier. Prove the
ideal algorithm's soundness and conditional completeness, then quantify loss,
false retention and finite-copy detection. Contrast commuting ideal predicates
with a capacity-limited order counterexample. Mechanism plates separate
molecular recognition from physical retention and evidence of identity.

## Chapter 13 scope (standalone candidate): SAT and combinatorial constructions

Build disjoint-residual clause selection with finite copy counts. Prove its
soundness and pool-relative completeness; compare against an independent
integer SAT oracle. Derive coverage and detection probability, expose the
duplicate-copy OR bug, and separate a positive certificate from no-signal
evidence. Compare the resource model cautiously with 2026 scaffolded computation.

## Chapter 14 scope (standalone candidate): sticker systems and molecular memory

Implement occupancy registers, count-preserving pushforward writes and
conditional AND with explicit output clearing. Test every initial register
and address permutation. Explain reset information loss, operation-level
retention and state-transition errors. Draw polarity-correct memory complexes
and distinguish abstract selective clear from demonstrated renewable computing.

## Chapter 15 scope (standalone candidate): splicing and insertion-deletion systems

Define contextual cuts and both recombinant products before implementing a finite-copy
reaction. Separate language closure from molecular inventory and bounded search.
Use polarity-correct ligation schematics to identify the chemical interface
without claiming a formal splice is an implemented laboratory operation.

## Chapter 16 scope (standalone candidate): languages, automata and molecular recognition

Construct and minimize an end-marked finite-state recognizer, then implement
a least-significant-bit-first addition transducer. Prove prefix invariants,
compare exhaustive arithmetic oracles and propagate an explicit error/loss
channel. Relate the formal interface to current scaffolded molecular computing
without substituting a probability model for measured chemistry.

## Pending milestone: integrate Chapters 1-10

Audit strand/count/concentration/signal notation, units, measurement assumptions,
source coverage, and prerequisites, including the interfaces now used by
Chapters 11-16. Preserve the distinction between a physical separation and a formal
predicate.
Build a new cumulative entry point with unified bibliography and index; retain
standalone candidates and accepted editions unchanged. Do not promote acceptance
without independent review and the existing release gates.

## Quality gates before widening the manuscript

1. Complete a locally reproducible chapter: explanations, derivations,
   source access notes, tested examples, worked exercises, and figure TXT
   companions. Numerical figure labels must agree with executable results.
2. Inspect every rendered page in color and grayscale. Check polarity,
   molecular inventory, arrow meaning, units, and captions separately from
   visual appearance. Hash the reviewed source set and PDF.
3. Request independent domain and reader review. Record disagreements and
   corrections; author-agent review does not satisfy this gate.
4. After Chapter 10, prepare a combined Chapters 1-10 integration candidate:
   audit notation, prerequisites, duplicate explanations, bibliography,
   cross-references, and index. Earlier specialist reviews may happen sooner.
5. Advance cumulative acceptance only after its existing gates pass.
   Standalone chapter completion must never silently promote the edition.

The implementation-first teaching pattern is predict, derive, implement,
check against an independent result, deliberately break an assumption,
then explain the boundary. Depth comes from these connections, not a fixed
page count or a fixed number of decorative figures.
