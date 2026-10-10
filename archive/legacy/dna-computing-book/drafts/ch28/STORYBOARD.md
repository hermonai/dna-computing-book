# Chapter 28 visual teaching plan

## 01-semantics

A shared reaction-channel node links A→B and B→A; each edge changes counts by one and conserves A+B. The continuous state node has concentrations in mol/L and a smooth ODE flux. The count state node has nonnegative integers, event propensities kf A and kr B, and random jumps. A conversion edge uses Omega=NA V; only the linear first-order mean matches the ODE exactly. Molecule shapes are abstract species, not sequence-level chemistry.

## 02-ssa

Count state and time determine hazards. Zero total hazard leads to an absorbing completed interval. Positive hazard fans out to an open-interval waiting-time uniform and a half-open channel-choice uniform. A before-horizon event updates the integer state, appends it, and loops. An after-horizon event leaves the preceding state valid through T. A budget-limit branch returns incomplete at current time and disallows queries beyond the simulated interval.

## 03-ode

The smooth plotted node is generated exact A(t)=20+80 exp(-0.5t) over t=0..5. Its equilibrium asymptote is a dashed line at 20. Side annotations distinguish universal positivity h<=2.5 from absolute stability h<=4; h=3 is a stable negative-population counterexample. The independently generated Euler table measures terminal errors and the first-order halving ratio. All populations are continuous copy-equivalents, not single-path fractional molecules.

## 04-ensemble

Left panel follows the generated seed-28 count path with right-continuous step segments; counts are integer and conserve A+B=100. Right panel is the exact Binomial(100,pAA) law at T=5, plotted from generated probabilities, not an empirical histogram. An annotation compares the exact mean and individual-path variance with the 2000-path sample mean and its standard error. The panels must not conflate population spread with uncertainty of an estimated mean.

## 05-units

Distinct species give A*B eligible partners and propensity k AB/Omega under v=k a b. Identical species give choose(A,2) unordered pairs and pair coefficient 2k/Omega under the declared event law v=k a^2. A separate stoichiometric edge consumes two A per event, yielding da/dt=-2v. Omega=NA V is a unit-conversion node; doubling V at fixed copies halves propensity. This illustration is a combinatorial mechanism, not molecular geometry.

## 06-validation

Domain validation flows to enabled stoichiometric jumps and independent analytic law checks. Stopping status separates complete from censored paths before ensemble aggregation. Statistical evidence compares mean, variance, and Monte Carlo uncertainty. A dashed edge leads to experimental calibration/held-out validation, an explicitly unperformed gate. Author model tests do not become scientific or publication acceptance.

All figures use editable vector sources, numbered captions and semantic TXT companions. Shape, position, solid/dashed lines and explicit labels preserve meaning in grayscale. Charts are generated from the tested reference, not invented visual data. Original artwork; no copied textbook illustrations.
