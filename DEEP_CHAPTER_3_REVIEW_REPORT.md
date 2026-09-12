# Chapter 3 review and scientific-architecture checkpoint

12 September 2026. Author review, not independent acceptance.

## Delivered chapter

Combinatorial search and complexity: 4453 whitespace-delimited manuscript words,
12 original editable SVG figures with semantic TXT companions, 12 worked exercises,
a glossary, tested boundary diagnostics and a source ledger. The standalone
review PDF has 18 pages, including its contents and appendices.

The PDF skill's render-and-inspect workflow informed the final layout: a separate
contents page, captions kept with figures, legible vector labels and checked page
boundaries. Every page was inspected in contact sheets; the eight new figures
across both books were also inspected at their native rasterized size.
A grayscale sample covers the new mechanism figures. No independent
biologist, mathematician or reader approval is implied.

PDF SHA-256: fed98c7991743f0245c8c0d171468922156681f28c90322c038a95e886bc0e09

Machine-readable provenance: [Chapter 3 review record](artifacts/deep/ch03-review.json).
Reproduction: [Chapter 3 README](drafts/ch03/README.md).

## Requested architecture report

| No. | Field | Finding |
| --- | --- | --- |
| 1 | Starting commit | bdbd289b57037ca39d582178ef9c58c38554cb95 |
| 2 | Branch | astra-deep-rewrite |
| 3 | Repository status | Clean at architecture-pass entry. This checkpoint changes only bounded research/Chapter 3 assets and their checks; generated PDF/render output is gitignored. |
| 4 | Completed chapters preserved | Accepted Chapters 1-2, canonical chapter count, review manifest and published PDF bytes are unchanged. No new acceptance hashes substitute for earlier review. |
| 5 | Scientific sources inspected | MIT Sipser complexity lectures; MIT 6.046J cycle/path construction; Toronto coNP notes. CRN and modern molecular-programming access limits are recorded in the research ledger. Cook/Karp were located, not fully re-proved from primary papers. |
| 6 | Current strengths | Representation-aware complexity, explicit quantifiers, independently enumerated small instances, both reduction directions and separation of symbolic state from physical population. |
| 7 | Missing scientific domains | Detailed chemistry, thermodynamics, kinetic and stochastic mechanisms, assay calibration, strand displacement and modern CRNs are mapped to later chapters; not supplied by the graph model. |
| 8 | Missing mathematical foundations | The complete upstream NP-hardness chain is an imported premise, not newly established here. Deeper physical cost and error models remain later work. |
| 9 | Missing computational foundations | Physical representation maps, yield-aware and kinetic simulators must follow the current symbolic references. |
| 10 | Missing experimental foundations | Measured survival/detection probabilities, correlated failures, controls and calibrated material/time/readout accounting. |
| 11 | Visual weaknesses addressed | Replaced the four remaining storyboard-only entries with original SVG/TXT pairs. Protein occupancy, antiparallel DNA and population cartoons are distinct from algorithmic boxes. These are pedagogical schematics, not atomistic models. Chapter-wide specialist review is still required. |
| 12 | Recommended Parts | Retain seven: origins; molecular foundations; encoding/algorithms; formal computation; molecular programming; engineering/evidence; executable models/research. |
| 13 | Recommended chapters | Retain the 32-chapter curriculum with mechanism/evidence gates; no expansion solely for apparent depth. |
| 14 | Chapters retained | All canonical chapter IDs and prerequisite ordering are retained. Chapters 1-2 remain accepted; Chapter 3 is a review candidate. |
| 15 | Chapters deepened | Chapter 3 now adds work/depth bounds, conditional missing-signal accounting, proof boundaries and physical-state interpretation. Later deepen-in-place entries remain plans. |
| 16 | Chapters moved | None. |
| 17 | Chapters split or merged | None. |
| 18 | New chapters | None beyond continuing the already-started Chapter 3. No Chapter 4 manuscript was generated. |
| 19 | Dependency DAG | docs/scientific-dependencies.json and .txt retain the canonical ordered acyclic graph. Cross-book imports remain explicit in the chapter map. |
| 20 | Master architecture | docs/DEEP_SCIENTIFIC_BOOK_ARCHITECTURE.md and research/figures/scientific-master.svg/.txt; not a replacement acceptance manifest. |
| 21 | Animation plan | docs/SCIENTIFIC_VISUAL_MAP.md preserves chapter keyframe plans. New mechanism assets are static editable vectors; no completed video or new animation sequence is claimed. |
| 22 | Executable progression | Sequence/graph/filter models → verified search and reductions → resource/sampling accounting → physically parameterized kinetic and molecular-programming models. |
| 23 | Source/research map | research/scientific-recalibration-sources.md, domain-specific research maps and drafts/ch03/sources.md. Access-depth limits are explicit; preserved maps remain under research/pre-recalibration/. |
| 24 | Checks passed | Final validation counts are recorded below. All 12 chapter SVGs plus the master map passed browser text-bound checks; the PDF has no extracted words outside page boundaries or missing-character build warnings. |
| 25 | Commits | Architecture: 033d704. Chapter work: the bounded feat(book) commit containing this report. |
| 26 | Push status | Not pushed. No remote publication or repository settings changed. |
| 27 | Exact next bounded chapter | First close Chapter 3 independent/cumulative acceptance gates. Then DNAD-04: Molecular parallelism and resource accounting, with calibrated-versus-toy quantities kept separate. |

## Validation and limitations

Final regression result: 229 passed, 2 skipped (Evolutor-only PyTorch controls), in 93.68 seconds.
Scientific architecture/figure regeneration checks and git whitespace checks passed.

The initial shell selected Python 3.9 without PyTorch; validation was rerun using
Python 3.13.6 with PyTorch 2.10.0. A later preservation test caught the review PDF
changing while its renderer and the regression suite ran concurrently. No
preservation assertion was weakened; final validation runs after all PDF writes.
The accepted Chapter 1-2 manifest and published release remain unchanged.

Scientific acceptance is still open: independent review, cumulative source
integration, consistent final figure numbering, bibliography and index must be
completed before promoting the chapter. The source ledger preserves earlier
pass notes and marks what the current extension supersedes. No new wet-lab
result, trained genomic model, specialized engine, speedup or novelty claim is made.
