# Canonical deep Chapter 1 production report

Date: 7 September 2026. Status: internally reviewed development prototype, not a completed book or independent scientific endorsement.

## Release identity

- Repository: hermonai/dna-computing-book; verified public.
- Branch: `astra-deep-rewrite`; no merge into main.
- Starting commit: `a95da1f6d7d00bdf66d479a763e371597e0e8001`.
- Final release commit: the commit introducing this report; resolve with `git log --diff-filter=A --format=%H -- DEEP_CHAPTER_1_REPORT.md`. Its actual hash and remote verification are reported in the delivery message, avoiding a self-referential commit hash.
- Chapter: [Computing with DNA](tex/deep/ch01.tex).
- PDF: [canonical Chapter 1](output/pdf/deep-dna-computing.pdf), 20 physical pages: cover, about, contents; 14 chapter pages; glossary, bibliography and selective index.
- 13 sections, 10 exercises with worked solutions/discussion, 11 bibliography entries.
- The original eight-section planning outline remains preproduction history; production deliberately refines it without expanding into Chapter 2.

## Sections

1. Computation in matter
2. Adleman's experiment: the founding idea
3. The graph problem, precisely
4. From adjacency to oriented strands
5. A population is not an exhaustive search
6. Filtering: why the predicates fit together
7. Laboratory mechanisms and readable evidence
8. Parallelism and computational complexity
9. Combinatorics becomes a material budget
10. The executable logical companion
11. From one search to a field
12. Exercises
13. Worked solutions and discussion

## Original figures and static sequence

Ten editable SVG figures in [book/figures/deep](book/figures/deep), each with a semantic Unicode TXT companion in [book/diagrams/deep](book/diagrams/deep). No copied source artwork, raster figure, or ASCII box-art diagram is used. Figure IDs are DNAD-01-F1 through F10.

Figures teach specification/physical evidence, the directed graph, candidate counterexamples, antiparallel edge/splint encoding, multiplicity, nine selection stages, laboratory mechanisms/failures, synthetic readout, factorial scaling, and a non-sequential field map.

[Animation directory](animation/dnad-01) contains 9 original editable static keyframes plus a state ledger and storyboard. Each frame identifies changed, unchanged and created/consumed information; a concrete state panel changes alongside the focus highlight. These are not exported moving animations or experimental recordings.

## Executable work and mathematics

[Plain Python companion](examples/deep/ch01.py), runnable as `python3 examples/deep/ch01.py`, and [generated results](artifacts/deep/ch01-results.json). Printed excerpts are generated references to actual source lines, not separately maintained code.

The original six-vertex, nine-edge graph has two witnesses, ABCDEF and ACBDEF. Bounded legal-walk generation and filtering produce 106 → 14 → 4 → 2 → 2 candidates. An injected illegal-edge pseudo-path survives length and coverage but fails independent verification. A separate permutation oracle checks survivors; all 64 loop-free directed graphs on three vertices are tested against it. Multiplicity, invalid routes and bounds, sampling domains and 256 reverse-complement four-mers are covered.

Formal work: directed-walk/Hamiltonian predicates; proof that length plus complete coverage implies distinctness but not adjacency; oriented half-domain encoding and endpoint length; multiset support; conditional retention; O(n) witness verification under stated lookup assumptions; (n−2)! fixed-endpoint orders; independent-sampling miss bound and ceiling (109 draws for one designated order, 53 for either witness in the hypothetical six-vertex uniform space); cV N_A molecule accounting.

## Source and scientific review

[Source-by-source access ledger](research/deep-ch01-sources.md) distinguishes read portions and permitted scope. All 11 citation keys resolve; no long quotations, imported benchmarks or historical figure reproductions.

