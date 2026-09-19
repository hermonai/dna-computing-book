# Chapter 7 visual reasoning plan

Original editable TikZ figures; semantic TXT companions explain every mechanism.
No copied artwork or ASCII diagrams. Numerical plots are generated from tested code.

## Figure 7.1: Distinct strands and duplex inventory

Source: figures/01-reaction.tex

Free A and B are antiparallel when aligned. Association consumes one of each and forms one duplex. Dissociation reverses the count change. Backbone arrowheads specify 5-prime to 3-prime polarity; dashed rungs denote noncovalent pairing. Neither arrow implies replication. Four-base illustration is schematic, not the sequence that determines an experimentally measured rate.

## Figure 7.2: Same equilibrium, different clock

Source: figures/02-relaxation.tex

Two exact deterministic concentration trajectories start at zero duplex with 100 nM total of each strand. Baseline kon is 1e6 M^-1 s^-1 and koff is 0.005 s^-1. Multiplying both by ten preserves 5 nM Kd and 80 nM equilibrium while rescaling time. Solid and dashed styles remain distinguishable in grayscale.

## Figure 7.3: Two random choices, one event

Source: figures/03-event-clock.tex

Current integer state determines association and dissociation propensities. Their sum sets exponential waiting time. Their ratio sets channel choice independently at this state. Execute the chosen stoichiometric change only if within the horizon, then recompute. The dashed return arrow is computational feedback, not another chemical reaction.

## Figure 7.4: A single vessel changes by integers

Source: figures/04-trajectory.tex

Exact-event model sampled with seed 1701, 20 copies per strand, volume 3.321078134e-16 L, kon 1e6 and koff 0.005, 120 seconds. Step plot holds the post-event value until the next event. Final extension to horizon is not an event. This is simulated, not measured.

## Figure 7.5: Stationary population distribution

Source: figures/05-distribution.tex

Bars are normalized probabilities from the birth-death detailed-balance recurrence, not the histogram of one sample trajectory. Full computation covers counts zero through twenty; display shows ten through twenty and says that lower counts are omitted. All counts remain in normalization. Finite-copy stochastic means need not equal the deterministic equilibrium root.
