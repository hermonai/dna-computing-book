# Chapter 3 progress: executable foundations

9 September 2026. **Working draft, not publication acceptance.**

The next chapter, **Combinatorial search and complexity**, now has [a substantive first manuscript](drafts/ch03/manuscript.md), [source-access notes](drafts/ch03/sources.md), a 12-figure storyboard, four original editable SVG/TXT figure pairs, runnable reference code and computed results. All eight produced figures across the two books were rendered and visually inspected for readable labels, correct directions, formulas and declared numerical axes. This is figure review, not PDF page review.

The reference implements a certificate verifier, subset-state search, an independent permutation oracle, decision-to-search edge deletion, a directed-cycle-to-fixed-path reduction and vertex-position CNF encoding. Exhaustive small-instance tests cover all 4,096 four-vertex directed graphs, all 64 three-vertex graphs and every pivot, and all 512 Boolean assignments for each three-vertex CNF. The manuscript proves the recurrence and encoding equivalence while explicitly leaving the fuller primary-source hardness chain for the next pass.

The current publication metadata, Chapter 1–2 manuscript sources, acceptance records and public branches are not advanced by this draft. Existing PDFs are preserved. The regression build previously rewrote the current PDF as a side effect of testing; its test now builds in a temporary copy and asserts that the original PDFs remain unchanged. No acceptance gate or scientific review flag was weakened.

## Verification and remaining work

The full suite passes **204 tests**, including the real PDF build in an isolated copy. The accepted source gate still passes and the original publication PDFs remain byte-identical. No tests were disabled to accommodate the draft.

The user's illustration direction is incorporated into CHAPTER_STANDARD.md for both books: explain biological mechanisms with scientifically grounded structures and reaction sequences, and algorithmic mechanisms with states, transformations and data flow. The first revision replaces text-only prefix summaries with explicit directed path histories and replaces the stacked gradient-rule list with a forward/reverse computation diagram. Both revised figures were rendered and inspected.

Complete the remaining eight figures per book, unresolved source/proof work, extended exercises and publication apparatus before promoting Chapter 3. No new PDF, moving animation, laboratory result, model benchmark or independent scientific review is claimed.
