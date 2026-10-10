# DNAD-30 technical audit

55 chapter tests. Incoming ZIP fully inspected before explicit import; original
provenance remains in incoming/. Finite nonnegative scalar states and declared
probability domains are enforced.

Independent checks:

- Partition-function occupancy and explicit two-allele arithmetic.
- At alpha=3, symmetric c=1.2134116627622298 has eigenvalues -2.191058891491847
  and +0.191058891491847. Asymmetric roots (2.618033988749895,
  0.38196601125010515) and their swap have eigenvalues -5/3 and -1/3.
  The symmetry-breaking threshold alpha=2 follows from c=1.
- Simultaneous Euler is positive for 0<h<=1. Independent dense rational-RHS
  RK4 checks first-order refinement. Sequential updates and h=2 are falsifiers.
- Exact symmetry remains invariant even at a saddle. The biased tau=60 path
  approaches a stable branch; production-off preserves the initial state
  and has a separate exact decay oracle.
- Recorded lineage edges require known parents and increasing observed times;
  pseudotime sorting gives a different relation.
- Eight independent bit strings give N=3 partition probabilities 1/8,3/8,3/8,1/8.
  Daughter counts sum to N; they are not independently sampled.
- Reproduction-before-mutation, weight-scale invariance and neutrality are checked.
  For p0=1/4, weights 2 and 1, no mutation, pt=2^t/(2^t+3), p6=64/67.
  Reversing mutation and selection changes the operator.

The dimensionless model is phenomenological, not a calibrated toggle, experimental
developmental trajectory, sequence evolution or measured fitness. The executable
folds RNA/protein mechanisms into effective production/loss. Hill exponent does
not prove stoichiometric cooperation. Local stability and finite-domain guards
do not prove global numerical robustness or biological adequacy. The 2026 GRN
perspective is labeled a research agenda.

Six original editable plates/TXT, five complete tested listings and twenty worked
exercises. Final source/PDF hashes, regression and every-page color/grayscale
author review are bound separately. Cumulative and independent review do not
inherit standalone acceptance. No publication acceptance promotion or push.
