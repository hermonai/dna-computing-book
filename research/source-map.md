# Source map

Snapshot date: 2026-09-04. Local paths identify research inputs only; source binaries are not copied into this repository.

## Primary supplied sources

| Source | Local identity | Use | Caveat |
| --- | --- | --- | --- |
| *DNA Computing Foundations: From Molecular Information to Learning Systems* | `/Users/wenyan/ClaudeProjects/dna2agi/DNAComputingFoundations.pdf`, 170 pages, first edition v1.0, July 2026 | prior pedagogical structure, bibliography leads, existing explanations to audit | author-created source, not the external Kari/Seki/Sosik work named in the prompt; claims require primary-paper verification |
| *Evolutor: A Theory of Genomic Computation* v1.4.1 | `/Users/wenyan/Evolutor/Paper/Evolutor - A Theory of Genomic Computation v1.4.1.tex` and `.pdf`, 17 pages | downstream GCS bridge, formal vocabulary, theorem audit handoff | source-derived theory, not established DNA-computing science |
| *Evolutor: A Theory of Genomic Computation* v1.7.0 | `/Users/wenyan/Evolutor/Paper/Evolutor - A Theory of Genomic Computation v1.7.0.tex` and `.pdf` | later revision awareness | do not silently substitute it for v1.4.1; changed proofs and caveats need a versioned comparison |
| DOGMA engine architecture | `/Users/wenyan/ClaudeProjects/dogma/docs/ARCHITECTURE.md` | historical/current recurrent engine facts | repository has an unborn `main` branch; no commit identity available |
| DOGMA two-book generation prompt | `/Users/wenyan/ClaudeProjects/dogma/docs/BOOK_GENERATION_SYSTEM_PROMPT.md` | measured-result discipline and correction record | describes DOGMA as recurrent/non-transformer, conflicting with proposed target naming |
| DOGMA audit errata | `/Users/wenyan/Evolutor/Paper/DOGMA_AUDIT_ERRATA_2026-08-02.md` | invalidated-claim inventory and corrected evidence policy | supersedes older empirical and universality claims in neighboring DOGMA papers |

The separately named work *DNA Computing: Foundations and Implications* by Lila Kari, Shinnosuke Seki, and Petr Sosik was not located as a distinct local file. `[RESEARCH NEEDED: obtain an authorized copy or exact bibliographic identifier before treating it as inspected.]`

## Related repositories inspected without modification

| Repository | Snapshot | Working state | Relevance |
| --- | --- | --- | --- |
| `/Users/wenyan/ClaudeProjects/dna2agi` | `49e6fa790a6faaa2b470881f058fdf8fcd69e1ab` | branch `paper/capacity-is-all-you-measured`, 50 changed paths | prior textbook, correction paper, web edition |
| `/Users/wenyan/ClaudeProjects/evo-trainer` | `610117f0c6f73eed12d7bfba1478696512fb52c2` | branch `fix/dogma-causality`, 59 changed paths | training, causality, evaluation, correction artifacts |
| `/Users/wenyan/ClaudeProjects/hermon` | `472a44cdb511b2dae6c9569e59543db8f8350b25` | branch `main`, 1 changed path | transformer-oriented inference runtime and paged KV machinery |
| `/Users/wenyan/ClaudeProjects/dogma` | no commit (unborn `main`) | 9 changed paths | recurrent-state inference engine and book prompt |
| `/Users/wenyan/Evolutor/evolutor` | no commit (unborn `main`) | 16 untracked roots | earlier GCS runtime/book scaffold; remote credential hygiene issue observed and left untouched |

No claim in this book should use an uncommitted working tree as immutable evidence. Hash individual source files or create a reviewed source snapshot when a claim depends on them.

## Primary external literature verified during bootstrap

- Leonard M. Adleman, “Molecular Computation of Solutions to Combinatorial Problems,” *Science* 266 (1994), DOI [10.1126/science.7973651](https://doi.org/10.1126/science.7973651).
- Richard J. Lipton, “DNA Solution of Hard Computational Problems,” *Science* 268 (1995), pp. 542-545. `[RESEARCH NEEDED: verify DOI from the publisher record.]`
- Erik Winfree, *Algorithmic Self-Assembly of DNA*, Caltech PhD thesis (1998), DOI [10.7907/HBBV-PF79](https://doi.org/10.7907/HBBV-PF79).
- Bernard Yurke et al., “A DNA-fuelled Molecular Machine Made of DNA,” *Nature* 406 (2000), DOI [10.1038/35020524](https://doi.org/10.1038/35020524).
- Georg Seelig et al., “Enzyme-Free Nucleic Acid Logic Circuits,” *Science* 314 (2006), DOI [10.1126/science.1132493](https://doi.org/10.1126/science.1132493).
- David Soloveichik, Georg Seelig, and Erik Winfree, “DNA as a Universal Substrate for Chemical Kinetics,” *PNAS* 107 (2010), DOI [10.1073/pnas.0909380107](https://doi.org/10.1073/pnas.0909380107).

## Source-use rules

1. The existing textbook is a source map, not an authority.
2. The Evolutor papers inform the bridge only after established DNA computing is presented.
3. Quantitative physical claims require primary experimental literature and declared conditions.
4. Architecture measurements require an immutable script/artifact/checkpoint identity.
5. Missing evidence is recorded as a research task, not repaired with plausible prose.

