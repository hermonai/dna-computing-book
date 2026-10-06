# Continuation contract

DNAD-27 established exact symbolic transition semantics. DNAD-28 attached
deterministic and stochastic time semantics to a fixed stoichiometric model.
DNAD-29 adds differentiation as a *computational interface to a declared surrogate*.

The chapter must preserve these boundaries:

- a derivative is with respect to the chosen mathematical model, not directly
  with respect to physical chemistry;
- exact Gillespie reaction selection is discrete, so differentiable stochastic
  variants require estimators, relaxations or other approximations;
- a soft nucleotide distribution is not a physical DNA molecule;
- optimizing a predictor can exploit predictor error, so inverse design requires
  held-out/orthogonal validation;
- finite differences, analytic derivatives and autograd are independent checks
  where all are available;
- gradients require explicit units, parameterization and constraints.
