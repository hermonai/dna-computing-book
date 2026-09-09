# Chapter 3. Combinatorial search and complexity

Working draft, 9 September 2026. This is the first technical core, not an accepted publication chapter. Chapters 1–2 remain the published build. Figure numbers below are stable draft asset IDs, not final LaTeX numbering.

## 3.1 A successful experiment leaves an algorithmic question

Chapter 2 showed how a molecular population can encode candidates and how selective operations can enrich a witness. But a seven-vertex success cannot, by itself, answer a question about a growing family of inputs. What happens as the graph grows? Which resource grows? Does an observed failure mean the graph has no solution, or only that the experiment failed to expose one?

To ask those questions precisely, separate an **instance**, an **algorithm**, and an **implementation**. The instance is a particular directed graph with specified endpoints. The algorithm determines which transformations and tests are performed. The implementation supplies storage, arithmetic, reactions, transfers and measurements. Complexity theory begins with an explicit abstract cost model. Molecular engineering must additionally explain how that model is realized.

We will use a new four-vertex graph, not silently replace the historical graph:

\[
V=\{0,1,2,3\},\quad s=0,\quad t=3,
\]
\[
E=\{(0,1),(0,2),(1,2),(2,1),(1,3),(2,3)\}.
\]

It has two Hamiltonian witnesses: \((0,1,2,3)\) and \((0,2,1,3)\). The existence of two paths will matter: an algorithm that remembers only one representative can still answer an existence question correctly, while losing counting information.

## 3.2 The quantifier makes the problem

Define a relation \(R(G,s,t,P)\) that holds exactly when \(P\) lists every vertex once, starts at \(s\), ends at \(t\), and follows only edges of \(G\). The decision question is

\[
\exists P\;R(G,s,t,P)?
\]

The search question asks for such a \(P\), or a justified report that none exists. The verification question takes a proposed \(P\) as an additional input and evaluates \(R\). These questions share a relation but require different outputs. Rejecting \((0,1,3,2)\) does not answer the existence question for our graph; both valid paths above still exist.

![A verifier accepts or rejects one certificate, not all possible certificates.](figures/DNAD-03-F1.svg)

**DNAD-03-F1.** A verified certificate establishes a yes-instance. A rejected certificate only eliminates the submitted order. The distinction is the existential quantifier, not a difference in terminology.

Under an adjacency-matrix representation already in memory, a verifier can mark each visited vertex and check each successive edge. This takes \(O(n)\) word-level operations for an \(n\)-vertex candidate when indexing and labels fit the chosen word model. Reading or constructing the full matrix still costs \(\Theta(n^2)\) bits/entries at the appropriate representation level. Do not quote the verifier's inner loop as the end-to-end cost of acquiring the graph.

The reference `verify` validates its graph argument before checking the certificate, so its total Python work also includes graph normalization. Set lookup, integer representation and interpreter overhead are implementation details; our operation counts below are not measured processor timings.

## 3.3 Polynomial in which size?

An algorithm's running time is a function of the encoded input length, not merely the largest number printed in its input. A binary integer \(N\) takes approximately \(\log_2 N\) bits; performing \(N\) iterations can therefore take exponentially many iterations in that bit length. For explicitly represented simple graphs, matrix and adjacency-list encodings differ in size but can be translated with polynomial overhead. A succinct circuit describing an exponentially larger graph would define a different representation problem.

