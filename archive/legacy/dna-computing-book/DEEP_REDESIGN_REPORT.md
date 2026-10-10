# Deep-redesign implementation report: DNA Computing

Date: 7 September 2026. Scope: planning-only technical reset. Branch: astra-deep-rewrite.
Starting commit: 0779ed552b26d678e2443c0d94177faa04dc293c.
Final local commit: the commit containing this report, retrievable with git log -1 --format=%H -- DEEP_REDESIGN_REPORT.md. No self-referential commit hash is embedded here.

## Outcome and audience

Full technical and scientific depth, explained straightforwardly. Useful abstraction is explicitly permitted and must be grounded, defined and interpreted. No university-level ceiling or prerequisite-free constraint remains. The audience is technically capable researchers and engineers entering an adjacent domain.

Entry assumptions: Basic programming and algorithmic reasoning; Algebra, functions, sets and discrete mathematical maturity; Basic probability, vectors, matrices and first-year calculus.

## Macro architecture

32 substantial chapters in 7 parts. Count is a consequence of grouped mechanisms and arguments, not a lecture quota.

- I · Origins and computational strategy: chapters 1–4.
- II · Molecular foundations and operators: chapters 5–10.
- III · Encoding and molecular algorithms: chapters 11–15.
- IV · Formal molecular computation: chapters 16–18.
- V · Molecular programming: chapters 19–22.
- VI · Engineering and evidence: chapters 23–26.
- VII · Executable models and modern research: chapters 27–32.

The [complete TOC](BOOK_PLAN.md), [dependency graph](PREREQUISITE_GRAPH.md) and [course map](COURSE_MAP.md) assign every chapter technical topics, mathematical development, implementation/assessment work and visual progression.

## Previous edition disposition

All 36 previous topic IDs are mapped in [PREVIOUS_EDITION_AUDIT.md](PREVIOUS_EDITION_AUDIT.md). Only the prior Chapter 1 was an actual manuscript; the other entries were plans. Preserve the old opening as a historical experiment and write a fresh deep opening next. No prose is automatically moved to a preface.

Counters, add_two and basic Python/symbol rehearsals no longer determine the active route. The new opening reaches the historical experiment, graph problem, molecular encoding, ideal filter correctness and physical scaling directly.

Earlier manuscripts, examples, diagrams, figures, PDFs and historical snapshots remain byte-identical. The old TeX manifest is retained for its historical entry point; active deep metadata has an empty chapter list and no main. Its PDF gate rejects attempts to relabel the preserved source as the deep edition.

## New Chapter 1

**Computing with DNA** — detailed outline only, not manuscript.

1. The molecular-computation idea.
2. A graph problem precise enough to compute.
3. From graph edges to oriented DNA.
4. A candidate pool, not an exhaustive oracle.
5. Generate, filter and verify.
6. What the laboratory actually observes.
7. Parallelism and the resources it consumes.
8. The field after the first experiment.

See [CHAPTER_1_OUTLINE.md](CHAPTER_1_OUTLINE.md) for mechanisms, defined formalism, worked examples, eight figure briefs, primary-source gates, exercises and executable-example scope. Later chapters provide full derivations and mechanisms rather than becoming prerequisites hidden inside the opening.

## Illustration and animation strategy

Retained: original editable scientific vectors, semantic Unicode TXT companions, correct molecular orientation and bond/interaction types, UML software diagrams, tensor shapes, memory ownership, timelines, readable labels, captions, grayscale and actual final-page review. Useful abstract figures remain welcome.

The deep inventories contain 39 primary visual briefs and 16 animation candidates, including the eight opening figures. Additional diagrams will be designed when each substantial chapter needs them; there is no one-figure quota. Animation inventory entries have frame actions and planned directories, not created frames or exported media. No final artwork or deep PDF is delivered in this milestone.

## Taxonomy and research boundaries

DOGMA = non-Transformer DNA-native model + DOGMA Engine.
Hermon DNA = Transformer-based DNA model + Hermon DNA Engine.
Evolutor = broader genomic computation theory, research and eventual runtime above both.

