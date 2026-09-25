# Chapter 18: Universality and complexity models

Author-approved storyboard, 25 September 2026. Original figures planned before prose; independent review remains open.

## Figure 18.1: What changes in one Turing step

- Asset: 01-tape.tex, with semantic TXT companion.
- Objects and arrow meaning: Tape cells, read/write head, control state and one right move.
- Change/invariant and caption claim: A written symbol and a moved head determine the successor.
- Scientific risk to audit: Mathematical unbounded tape is a resource family, not an infinite device.

## Figure 18.2: What an implementation proof must preserve

- Asset: 02-simulation.tex, with semantic TXT companion.
- Objects and arrow meaning: Source configurations and target microsteps joined by decode maps.
- Change/invariant and caption claim: The two routes through a commuting diagram yield the same source successor.
- Scientific risk to audit: A finite trace comparison is not a universal simulation theorem.

## Figure 18.3: How binary increment actually uses resources

- Asset: 03-growth.tex, with semantic TXT companion.
- Objects and arrow meaning: Computed transition counts and visited tape span.
- Change/invariant and caption claim: Carry propagation changes step count while input width bounds the working region.
- Scientific risk to audit: This machine is an incrementer, not a universal machine.

## Figure 18.4: Where preparation can hide the answer

- Asset: 04-uniform.tex, with semantic TXT companion.
- Objects and arrow meaning: Instance, uniform constructor, encoded device and output interpreter.
- Change/invariant and caption claim: Count both program generation and execution; flag answer-dependent preparation.
- Scientific risk to audit: Do not confuse nonuniform advice with a practical solver.

## Figure 18.5: Local fidelity and whole-computation reliability

- Asset: 05-reliability.tex, with semantic TXT companion.
- Objects and arrow meaning: Generated per-step-error survival curves and a union-bound budget.
- Change/invariant and caption claim: Number of logical or physical events matters to the reliability claim.
- Scientific risk to audit: Assigned probabilities are not measured chemical error rates.
