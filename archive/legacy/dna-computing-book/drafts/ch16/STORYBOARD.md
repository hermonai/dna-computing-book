# Chapter 16: Languages, automata and molecular recognition

Author-approved storyboard for the original standalone candidate. Independent review remains open.

## 01-dfa

Question: What memory is needed to recognize a word ending in 01?
Objects and arrow semantics: Three-state directed graph; accepting double circle; each edge consumes exactly one bit.
Change/invariant and caption claim: States remember the longest useful suffix, not the full input.
Scientific risk: End-of-input is necessary before interpreting acceptance.

## 02-trace

Question: What changes when a symbol is consumed?
Objects and arrow semantics: Input cells and a cursor paired with the DFA state at each step.
Change/invariant and caption claim: Cursor advances once and the transition table determines the next state.
Scientific risk: Do not treat state changes as observed chemical transitions.

## 03-transducer

Question: How does one carry bit implement addition?
Objects and arrow semantics: Two carry states, local input bit pairs, emitted sum bit and final carry flush.
Change/invariant and caption claim: Least-significant-bit-first order is part of the contract.
Scientific risk: Fixed-width overflow must not silently disappear.

## 04-scaffold

Question: How can local matching encode an automaton constraint?
Objects and arrow semantics: Antiparallel position-bound compute strands on a scaffold, matching state-domain interfaces, one deliberately mismatched interface.
Change/invariant and caption claim: Satisfying local adjacency encodes a valid state path.
Scientific risk: Conceptual domain schematic, not a validated base-sequence design or kinetic pathway.

## 05-errors

Question: Can a missing molecule be called a rejected word?
Objects and arrow semantics: Mass-preserving logical-state distribution plus a separate absorbing loss state.
Change/invariant and caption claim: Correct/incorrect transitions differ from disappearance and readout.
Scientific risk: Assigned noise parameters are illustrative, not experimental fits.
