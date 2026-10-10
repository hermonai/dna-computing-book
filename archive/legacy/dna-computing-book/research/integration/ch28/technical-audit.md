# DNAD-28 technical audit

35 chapter tests: independent equilibrium closed form across five times; zero-rate and tiny-time stable evaluation; every-step geometric Euler oracle; first-order refinement; stable-but-negative counterexample; positivity endpoint; strict count/rate/clock/seed domains; hand inverse-transform and threshold ties; no uniform epsilon clamp; conserved nonnegative integer unit jumps; local RNG isolation; right-continuous event-time observation; explicit event-budget censoring; absorbing and zero-horizon branches; independent five-molecule configuration enumeration; fixed 2000-path mean/variance comparison; volume scaling; identical-reactant factor-of-two and nonlinear mean-closure counterexamples.

ODE and CTMC share first-order mean because propensities are linear. The mixed-initial-state distribution is a sum of two binomial groups, generally not one binomial. Exact-law mean26.566799889911906 and variance19.508851326005672; fixed ensemble mean26.702, sample variance19.51895547773887, estimated meanSE.09879006902958128. Seed28 path111events final(29,71), rendered as a right-continuous staircase extended to horizon. No discarded censored paths.

For bimolecular event law v=k a b, alpha=k AB/(NA V). For v=k a^2 in 2A→P, alpha=k A(A-1)/(NA V), equivalently2k/Omega*choose(A,2), and consumed concentration rate is -2v. Other reported rate conventions require conversion. Euler positivity h max(kf,kr)<=1 differs from stability h(kf+kr)<=2. No clipping of invalid states.

Limitations: well-mixed, constant first-order model; no fitted chemical rates, spatial transport, sequence thermodynamics, accelerator benchmark or wet-lab replication. Selected intermediate finiteness guards are not a proof for arbitrary-magnitude inputs. Internal Trajectory objects are trusted outputs, not an external path-authentication schema.

Incoming raw browser citation tokens and failed compilation evidence were not propagated. The following actual Chapter29 package is Differentiable molecular and sequence models, not the incoming handoff's Experimental design and calibration label; bridge follows the inspected manuscript. Frozen opening/accepted sources remain unchanged.

Gates: chapter tests, full regression, strict build, every-page color/grayscale review, source/PDF hash binding, cumulative build, independent scientific/reader review, and publication acceptance are distinct. Six mechanism/algorithm plates, five literal tested function listings and twenty worked exercises.
