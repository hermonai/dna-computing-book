# DNA Computing: deep technical redesign

Date: 7 September 2026. Active branch: astra-deep-rewrite.
Starting commit: 0779ed552b26d678e2443c0d94177faa04dc293c.

DNA Computing is a deep reference textbook on how physical DNA becomes a computational medium: molecular biology and chemistry → algorithms and formal models → molecular programming → engineering evidence and simulation. Its readers include CS/AI engineers, chemists, computational biologists and researchers entering an adjacent field.

The 32-chapter structure consolidates the old 36 micro-units, but restores depth in thermodynamics, kinetics, formal languages, automata, universality, resource models, strand displacement, CRNs, circuits, self-assembly and simulation. Seven parts organize knowledge rather than prerequisites from zero. The earlier four graph/Adleman units become an opening technical overview plus a dedicated mechanistic reconstruction, with later encoding/algorithm chapters extending rather than repeating them.

Origins first is intentional: Chapter 1 supplies the graph and molecular vocabulary necessary for its worked example; Chapter 2 explains each historical operation locally. Part II then derives the chemistry in depth. These are explicit previews, not hidden forward prerequisites. Formal variants and full proofs follow after the opening.

Reading routes: follow all chapters for the full reference; algorithms readers can follow DNAD-01–04, 05–12 and the formal-model dependencies; molecular programmers emphasize 05–10 and 19–24 with their listed prerequisites; simulation readers use 27–29 after the named physical/formal models. The route is not a license to skip a prerequisite.

The new Chapter 1 is **Computing with DNA**. It starts with the experiment, gives a formal Hamiltonian-path problem and an oriented symbolic encoding, follows candidate generation/selection/readout, and derives a sampling/resource bound. It does not teach counting or elementary Python. Historical encoding and graduated-PCR readout were checked against Adleman's article; the original teaching graph uses symbolic domains, not unvalidated laboratory sequences.

## Permanent intellectual standard

Go as deep as the subject requires and explain each step directly. **Useful abstraction is welcome.** The user's clarification supersedes any “minimum abstraction” slogan in the amendments: remove unexplained abstraction, not abstraction itself. A formal definition, a proof, an operational semantics or an abstract machine may be the clearest explanation.

Assume a technically capable reader, not a particular degree level. Basic programming, algorithms, algebra, sets, elementary probability, vector/matrix notation and first-year calculus are entry knowledge. Teach domain-specific chemistry, biology, formal computation, ML and systems concepts before relying on them. Offer focused refreshers when needed; do not repeat counting, arithmetic or basic Python syntax as chapter content.

Use foundational → intermediate → advanced → engineering depth → research frontier as local signposts, not separate editions or ceilings. A chapter may cross all layers. Length follows the argument; 30–50 pages can be appropriate, but neither a minimum nor a quota.

## Explanation and abstraction discipline

1. State the problem and what must be explained.
2. Show the concrete mechanism or a precise worked case.
3. Name the abstraction, its domain/codomain and the map from the mechanism.
4. Define notation, units, shapes, state and assumptions before substantive use.
5. Derive the important steps; explain why each follows.
6. Interpret the result, implement it when useful, and test an independent case.
7. Zoom back out to consequences, failure modes and open questions.

This is flexible: an illuminating equation may precede a picture when both are explained. Do not force all subjects into one template. Do not replace a rigorous proof with a cartoon, or an accessible explanation with a list of equations. A technically mature reader should be able to reconstruct the reasoning.

Example of the standard: with independent sampling, missing a particular witness in one draw has probability 1-p. Missing it in M draws multiplies those probabilities, giving (1-p)^M. The abstraction is useful precisely because independence and p are visible assumptions; a real molecular pool need not satisfy either a uniform p or independent selection. The expression alone is not a physical prediction.

## Visual and mathematical depth

Retain original editable SVG/TikZ/Graphviz/PlantUML and semantic Unicode TXT companions; no crude ASCII box art. Figures explain structure and change; prose explains meaning; mathematics makes relationships exact; code executes the specified model. Use these together rather than interchangeable decoration.

Molecular figures show orientation, bonds, species, enzymes and conservation. Energy and kinetic plots show units and assumptions. Software uses UML or equally precise engineering notation; memory pictures show ownership and actual storage categories. Tensor diagrams show dimensions. Runtime diagrams show time, queues, cancellation and state lifetime. A diagram may be abstract, but its arrows and omissions must be explicit.

Chapter 1 now has original static keyframes with explicit state changes; later animation candidates remain storyboards, not delivered moving media. Before artwork, define before-state, changed/unchanged objects, movement, creation/consumption, stable identities and arrow semantics. Preserve static keyframes and reduced-motion alternatives. Render final figures inside the actual LaTeX pages before accepting them. No fixed number of figures per page or chapter overrides explanatory value.

## Code, evidence and research

Use Python for symbolic algorithms and simulation; NumPy for numerical work; PyTorch when differentiation or tensor models justify it. Do not introduce a custom training framework for branding. Reference semantics → exact small cases → independent oracle/parity checks → experiments → profiling → optimized code. Distinguish a tested symbolic simulator from a validated chemical model.

Research questions remain questions until mechanisms and experiments support them. Compare the nearest conventional baseline, matched capacity and full resource budgets; include ablations, causality checks, repeated seeds and failures where relevant. Hypotheses belong in the main argument, but repetitive methodological warnings should not displace the science. Put full claim provenance and source-access depth in research ledgers.

Primary-source review is required before drafting technical claims. Publication dates and “latest” claims must be checked then; this plan is not an exhaustive current literature survey. Preserve historical naming and commits. No architecture name alone proves novelty, speed, biological fidelity or AGI capability.

## Scope and production gate

The canonical Chapter 1 is now a fresh deep manuscript with ten original vectors, semantic TXT, static keyframes, exact code, exercises and a distinct reviewed PDF. The gate rejects old or changed-after-review source. No training run, physical experiment or inference engine is delivered. The undergraduate branch is frozen as a pedagogical archive.

Next execution: Chapter 2 under the existing source and dependency gates. Do not continue the undergraduate manuscript or old Chapter 2. The original eight-section outline is retained as preproduction history; the actual source and ten-figure production inventory supersede its asset count. All later chapters remain plans.

Internal structural and author-perspective review is not independent scientific certification or a real reader study. Release still needs subject review, actual technically capable readers, source/rights checks, reproducible evidence and accessibility work.

## Authoritative plan and preservation

[Macro TOC](BOOK_PLAN.md), [course map](COURSE_MAP.md), [dependency graph](PREREQUISITE_GRAPH.md), [Chapter 1 outline](CHAPTER_1_OUTLINE.md), [complete prior-topic disposition](PREVIOUS_EDITION_AUDIT.md), and [technical reset](TECHNICAL_LEVEL_RESET.md).

Active machine-readable sources are pedagogy/deep-curriculum.json, pedagogy/deep-book-i-contract.json and pedagogy/deep-ch01-outline.json. The unprefixed curriculum, contract, figure and animation inventories remain historical undergraduate data, not active inputs. scripts/build_deep_plan.py generates the active root documents and deep-prefixed inventories. scripts/build_pedagogy.py dispatches to the deep generator when the active edition is 4-deep; legacy functions remain regression-tested against the preserved Git snapshot.