The usual class **P** contains decision problems decidable in polynomial time. **NP** can be characterized by polynomial-length certificates whose validity is checked in polynomial time. The certificate definition does not prescribe enumerating all certificates, and it does not describe a physical machine creating every possibility for free. These are the conventions used in [Sipser's lecture on P, NP and reducibility](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/45e2fd621349cfd7c9faf93a6ba134a3_MIT18_404f20_lec14.pdf).

An important negative statement follows from logic alone: the definition supplies short certificates for yes-instances. It does not automatically supply short certificates for no-instances. Negating the entire existence statement gives \(\forall P\,\neg R(G,s,t,P)\), not the rejection of one chosen \(P\). We should not confuse that distinction with a proof that no concise negative certificate could ever exist.

## 3.4 Reuse the future question, not the entire history

Naive fixed-endpoint enumeration examines up to \((n-2)!\) interior orders. Many prefixes, however, lead to the same remaining problem. Suppose two valid prefixes have visited the same set \(S\) and both end at vertex \(v\). The remaining vertices are \(V\setminus S\), and the next step must use an outgoing edge from \(v\). Their internal orders no longer affect whether an unused suffix can complete the path.

This motivates a Boolean state:

\[
D[S,v]=\text{a simple path from }s\text{ visits exactly }S\text{ and ends at }v.
\]

![Two valid histories merge only when both their visited set and endpoint agree.](figures/DNAD-03-F2.svg)

**DNAD-03-F2.** This separate five-vertex illustration exposes a state equivalence before the final step. Equal visited sets alone are insufficient: different last vertices can have different outgoing edges. Equal last vertices alone are also insufficient: different used vertices permit different future moves.

Start with \(D[\{s\},s]=\mathrm{true}\). For a reachable state and an unused neighbor \(w\), set

\[
D[S\cup\{w\},w]\leftarrow\mathrm{true}
\quad\text{if }(v,w)\in E\text{ and }w\notin S.
\]

Process sets in increasing cardinality. The invariant is proved by induction. The base state is the one-vertex path. Every transition appends one unused vertex through a permitted edge, preserving validity. Conversely, remove the last vertex from any valid longer path. Its remaining prefix is a valid smaller state, and the recurrence restores exactly that final step. Therefore \(D[V,t]\) is true if and only if a witness exists.

Our implementation additionally refuses to enter \(t\) before the set is full. This is safe because a simple path ending at \(t\) cannot leave \(t\) and later revisit it. One predecessor per reachable state is enough to reconstruct one witness. It is not enough to count all witnesses or represent their molecular multiplicities. Different questions need different state values and sometimes different state definitions.

There are at most \(n2^n\) mask/endpoint pairs. Scanning up to \(n\) outgoing neighbors for each gives an \(O(n^2 2^n)\) upper bound in the usual unit-cost subset-DP account, with \(O(n2^n)\) state storage. This is not a best-known-algorithm claim. The executable implementation uses arbitrary-precision Python bitmasks, whose operations acquire a size-dependent cost as masks exceed machine words. Both accounts remain exponential, not polynomial.

## 3.5 What the counters actually show

On the four-vertex example, the implementation creates six reachable states, arranged in cardinality layers \(1,2,2,1\), and performs ten outgoing-neighbor scans. The two full paths merge into one terminal reachability state. These counts come from [the executable result artifact](results.json), not a decorated complexity diagram.

For the complete directed graph with fixed endpoints and \(n\ge3\), our early-terminal rule permits exactly

\[
2+(n-2)2^{n-3}
\]

reachable states. To derive this, count the initial state and final state separately. Every other state chooses one of the \(n-2\) interior vertices as its last vertex, then any subset of the other \(n-3\) interior vertices as already visited. Completeness of the graph makes every such choice reachable. At \(n=8\), the result is 194 states. This is a state-count formula for this graph family and this implementation, not a general physical-resource law.

The tests compare subset search against independent permutation enumeration on **every one of the 4,096 simple directed four-vertex graphs**. This is useful fault detection. The inductive invariant is what supports correctness for arbitrary finite graph size; exhaustive testing at size four cannot replace it.

## 3.6 A reduction has a direction and two implications

A polynomial many-one reduction from problem \(A\) to problem \(B\) computes a mapping \(f\) such that

\[
x\in A\iff f(x)\in B.
\]

Thus a fast solver for \(B\), composed with \(f\), would solve \(A\). Hardness travels from the source problem toward the target problem. A mapping in the reverse direction establishes a different claim.

Consider a directed Hamiltonian-cycle instance. Choose a pivot vertex, replace it by a source \(s\) and sink \(t\), redirect outgoing pivot edges from \(s\), and redirect incoming pivot edges into \(t\). Keep the other edges. A cycle through the pivot opens into a spanning \(s\)-to-\(t\) path. Conversely, identifying the endpoints of such a path closes a cycle through the original vertices. The construction adds one vertex and preserves the number of edges for our loop-free graph convention. This is the vertex-splitting reduction presented in [MIT's algorithms recitation](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/1dee182d301235b901119a0ff57f05e2_MIT6_046JS15_Recitation8.pdf).

![Opening and closing a cycle at a split pivot.](figures/DNAD-03-F3.svg)

**DNAD-03-F3.** The three-cycle is an illustration, not the proof for every graph. The code checks all simple directed three-vertex graphs and every pivot, including graphs without cycles.

This argument transfers an established hardness premise for directed Hamiltonian cycle to the fixed-endpoint path problem. It does not establish that premise from scratch. A full path from satisfiability to the Hamiltonian family needs a separately reviewed construction; do not hide that missing step inside a decorative arrow.

## 3.7 Encode the whole predicate in Boolean clauses

We can also map a fixed-endpoint path instance to a satisfiability instance. This direction is useful for expressing constraints but, by itself, is not a proof that the path problem is NP-hard.

Let \(x_{v,p}\) mean that vertex \(v\) occupies position \(p\). There are \(n^2\) variables. Require exactly one vertex at each position and exactly one position for each vertex. An elementary exactly-one encoding uses one positive clause for “at least one” and a negative two-literal clause for every pair that must not both be true. Add the unit clauses \(x_{s,0}\) and \(x_{t,n-1}\). Finally, for each forbidden transition \((u,v)\notin E\) and each \(p<n-1\), add

\[
\neg x_{u,p}\lor\neg x_{v,p+1}.
\]

![The assignment matrix separates permutation constraints from legal transitions.](figures/DNAD-03-F4.svg)

**DNAD-03-F4.** A permutation matrix can still describe a forbidden-edge route. The transition clauses implement the extra adjacency condition already exposed by Chapter 2's pseudo-path.

Soundness is direct: every satisfying assignment is a permutation matrix, and the endpoint and transition clauses turn its decoded order into a witness. Completeness is also direct: encode any valid path by putting true in its occupied vertex/position cells; every clause family is then satisfied.

Our encoding emits

\[
2n+2n\binom n2+2+(n-1)(n^2-m)
\]

clauses for a loop-free directed graph with \(m\) edges. The four terms count positive exactly-one clauses, pairwise exclusions, endpoints and forbidden transitions. Self-transitions are included among forbidden edges even though the permutation constraints already rule them out; redundancy does not invalidate the encoding. Our toy graph produces 16 variables, 88 clauses and 190 literal occurrences. Tests inspect all \(2^9\) Boolean assignments for each three-vertex graph, not just hand-picked permutation assignments. That catches encodings that accidentally admit malformed matrices.

## 3.8 Turn a decision oracle into a witness

Suppose an oracle answers the fixed-endpoint existence question. Ask it once about the original graph. If the answer is yes, consider edges one by one. Delete an edge whenever the oracle says a witness still exists without it. This maintains a yes-instance and terminates after at most \(m+1\) oracle calls.

Why does the remaining graph reveal a path? Select any spanning witness in the final graph. If an edge lay outside that witness, removing it would preserve that witness, contradicting edge minimality. Hence every remaining edge belongs to the chosen path; the final graph contains exactly its \(n-1\) edges. An edge that was indispensable when considered cannot become dispensable after further deletions: deleting more edges cannot create a missing path. This justifies a single pass over the edges.

The companion implements this reduction with `subset_search` as its oracle. That oracle is exponential; calling it “an oracle” does not remove its cost. On our six-edge toy graph, seven calls leave the witness \((0,2,1,3)\). This differs from the first witness returned by subset search, without any contradiction: the task requests a witness, not a unique canonical order.

## 3.9 Bring the accounting back to molecules

The Boolean DP can forget alternate histories because its question is existential. A molecular population cannot always be treated that way. Copy numbers affect survival and detection, and different sequences with the same abstract future role may have different physical interactions. A proposed molecular implementation of the recurrence must explain how sets and endpoints are represented, how equivalent states are recognized, and what each transition costs.

Similarly, reducing a graph to a polynomial-size formula says that the formula is not exponentially larger than the encoded graph. It does not say that solving the formula is polynomial. Putting candidate assignments into many simultaneous physical objects changes allocation and depth, not the need to account for those objects.

The next resource chapter should therefore keep total work, critical-path depth, material, memory and readout separate. No theorem in this draft turns all DNA Hamiltonian solvers into factorial algorithms, and no small-instance simulation proves asymptotic superiority over electronic computation.

## 3.10 Exercises with worked reasoning

1. **A failed certificate.** In the four-vertex example, submit \((0,1,3,2)\). Does rejection prove the instance is negative? **Solution:** It ends at 2 rather than 3 and requires absent edge \(3\to2\). This rejects that order only; either listed witness proves the instance positive.
2. **Insufficient state.** Why not store only the visited set? **Solution:** Two prefixes using the same set may end at different vertices. Their available outgoing edges differ, so they need not admit the same completion. The last vertex must be retained unless another representation supplies equivalent information.
3. **Counting witnesses.** Can the one-predecessor table count both toy witnesses? **Solution:** No. Boolean reachability merges successful histories. Counting requires a sum over predecessor counts with a base count of one. Reconstructing all paths requires still more information or traversal; its output can itself be large.
4. **Reduction direction.** Does a polynomial path-to-SAT encoding prove path hardness? **Solution:** Not by itself. It says a SAT solver can solve the encoded path problem. For a hardness transfer from SAT, a reduction must go from SAT to the claimed hard target, with both existence implications proved.
5. **Clause audit.** Explain the 88 toy clauses. **Solution:** Eight positive row/column clauses plus 48 pairwise exclusions plus two endpoint units plus \(3(16-6)=30\) transition exclusions total 88. The redundant self-transition exclusions are included in that total.
6. **Oracle budget.** Why do seven oracle calls not constitute a seven-step polynomial-time path solver? **Solution:** The calls contain substantial computations. Here each call uses an exponential subset algorithm. A polynomial number of calls to a hypothetical polynomial-time oracle would imply a polynomial-time composition, but that hypothesis has not been established.

## Publication work still required

Expand the complexity-class and reduction foundations with a primary-source-reviewed hardness chain; complete the remaining eight storyboard figures, including work/depth and no-signal logic; add further research exercises; integrate LaTeX references, index and glossary; then perform scientific, mathematical and every-page publication review. The working draft is deliberately excluded from the accepted entry point and its source-hash review.
