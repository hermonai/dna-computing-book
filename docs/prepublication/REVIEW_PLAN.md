# Review plan: undergraduate textbook revision

Started 18 October 2026 from `main` at `5987341` (identical to the public review
prerelease `dna-review-2026-10-17`). Brief: `docs/CLAUDE_PREPUBLICATION_REVIEW_PROMPT.md`,
plus the author's instruction to restructure where useful, add current
research, unify the bibliography and publish to `main`.

## Audience and reconciliation

Undergraduate accessibility is the primary teaching level; scientific accuracy
and depth are retained. `docs/CHAPTER_STANDARD.md` (deep edition, September 2026)
assumed declared mathematics and programming; the current brief takes precedence
where they conflict. Reconciliation adopted in this revision:

- Every chapter opens with learning goals and the ideas it relies on, and closes
  with key ideas; derivations, proofs and executable checks are unchanged.
- Background for readers from the other discipline is supplied in **Biology
  bridge** and **Computing bridge** boxes and two appendices (molecular biology
  primer; mathematical toolkit), not by removing technical content.
- One edition only. The archived undergraduate prototype is not revived.

## Prerequisite map

| Concept | Introduced | Used by |
|---|---|---|
| strand direction, complementarity | Ch 1 primer (Sec. 1.4), Ch 5 | 2, 8, 11, 19, 22, 25 |
| multiset, copies vs identities | Ch 1, Ch 4 | 12, 13, 14, 23, 24 |
| at-least-one probability, logs | App. B, Ch 1, Ch 4 | 9, 12, 13, 23, 24 |
| equilibrium, free energy | Ch 6 | 11, 19, 22, 23 |
| rates, ODEs, propensities | Ch 7 | 19, 20, 21, 28, 30, 31 |
| enzymes (cut, join, copy) | Ch 8, App. A | 2, 9, 15, 17 |
| complexity classes | Ch 3 (CS bridge in Ch 1) | 13, 18, 24 |
| automata | Ch 16 | 17, 18 |
| strand displacement | Ch 19 | 20, 21, 27, 31 |

## Structure

The 32-chapter numbering is retained (tests, manifests and companion code are
keyed to it). Chapters are grouped into eight Parts with orientation pages
(`book/parts/`), a reading map with core, theory and laboratory paths, an
Epilogue on frontiers and open problems, and three appendices. No chapter was
merged or renumbered.

## Batches

1. Infrastructure: visual language, boxes, Parts, front matter, unified
   bibliography, appendices, Epilogue. Chapter 1 as calibration sample.
2. Chapters 2–10 (molecular toolkit plates).
3. Chapters 11–26 (DNA neural networks, origami, storage).
4. Chapters 27–32, glossary, records, validation, publication to `main`.

## Next concrete batch (not yet done)

See `PUBLICATION_READINESS.md`. The highest-value next step is a full-resolution
page-by-page visual pass of the ~170 retained older plates against the new
visual language, starting with Chapters 11–18, followed by independent
specialist and student review.
