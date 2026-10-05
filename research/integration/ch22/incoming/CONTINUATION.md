# Continuity contract

Chapter 21 established that molecular circuits require explicit material, timing,
loading and observation interfaces. Chapter 22 retains that discipline but changes
the computational substrate from reaction trajectories to spatial growth.

Inherited definitions and boundaries:
- strand polarity, concentration/count distinctions, reaction kinetics and finite-copy
  noise from Chapters 5–7;
- formal language/computability versus physical realization from Chapters 16–18;
- explicit material and kinetic interfaces from Chapters 19–21;
- abstract correctness never implies high physical yield.

New definitions:
- oriented square tile type, glue label, nonnegative integer glue strength;
- finite assembly as a partial map Z^2 -> tile types;
- temperature tau=2 legal attachment by matching occupied neighbors;
- producible, terminal and directed assembly;
- frontier, mismatch and attachment ambiguity;
- abstract tile complexity, area, frontier work and finite-yield model.

The chapter proves a deterministic seeded XOR construction under the stated aTAM
variant and supplies an independent cellular-automaton oracle. It then shows a
single added tile type that creates attachment ambiguity. Physical DNA-tile and
origami sections map abstract sides to recognition interfaces but do not equate
strength integers with energies.

Next: DNAD-23 — Errors, redundancy and molecular reliability.