Primary Adleman history is separated from the new teaching instance: seven historical vertices, 20-nucleotide codes, complementary splints, endpoint PCR, 140-bp length selection, affinity selection and graduated-PCR evidence. The chapter does not call that readout modern sequencing. Pairing is distinguished from covalent ligation. A mixed readout does not assign every band to one molecule. Physical absence is not automatically a mathematical proof of nonexistence. Modern automata, reaction networks, circuits and assembly are narrow sourced anchors, not a complete survey.

Scientific, mathematical, clarity, citation and visual review were conducted by the authoring agent. They are not independent expert approval or demonstrated reader learning.

## Visual and build review

Every physical page (1–20) was rendered and inspected in color; all 9 static frames were inspected. Representative mechanism/memory pages were also checked in grayscale. The PDF skill's rendered-page review led to concrete fixes: readable code sizing, unbroken comparison-table heading/rows, a non-wrapping KV label, covalent connections in the strand figure, explicit UML guards/dependency directions, and stateful frame panels. No clipped text, missing glyphs, unresolved references, overfull or underfull boxes remain in the final checked build.

[Source-hashed review record](artifacts/deep/ch01-review.json) binds acceptance to manuscript, apparatus, executable source, generated results, storyboard, SVG/TXT and frames. Tests reject stale source, missing manifests and an unreviewed figure. Coordinate rounding makes original SVG generation stable across the two local Python runtimes.

Verification commands:

```sh
make pdf PYTHON=/Users/wenyan/.pyenv/versions/3.13.6/bin/python3
/Users/wenyan/.pyenv/versions/3.13.6/bin/python3 -m pytest -ra
make review-pdf PYTHON=/Users/wenyan/.pyenv/versions/3.13.6/bin/python3
```

Final full-suite acceptance: 133 tests passed, including PDF compilation, citation closure, generated-asset freshness, invalid-plan rejection, exact examples and historical byte-preservation. The machine-specific Python path records the tested environment; a compatible Python with repository test dependencies may be used elsewhere.

## Preservation and consistency

The undergraduate branch is frozen and was not checked out, advanced or synchronized. Its preserved source/artwork/examples and all previously committed PDFs are byte-identical. Main, astra-rewrite and archive/pre-reboot-20260905 retain their original tips:

| Ref | Preserved commit |
| --- | --- |
| astra-undergraduate-rewrite | 0779ed552b26d678e2443c0d94177faa04dc293c |
| main | fd41e8c360d8d8698bcf8bfc90bef4314b2dd384 |
| astra-rewrite | a1fb9a6154976f903b39d0f8a26834a8336f2264 |
| archive/pre-reboot-20260905 | 3e10fc84bd81e733351da539e28b729eb1f007cf |

Both repositories carry identical Book I dependency contracts. DNAD-01 is prototype-available; later dependencies remain planned, not already taught. The 32/52 chapter architectures are preserved.

DOGMA is the non-Transformer DNA-native model and non-Transformer engine line. Hermon DNA is the Transformer-based DNA model and Transformer engine line. Evolutor is the broader theory, research, compiler/runtime and orchestration framework above both. Physical DNA computation, genomic sequence modeling and biologically inspired digital computation remain distinct.

## Limits and next chapter

Independent specialist and real-reader review remain open. No wet-lab validation, calibrated kinetic simulator, trained DNA-native model, optimized production engine, measured comparative advantage or AGI capability is delivered. Sources and index are selective. Semantic TXT helps access but the PDF is not tagged or certified PDF/UA. More lifelike chemical illustrations and moving animations remain possible future improvements, not delivered assets.

Next: DNAD-02, **Adleman's experiment: a mechanistic reconstruction**. Deepen historical oligos/operations, tube-state accounting, physical loss and incomplete coverage, controls and graduated-PCR interpretation. Reconstruct only what the primary record supports.

No Chapter 2 manuscript was authored in this milestone. [CHAPTER_STANDARD.md](CHAPTER_STANDARD.md) records the production lessons; [canonical strategy](CANONICAL_EDITION_STRATEGY.md) freezes parallel undergraduate development.
