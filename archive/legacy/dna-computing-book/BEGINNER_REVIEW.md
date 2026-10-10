# Beginner review: DNA Computing

> Historical undergraduate-design review, retained as evidence of the earlier experiment. It is not the active audience policy. See DEEP_REDESIGN.md and REVIEW_GATES.md for the deep edition.

This is an internal role-based walkthrough performed by the authoring assistant, not a panel of actual readers or separate agents. Status: revised architecture ready for user review; empirical readability remains untested.

| Perspective | Where the old route loses them | Applied structural revision | Remaining check |
|---|---|---|---|
| 18-year-old first-year student | Graph tuple, witness and completeness in the opening | Counters in DNAU-01; cities/dots/arrows in 05; Hamiltonian naming in 21; proofs after checking | Teach-back on opening paragraph and city sequence |
| Software-curious biology student | Implicit Python setup, dictionary and asymptotic cost knowledge | Syntax and execution in 04; small arrangement counts in 06; matrix rows in 34 | Try an installation-free activity before interpreter setup |
| Biology-curious programmer | Sugar positions, bonds and concentration assumed from vocabulary | Atoms/bonds in 07; quantities in 08; nucleotide zoom in 10; polarity in 11 | Ask reader to explain 5-prime versus sequence index |
| Technical entrepreneur | Molecular parallelism might sound like free speed | Tiny candidate counts first; physical instruments before reconstruction; resource limits in 24/35 | Ask what must be paid for besides elapsed time |
| Scientifically literate general reader | Research taxonomy and notation arrive before a motivating object | Tangible chapter questions, small operation chapters and repeated zoom-out connections | Verify specialist terms in figure captions, not just prose |

## Revisions from this walkthrough

- Split objects, chemistry and orientation rather than merging them into a single “molecular foundations” chapter.
- Separate ordinary graph paths from the all-vertices-once problem and from DNA encoding.
- Make Python installation and code syntax an explicit lesson rather than an exercise prerequisite.
- Teach independent-trial arithmetic before the repeated-trial expression.
- Give every laboratory operation its own input/action/output explanation.
- Keep vector and matrix basics in Book I so Book II has a real, testable bridge; do not pretend Book I already teaches ML.
- Treat the chapter count as flexible teaching units, not a one-semester promise.

## Opening design to test next, not drafted prose

DNAU-01: counters → written rule → step-by-step action → result → same rule on another material. No graph notation, Hamiltonian terminology, complexity class or proof appears in this opening plan. The exit task asks the reader to identify input, output and an ambiguous rule.

DNAU-11: sugar-position orientation → opposite-direction paired strands → same partner read from the other end → only then string notation and Python. Use AACG rather than a symmetric example that hides the difference.

## Unresolved

We have not observed novices reading new prose because no new prose is drafted. The first-use ledger is not exhaustive language analysis; words such as “parameter,” “representation” or “control” require context-sensitive checks. Source facts and final figure geometry remain chapter-production work. Actual course pacing and accessibility require testing on final artifacts.
