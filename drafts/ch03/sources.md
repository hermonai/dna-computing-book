# Chapter 3 source ledger: first technical core

Consulted 9 September 2026. This ledger distinguishes directly read support from located-but-unread material. It is not a systematic review or independent approval.

## Directly read support

- Michael Sipser, MIT 18.404J (2020), [Lecture 14: P and NP, SAT, polynomial-time reducibility](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/45e2fd621349cfd7c9faf93a6ba134a3_MIT18_404f20_lec14.pdf). The certificate, input-encoding and reduction discussion was read from the instructor's notes. Used for class conventions, not a proof of a separation between P and NP.
- MIT 6.046J (2015), [Recitation 8](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/1dee182d301235b901119a0ff57f05e2_MIT6_046JS15_Recitation8.pdf), section 2, physical page 2. Read the directed-cycle-to-path vertex-splitting construction and both existence implications. Our original figure uses a three-cycle; the executable extension exposes fixed endpoints and arbitrary pivot relabeling. The source's naive verifier bounds are not substituted for our separately stated representation-aware account.
- Sipser, [Lecture 15 resource and transcript](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/lecture-15-np-completeness/). Read the caution that directed 3SAT-to-HAMPATH gadgets require internal consistency details. No incomplete gadget diagram was promoted to a complete proof in this draft.

## Located but not used as a fully read proof

- Stephen Cook, *The Complexity of Theorem-Proving Procedures* (1971): [author-hosted scan](https://www.cs.toronto.edu/~sacook/homepage/1971.pdf), linked from the author's publication list. The bibliographic record and abstract were read; the scan did not expose machine-readable text in the browser. No claim that the whole paper was read. Its original reduction formulation needs care before attributing a modern many-one statement verbatim to it.
- Richard Karp, *Reducibility Among Combinatorial Problems* (1972): bibliographic identification only in this pass. Obtain and read the original relevant construction before expanding the full hardness chain.

## Original derivations and computations

### Second-pass source check

Toronto CS 2401 (Fall 2015), instructor Toniann Pitassi, lecturer Thomas Watson, scribe Benett Axtell: [Lecture 3](https://www.cs.toronto.edu/~toni/Courses/Complexity2015/lectures/lecture3.pdf), section 4 on physical page 4. Read the definition of coNP through language complementation, its universal-certificate formulation, and the statement that P is closed under complementation. Used only for these class conventions. The manuscript supplies its own deterministic complement-closure argument. The scribe prose about “flip the bits of the witness” is imprecise and is not copied or used as a proof: it is the verifier predicate that must be negated under the changed quantifier. No interactive-proof theorem is invoked.

Rechecked Sipser lecture 14's representation and complement question. The new figures show explicit counting units and quantifiers, without a separation diagram. The edge-deletion figure is generated from the actual retained-graph trace; its test replays every step against independent enumeration on all 4,096 four-vertex directed graphs.

The four-vertex instance, subset recurrence proof, dense reachable-state count, elementary vertex-position CNF clause count and edge-deletion self-reduction explanation are derived explicitly in the manuscript and checked by the local reference. These are pedagogical reconstructions of standard ideas, not claims of novel algorithms.

`reference.py` uses only Python's standard library. Its oracle enumerates interior permutations independently of the subset algorithm. Tests cover all 4,096 simple directed four-vertex graphs for existence agreement, all 64 three-vertex graphs with all three reduction pivots, and all 512 Boolean assignments per three-vertex CNF instance. Counts are algorithmic counters, not timing data.

## Scope exclusions

No P-versus-NP resolution, best-known exact-algorithm claim, universal molecular lower bound or new laboratory result. The full reduction chain, deeper work/depth treatment and physical accounting remain publication dependencies. Earlier historical/chemical details continue to rely on the preserved Chapter 2 source ledger; this draft does not re-report that work as new research.
