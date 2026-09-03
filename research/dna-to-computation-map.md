# DNA-to-computation map

| Biological or molecular phenomenon | State | Operator / transition | Digital model | Boundary |
| --- | --- | --- | --- | --- |
| base complementarity | ordered bases and orientation | pair-compatible mapping | string transform / permutation matrix | omits thermodynamics and kinetics |
| hybridization | strands, concentrations, temperature, salts | association/dissociation | exact matching, energy model, or stochastic reaction | a match score is not a melting-temperature prediction |
| restriction / ligation | molecular strands and cut sites | cleavage / covalent joining | substring cut and concatenation | omits enzyme specificity, yield, and side reactions |
| PCR | population of templates and reagents | denature, anneal, extend | branching/count process | omits reagent depletion and bias unless modeled |
| electrophoresis / affinity separation | molecular population | noisy physical partition | filter predicate with error model | an exact Boolean filter is idealized |
| recombination / splicing | structured strands | local rewrite | formal splicing or rewrite system | formal power depends on permitted rules/control |
| strand displacement | complexes and exposed domains | toehold bind, branch migrate, release | reaction transition system / CRN | domain abstraction hides sequence design and leakage |
| gene regulation | molecular concentrations, chromatin, context | binding, activation, repression, feedback | Boolean/probabilistic network or ODE | routing in a neural net is an analogy, not gene regulation |
| mutation and selection | populations over generations | variation and differential reproduction | evolutionary search | optimizer behavior is not biological evolution by default |

For every chapter example, the selected row becomes a checklist: declare what persists, what is copied, what is selected, what can occur in parallel, what is stochastic, and which physical assumptions are excluded.

