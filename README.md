# DNA Computing

The shared [About this book note](tex/frontmatter/about-this-book.tex) owns
the pedagogical acknowledgment and general evidence/review policy. It is
authored front matter for one-time inclusion in the next integrated edition;
chapter-specific assumptions and source notes remain in their chapters.

New authoring uses the [LaTeX-first Chapters 1–3 textbook candidate](tex/dna-computing-textbook.tex),
with a worked first-principles opening, native TikZ mechanisms and retained
reviewed vector figures. See [revision scope and build commands](TEXTBOOK_REVISION.md)
and the [shared textbook standard](TEXTBOOK_STANDARD.md). Run
`make -f textbook.mk textbook-check` then `make -f textbook.mk textbook`.
This is a new review candidate; the accepted Chapters 1–2 and their hashes remain frozen.

Canonical active edition: **astra-deep-rewrite**. Deep science and engineering, straightforward explanations, useful abstraction.

Chapters 1–2 are internally reviewed development manuscripts. Chapter 2 — **Adleman’s experiment: from graph to molecules** — adds 14 original editable SVG figures with semantic TXT companions, nine static keyframes, executable reference code and twelve exercises with worked solutions. The 32-chapter architecture remains; Chapter 3 has standalone and combined LaTeX review candidates. [Chapter 4: Molecular parallelism and resource accounting](drafts/ch04/README.md) is now an isolated authored-LaTeX review candidate with five vector plates, executable probability models, and twelve worked exercises. [Chapter 5: DNA chemistry and sequence geometry](drafts/ch05/README.md) adds five original mechanism plates, implementation-first derivations, tested code, and twelve worked exercises. [Chapter 6: Hybridization thermodynamics](drafts/ch06/README.md) adds five vector figures, tested numerical models, and twelve worked exercises. [Chapter 7: Reaction kinetics and stochastic chemistry](drafts/ch07/README.md) adds five mechanism figures, independent numerical checks, and twelve worked exercises. [Chapter 8: Enzymes as molecular operators](drafts/ch08/README.md) adds five biochemical/kinetic plates, substrate contracts, a tested catalytic model, and twelve worked exercises. [Chapter 9: Amplification and copy-number evidence](drafts/ch09/README.md) adds five molecular/counting figures, resource and sampling models, and twelve worked exercises. [Chapter 10: Separation, readout, and measurement](drafts/ch10/README.md) adds five mechanism/measurement figures, a tested inverse model with uncertainty and ambiguity checks, and twelve worked exercises. [Chapter 11: Sequence design and graph encoding](drafts/ch11/README.md) adds polarity-aware sequence checks, a tested graph code and five vector plates. [Chapter 12: Generate–filter–verify algorithms](drafts/ch12/README.md) adds exact multiset semantics, independent verification, finite-copy reliability and five vector plates. Each includes twelve worked exercises. Chapters 1–10 integration remains pending; cumulative acceptance has not advanced.

The [current editorial architecture](EDITORIAL_ARCHITECTURE.md) defines chapter responsibilities, prerequisites, evidence gates, and the next integration milestone. Use it for current authoring progress; generated historical plans retain their acceptance-snapshot status.

Read the [Chapters 1–2 PDF](output/pdf/deep-dna-computing-ch01-02.pdf), [Chapter 2 source](tex/deep/ch02.tex), [Chapter 2 production report](DEEP_CHAPTER_2_REPORT.md), [edition strategy](CANONICAL_EDITION_STRATEGY.md), [book plan](BOOK_PLAN.md) and [chapter standard](CHAPTER_STANDARD.md). The [Chapter 1-only PDF](output/pdf/deep-dna-computing.pdf) and [its production report](DEEP_CHAPTER_1_REPORT.md) are preserved unchanged.

DOGMA = non-Transformer DNA-native model + DOGMA Engine; Hermon DNA = Transformer-based DNA model + Hermon DNA Engine; Evolutor = broader theory/research/compiler/runtime above both. These are research identities, not claims of trained models or production engines.

[Chapter 13: SAT and combinatorial constructions](drafts/ch13/README.md) adds finite-copy clause selection, exhaustive small SAT oracles and coverage/resource derivations. [Chapter 14: Sticker systems and molecular memory](drafts/ch14/README.md) adds occupancy-register semantics, conditional writes, reset analysis and reuse limits. Each includes five editable mechanism figures with TXT companions and twelve worked exercises; current research comparisons have dated source-access notes.

[Chapter 15: Splicing and insertion-deletion systems](drafts/ch15/README.md) develops contextual cuts, finite-copy reactions, bounded reachability and chemical interface limits. [Chapter 16: Languages, automata and molecular recognition](drafts/ch16/README.md) develops recognizer invariants, an exact binary transducer, scaffolded recognition and noisy transitions. Each includes five editable vector figures with semantic TXT companions, tested reference code and twelve worked exercises.

[Chapter 17: Watson–Crick and biochemical automata](drafts/ch17/README.md) develops a proved two-head recognizer, explicit witness costs and a restriction-based molecular transition mechanism. [Chapter 18: Universality and complexity models](drafts/ch18/README.md) develops tape/two-stack simulation, uniform construction and reliability bounds.

Each new chapter includes five editable vector figures with TXT companions and twelve worked exercises. Chapters 13-18 are standalone author-reviewed candidates, not cumulative acceptance or independently validated industrial systems. Chapter 19 is next; cumulative integration remains pending.

## Build and verify

Chapter 3 now has a standalone [review edition](drafts/ch03/README.md), with twelve editable SVG/TXT figures and a page-inspected PDF. See the [review report and release gates](DEEP_CHAPTER_3_REVIEW_REPORT.md). It is not yet included in the accepted cumulative PDF.

```sh
python3 examples/deep/ch01.py
python3 examples/deep/ch02.py
python3 scripts/build_deep_chapter.py --check
python3 scripts/build_deep_chapter02.py --check
python3 scripts/build_textbook_plan.py --check
make pdf
python3 -m pytest
python3 scripts/review_deep.py
```

Dependencies: Python 3.10+ (pytest; Pillow for page review), XeLaTeX/latexmk, librsvg, Poppler, and DejaVu fonts. The full historical numerical regression suite also uses the existing repository dependencies. The PDF gate rejects old, empty, later-chapter, unreviewed, or changed-after-review source. To author new material, build a preview under build/ and complete review before updating the acceptance record; do not weaken the gate.

## Frozen editions

astra-undergraduate-rewrite is a pedagogical archive, not a parallel manuscript. Its source, figures, examples and committed PDF remain byte-identical. The default tests verify its preserved publication without rebuilding it; make historical-pdf remains an explicit reproduction tool under build/. Main, astra-rewrite and historical snapshots are preserved; no main merge is part of this milestone.

The original eight-section [preproduction outline](CHAPTER_1_OUTLINE.md) is retained as design history. The actual chapter deliberately expands it to 13 sections and ten figures. Full source-access details live in [the chapter source review](research/deep-ch01-sources.md). Review is author-agent work, not independent scientific certification or a real-reader study.
