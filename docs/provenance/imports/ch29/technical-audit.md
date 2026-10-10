# DNAD-29 technical audit

46 chapter tests. Independent checks:

- analytic/AD/FD across5times andbothrates
- zero/single-rate domains; input guards; no defaultdtype mutation
- geometric discrete solver gradients across3steps; h-refinement and detach mutant
- softplus chain; single/two-time rank and equilibrium scale counterexample
- all16softmaxgradient entries at3temperatures; rowshift/gauge checks
- 256-string expected-score and nonlinear mismatch oracles; exactGC/tie/constraints; localRNG

Three continuous derivative routes agree at477.5622517517959. Eulerh=.1 has derivative532.9885461886737, not the continuous target; repeated detach preserves forward but yields20.359627534869173. Refinement halves error. One observation is rank1; time1/time5 determinant-6324.0630410335225 gives local rank2 only. Soft motif score is exact expected positional match under independent sampling;256-string enumeration verifies it. 80updates post-step score.7804066666341538. Nonlinear uniform reward.75 vs all256onehotrewards0; expectedGC2 vs A-first argmaxGC0; strictGC enumeration givesAACC/.5.

Limitations: well-mixed constant first-order model, fixed initial populations, positive total-rate differentiable chart; no zero-total boundary gradient, calibrated chemistry, general differentiable SSA, Fast SeqProp reproduction, spatial model or biological sequence-design result. Selected finiteness guards do not prove arbitrary-magnitude numerical robustness. Continuous adjoint and Fisher information are derived context, not implemented production solvers. Enumeration length<=8 is an oracle, not scalable design.

Six original vector plates/TXT, five literal complete function listings and twenty exercises. Primary access depth is separately recorded. Strict local build and every-page color/grayscale author review must be bound to source/PDF hashes; cumulative and independent scientific/reader gates remain separate. No acceptance promotion or push.
