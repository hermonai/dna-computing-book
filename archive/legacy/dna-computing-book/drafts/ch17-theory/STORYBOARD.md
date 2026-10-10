# Chapter 17: Watson–Crick and biochemical automata

Expanded-theory author storyboard, 25 September 2026. Original assets 01-05 are retained; numbering in the typeset edition follows order of first use. New assets below are planned before the expanded prose. Independent review remains open.

## New plate 06: Syntactic determinism and prefix conflicts

- Question: Can two outgoing block rules apply to the same unread suffixes?
- Objects: two upper/lower label pairs; shared-prefix extensions; an explicit conflicting configuration.
- Semantics: comparison is logical compatibility, not a chemical transition.
- Caption claim: simultaneous prefix comparability flags a syntactic conflict; absence of conflicts guarantees at most one enabled rule on any fixed pair.
- Risk: compatibility alone does not prove reachability on an admissible paired input.

## New plate 07: One logical step and several chemical microsteps

- Question: What must an implementation preserve across binding, release and cleavage?
- Objects: symbolic state/suffix; free input complex, reversible bound complex, committed product and released transition species.
- Semantics: solid arrows are reactions; dashed vertical arrows are decoding at stable interfaces. A reversible binding loop is silent logically.
- Caption claim: completed chemical steps must refine the specified logical transition, while eventual completion requires a separate progress assumption.
- Risk: this is a declared reusable-transition coarse-graining, not a sequence-level reconstruction of the ligation-consuming 2001 device.

## New plate 08: Competing commitment paths

- Question: Why do concentrations alone not determine branch probabilities?
- Objects: common available input, two binding channels with dissociation and commitment, conditional-success probabilities and absolute probability mass.
- Semantics: rates carry units; the derived race sums to the probability of any commitment before a deadline, leaving an explicit uncommitted remainder.
- Caption claim: distinguish eventual branch odds, completion by a deadline and conditional correctness.
- Risk: exponential coarse-graining requires stated timescale and constant-pool assumptions; all numerical rates are assigned teaching values.

## Figure 17.1: Two coordinates on one paired input

- Asset: 01-heads.tex, with semantic TXT companion.
- Objects and arrow meaning: Antiparallel DNA polarity; two abstract head positions, both physically rightward.
- Change/invariant and caption claim: Distinguish coordinate direction from enzymatic synthesis.
- Scientific risk to audit: Read-only heads are a formal device, not molecular motors.

## Figure 17.2: Recognizing equal blocks by head separation

- Asset: 02-lag.tex, with semantic TXT companion.
- Objects and arrow meaning: Head-position lattice with three phases for aabb.
- Change/invariant and caption claim: Lag supplies input-dependent configuration memory.
- Scientific risk to audit: Identity pairing in an abstract alphabet is not natural base complementarity.

## Figure 17.3: Existential pairing is a resource choice

- Asset: 03-witness.tex, with semantic TXT companion.
- Objects and arrow meaning: Upper symbols and multiple admissible lower symbols; one accepting path.
- Change/invariant and caption claim: Separate pair acceptance from existential upper-language acceptance.
- Scientific risk to audit: A witness oracle is not free molecule preparation.

## Figure 17.4: How a molecular transition consumes an interface

- Asset: 04-cleavage.tex, with semantic TXT companion.
- Objects and arrow meaning: Polarity-correct duplex, transition recognition, enzyme-mediated cleavage and a newly exposed end.
- Change/invariant and caption claim: Separate current state/symbol interface from next-state interface and waste.
- Scientific risk to audit: Conceptual restriction-based cycle; not a sequence or enzyme protocol.

## Figure 17.5: State count does not count head positions

- Asset: 05-frontier.tex, with semantic TXT companion.
- Objects and arrow meaning: Computed reachable configurations and generic grid bound.
- Change/invariant and caption claim: Termination comes from advancing heads; all branches must be examined for rejection.
- Scientific risk to audit: A Python search counts logical configurations, not molecules.
