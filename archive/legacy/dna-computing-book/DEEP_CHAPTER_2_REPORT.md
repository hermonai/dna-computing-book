# Deep Chapter 2 production report

Review date: 9 September 2026. Scope: author-agent-reviewed development manuscript, not an independently certified edition.

## Release surface

- Starting commit: `6046afc3b1ef1bee59b11176a65a3e73778c125f`; branch: `astra-deep-rewrite`.
- Chapter: **Adleman's experiment: from graph to molecules**, [source](tex/deep/ch02.tex).
- 19 sections; 18 body pages (printed 15–32, physical 19–36).
- [Cumulative Chapters 1–2 PDF](output/pdf/deep-dna-computing-ch01-02.pdf): 40 pages including front matter, glossaries, bibliography and index.
- 14 original editable SVG figures, 14 semantic TXT companions, nine static keyframes (assembly, PCR, affinity selection). These are not exported moving media.
- Twelve exercises and twelve worked solutions; 12 distinct sources cited in Chapter 2, 15 entries in the cumulative bibliography.
- [Storyboard](pedagogy/deep-ch02-storyboard.json), [source-access ledger](research/deep-ch02-sources.md), [executable companion](examples/deep/ch02.py), [computed results](artifacts/deep/ch02-results.json).

## Scientific and skeptical review

The original Adleman paper was read beyond its abstract, including the graph, sequence illustration and experimental notes. The chapter reconstructs seven vertices, fourteen directed edges, endpoints 0 and 6 and the unique witness 0,1,2,3,4,5,6. Only the three published vertex codes are printed; absent codes are not invented. Internal edge strands are R_i L_j, aligned by complementary vertex splints. Terminal completion supplies the full 140-base path; the splint does not insert another code into the product.

The review separates annealing from covalent ligation, primer orientation from perfect PCR specificity, molecule length from vertex identity, and the two roles of streptavidin beads. Preparation recovers a free strand, capture retains a probe-bound target through washing, and release recovers the target into solution. Graduated PCR is a length/position projection, not modern sequence readout; a mixed sample can lose joint route identity.

The algorithmic account preserves multiplicity. All bounded legal walks produce 1,583 candidates, followed by stage counts 9, 2 and 1 after the first presence filter; the witness survives the remaining checks. An independent permutation oracle and deliberately illegal pseudo-paths expose the separate adjacency requirement. More copies cannot repair a missing graph edge.

Mathematics covers Hamiltonian predicates, a multiset decoding/selection relation, soundness versus completeness, readout projection, conditional survival and resource accounting. With three true copies, retention 0.8 and five stages, the probability of losing every true copy is about 0.304 under independent-copy survival; expectations alone need no cross-copy independence. The factorial illustration explicitly assumes fixed endpoints in a complete directed graph. Historical oligo inventory is not a count of completed routes. Seven days is reported workflow time, not evidence of an efficient NP-complete solver.

## Publication review

All 40 cumulative pages were rendered and visually inspected. Changed pages were re-rendered after correcting splint-domain alignment, PCR label placement and code pagination. Whole tested functions replace fragile line-range listings. Captions, equations, tables, glossary, bibliography and index were checked; all nine Chapter 2 frames and representative grayscale pages were inspected. No clipping, overlapping labels, unresolved references or layout warnings remain in the reviewed build.

The source-bound [acceptance record](artifacts/deep/ch02-review.json) covers cumulative manuscript inputs and generated evidence. The preserved Chapter 1 source, apparatus, review and all existing PDF bytes are checked against the starting commit; the cumulative edition has a new entry point and filename.

## Verification

Full repository run: **178 passed**, zero failures or skips, using Python 3.13.6. This includes 44 dedicated Chapter 2 tests and a healthy-copy control for the cumulative review gate. Existing tests remain enabled; milestone assertions now accept exactly Chapters 1–2 and still reject Chapter 3.

`make pdf` passes the source-bound acceptance gate, both chapter artifact freshness checks and LaTeX log validation. The full suite includes generated-plan freshness, citation/asset closure, independent expected results and preservation checks. No errors, missing glyphs, undefined references or overfull boxes were reported.

## Limits and next dependency

No laboratory replication, measured yield, thermodynamic simulation or new complexity result is claimed. Figures are original explanatory reconstructions, not reproductions of experimental photographs. The reference code has finite walk bounds and no reaction kinetics. The later-history source coverage is selective, with access depth disclosed.

Review was performed by the authoring agent, not independent historians, chemists or readers. Independent subject review, reader testing and accessible tagged publication remain open; the PDF is not certified PDF/UA.

The next planned chapter is **Combinatorial search and complexity**. It should develop reductions, verification and computational/physical resource distinctions before later thermodynamics and kinetics. No Chapter 3 source was implemented. Book II consistently distinguishes software processing of genomic strings from this book's physical molecular computation.
