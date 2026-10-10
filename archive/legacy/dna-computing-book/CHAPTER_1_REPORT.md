# Chapter 1 production report: DNA Computing

Date: 6 September 2026. Status: internally reviewed development chapter; no independent expert certification or learner study.

## Identity and scope

Starting commit: 505ab529d1752070ac6c1a66b0c3e49028f260a2.
Branch: astra-undergraduate-rewrite.
Publication commit: the commit containing this report (retrieve with git log -1 --format=%H -- CHAPTER_1_REPORT.md); its exact hash is supplied in the final delivery. This avoids a self-referential hash inside its own commit.

Approved title: **What does it mean to compute?**.
Canonical source: [tex/undergraduate/ch01.tex](tex/undergraduate/ch01.tex).
The title agreed across the approved redesign files. No old chapter prose was copied; earlier tex/chapters/ch01.tex and ch02.tex remain byte-identical. Only this chapter is active.

## Section sequence

1. Start with five counters, not five prerequisites
2. A rule must say what to do
3. Optional: let a computer follow that rule
4. Information needs a representation
5. Why introduce DNA?
6. From a physical change to an answer
7. What the rest of the book must earn
8. Practice: recognize, apply, question
9. Answers and a second look

## Learning objectives and prerequisite handling

Identify input, rule, steps and output; apply add-two by hand; explain representation and reading convention; distinguish DNA's physical order from an invented encoding; require representation, operation and readout evidence for a molecular design. Entry is ordinary arithmetic and reading. A minimal molecule preview motivates the subject without importing graph theory or lab chemistry.

The paper exercise remains compulsory; the tiny code section is optional. This explicitly refines the original no-new-code planning note without changing the entry contract.

## Terms, figures and executable material

18 retained glossary definitions: input; output; step; computation; rule; program; Python; function; information; representation; physical medium; atom; bond; molecule; DNA; strand; sequence; DNA computing.

The [terminology ledger](research/undergraduate-ch01-terminology.md) records first sentence/heading preview, definition sentence, section, picture or worked example, glossary key and related term. It includes early title/objective previews instead of pretending every name first appears at its formal definition.

- DNAU-01-F1: Counting by moving objects.
- DNAU-01-F2: One rule, one intended result.
- DNAU-01-F3: A quantity is not its carrier.
- DNAU-01-F4: From molecule to written order.
- DNAU-01-F5: What would make a physical change a computation?.
- DNAU-01-F6: The route from counting to molecules.

Each figure has original editable SVG, a Unicode TXT semantic companion, title/description metadata, scientific risk and evidence record. The generator is scripts/build_undergraduate.py; sources are under book/figures/undergraduate and book/diagrams/undergraduate. No copied textbook image, decorative raster illustration, ASCII box art or exported animation is included.

New code: examples/undergraduate/ch01_rule.py (add_two, two lines). The listing is included directly with VerbatimInput. The generated trace and artifacts/undergraduate/ch01-results.json run that exact function. Independent hand expectations test 0, 3, 4 and 7. There are eight exercises and eight answer notes.

## Verification

Full-suite result: 66 passed in 8.78 seconds (Python 3.13.6; pytest with real PDF integration).
Baseline rerun before production: 50 passing tests.
New Chapter 1 tests: 16 cases covering exact outputs, repeatability/boundary behavior, generated assets, six editable SVG/TXT pairs, invalid storyboard rejection, glossary/reference closure, source-linked code and real LaTeX/PDF integration.

The original architecture-only blocking test was legitimately replaced by a stricter new-edition gate: only the new Chapter 1 may build; empty, unreviewed or preserved-edition manifests are rejected. Existing computational examples and historical preservation regressions remain.

Publication: 16 A4 PDF pages, of which nine are the chapter (printed pages 1–9). There are three physical front-matter pages and four back-matter pages. All pages were rendered and inspected; final minor text corrections were rebuilt and rechecked. No overfull/underfull boxes, missing glyphs or undefined references remain in the checked build. PDFs are not tagged; no PDF/UA claim is made.

## Actual page and figure review findings

- Added a visible tray boundary to the counter storyboard to separate the counted collection from waiting objects.
- Repainted roadmap connectors after panels so their arrowheads remain visible.
- Kept figures and captions at authored paragraph boundaries after a biology float split a sentence.
- Prevented the Evolutor chapter title from hyphenating its project name.
- Made bibliography URLs ragged-right, eliminating meaningful spacing warnings.
- Generated reciprocal glossary links without duplicate punctuation or recursive location records.
- Corrected sentence-initial term presentation and exact lowercase returned words.

All six figures were checked independently of prose for identity, arrow meaning, labeling, reading size and grayscale interpretation. The biology illustrations explicitly state schematic level and missing machinery; software uses data flow, not molecular shapes. Front/back matter deliberately has more whitespace than teaching pages.

## Internal beginner and general-reader review

These are author-agent role perspectives, not actual participants.

The beginner review checked whether numbered counters might be mistaken for amounts; the caption now states that numbers identify objects. The general-reader review checked the jump from counting to DNA; representations now bridge it, and the molecule vocabulary is defined locally. Optional syntax is explained one piece at a time. Information is explicitly informal, not a sudden mathematical measure.

## Internal specialist-perspective review

| Perspective | Question and disposition |
|---|---|
| Molecular biologist | Does F4 imply a complete molecule or biological encoding of arithmetic? No: it is a labeled strand segment and the mapping is separate. |
| Chemist | Are boxes atoms or missing polarity presented as accurate chemistry? Caption says no; atom/bond/molecule are introductory descriptions, detailed structure deferred. |
| DNA-computing researcher | Is the checklist mistaken for an experiment or speed claim? It is explicitly a design abstraction; the Adleman statement is bounded to the inspected abstract. |
| CS instructor | Do hand rule, notation, code and answer agree? Exact-case tests and direct source inclusion check them; running is distinguished from correctness. |

## Claims and limits

Seven new ledger rows DNAU-CL01 through DNAU-CL07 cover the exact toy, working definitions, DNA structure, introductory chemistry vocabulary, bounded historical demonstration, design checklist and planned route.
See [claims ledger](research/claims-ledger.md) and [source register](research/undergraduate-ch01-sources.md). No scientific experiment was performed.

Remaining weaknesses: actual learner testing and independent subject review are still needed; chemical pictures are intentionally introductory; short exact tests do not validate arbitrary inputs; PDF accessibility structure is incomplete; index coverage emphasizes substantive definitions rather than a final exhaustive book-wide index. Later chapter links refer to plans, not completed text.


## Cross-book conclusion and next scope

See [the shared comparison](CROSS_BOOK_CHAPTER_1_REVIEW.md) and [the production standard](CHAPTER_STANDARD.md), written after the real production/review work.

Next: DNAU-02 — Symbols, information and representations, after DNAU-01.
No next chapter was drafted in this milestone.