The plan separates candidate model semantics, reference training, parity, native engines and higher-level runtime. DOGMA is not a generic RNN rebranded, constant-total-memory promise or no-KV slogan. Hermon DNA retains Transformer/attention/KV semantics. No novelty, benchmark advantage, biomedical result or AGI capability is claimed.

The [source register](research/deep-source-register.md) records limited planning-stage access and full-paper work still required. It is not a completed literature review. Historical evidence ledgers and names are preserved.

## Validation

Final verification result: 88 passed in 19.72 seconds (Python 3.13.6, full pytest suite, including historical PDF integration). Deep generator freshness and compatibility-dispatch checks also pass. No new deep PDF or artwork is being delivered.

The new deep-edition tests check generated-document freshness, complete migration mappings, acyclic ordered dependencies, exact cross-book contracts, outline consistency, planned-only artifact status, two-family taxonomy, default-PDF refusal and byte-for-byte preservation. Negative cases deliberately reverse taxonomy and break prerequisites, math, figure status and migration destinations.

Existing computational and figure tests remain. Historical planning freshness is now checked against its immutable undergraduate Git snapshot rather than the new active root documents. The original Chapter 1 example/figure/citation tests remain, and the PDF integration test explicitly calls historical-pdf into build/; it does not replace the committed PDF. A repository manifest test was made edition-aware so it validates the preserved entry point while separately enforcing an empty active deep manifest.

Initial validation caught two transition issues: the old manifest test assumed one active edition, and README linked to this not-yet-written report. Both were addressed before final verification. No failed check is treated as a pass.

## Files changed

- ASTRA_REDESIGN.md
- BEGINNER_REVIEW.md
- BOOK_PLAN.md
- CHAPTER_02_REPORT.md
- CHAPTER_1_OUTLINE.md
- CHAPTER_REPORT.md
- CHAPTER_STANDARD.md
- CONCEPT_MAPS.md
- COURSE_MAP.md
- DEEP_REDESIGN.md
- DEEP_REDESIGN_REPORT.md
- FIGURE_SYSTEM.md
- LEARNING_PROGRESSION.md
- Makefile
- PEDAGOGICAL_REDESIGN.md
- PREREQUISITE_GRAPH.md
- PREVIOUS_EDITION_AUDIT.md
- PROFESSIONAL_REVIEW.md
- PUBLICATION_PLAN.md
- README.md
- REFERENCE_IMPLEMENTATION.md
- RESET_REPORT.md
- REVIEW_GATES.md
- ROADMAP.md
- TECHNICAL_LEVEL_RESET.md
- TERMINOLOGY_AUDIT.md
- VISUAL_STORYBOARD.md
- book/GRAPH_STANDARD.md
- book/book.json
- pedagogy/README.md
- pedagogy/deep-animation-inventory.json
- pedagogy/deep-book-i-contract.json
- pedagogy/deep-ch01-outline.json
- pedagogy/deep-curriculum.json
- pedagogy/deep-figure-inventory.json
- research/deep-source-register.md
- scripts/build_deep_plan.py
- scripts/build_pedagogy.py
- scripts/require_active_manuscript.py
- tests/test_deep_redesign.py
- tests/test_pedagogical_architecture.py
- tests/test_repository_contract.py
- tests/test_undergraduate_chapter01.py

## Remaining work and recommended next execution

The plans have internal structural and author-perspective review only, not independent scientific endorsement or actual reader testing. Primary-source reconstruction, prose, figures, code, experiments and deep PDF production remain future work.

Recommended next prompt:

> Implement only the new deep Chapter 1 of DNA Computing and Evolutor on astra-deep-rewrite, following DEEP_REDESIGN.md, CHAPTER_1_OUTLINE.md and CHAPTER_STANDARD.md. Preserve prior editions. Keep useful abstraction and derive it with straightforward explanations and meaningful worked examples. Audit primary sources, create original editable figures with semantic TXT companions, include tested source-linked code and technical exercises/solutions, and render/review every PDF page. Do not draft Chapter 2 or implement future DOGMA/Hermon engines. Report evidence, tests, limitations and exact artifacts; do not merge to main.

No future scope is automatically authorized by this report. New branches are local unless a separate publication action is explicitly reported.
