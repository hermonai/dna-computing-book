# Chapter 20 storyboard
Approved author plan, 27 September 2026. No independent review implied.

Question: what does a reaction program preserve, compute and cost?
Prerequisites: Chapters 7, 17-19. This chapter owns program semantics and composition;
Chapter 28 owns general-purpose solvers and fitting.

1. Molecular interface: I + G -> W + O, actual antiparallel strands before/after.
   Invariant: three physical strand identities. Risk: species are not single strands.
2. Reaction coordinates: R, P and N columns for A+B -> W and 2A -> W.
   Change: one enabled jump; distinguish pair availability from net change.
3. Completion: equal-input annihilation, finite molecule-count staircase versus
   deterministic concentration tail. Axes use count-equivalent units and seconds.
   Risk: an ODE is not the mean of a low-copy jump process.
4. Shared fuel: catalysts A and B consume one common F pool into Y and Z.
   Annotate catalyst return, material invariant and competing reaction extents.
   Risk: formal catalytic arrows are not a sequence-level implementation.
5. Compiler contract: retain concrete molecular intermediates and show projection
   to a coarse state. Explicit residual and timescale assumptions; no exact
   lumpability claim for an arbitrary DNA cascade.

Five semantic TXT companions; twelve worked problems. Reference implements
validated stoichiometry, mass-action drift, finite-copy propensities, one exact
reaction event, completion moments and a shared-fuel solution.
