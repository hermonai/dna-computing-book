import importlib.util
import itertools
import math
from pathlib import Path
import pytest
import torch

P = Path(__file__).parents[1] / "drafts/ch29/reference.py"
S = importlib.util.spec_from_file_location("dnad29", P)
R = importlib.util.module_from_spec(S)
S.loader.exec_module(R)
D = torch.float64


@pytest.mark.parametrize("t", [0.0, 1e-8, 1.0, 5.0, 100.0])
def test_three_routes_each_partial(t):
    k = torch.tensor(0.4, dtype=D, requires_grad=True)
    r = torch.tensor(0.1, dtype=D, requires_grad=True)
    a = R.reversible_a_t(
        torch.tensor(t, dtype=D),
        torch.tensor(100.0, dtype=D),
        torch.tensor(20.0, dtype=D),
        k,
        r,
    )
    grads = torch.autograd.grad(a, (k, r))
    analytical = R.analytic_sensitivities(t, 100.0, 20.0, 0.4, 0.1)
    for axis, (g, exact) in enumerate(zip(grads, analytical)):
        fd = R.central_difference(
            lambda x: (
                R.scalar_a(t, 100.0, 20.0, x, 0.1)
                if axis == 0
                else R.scalar_a(t, 100.0, 20.0, 0.4, x)
            ),
            (0.4, 0.1)[axis],
        )
        assert float(g) == pytest.approx(exact, abs=1e-12)
        assert fd == pytest.approx(exact, abs=2e-8)
    assert float(a.detach()) == pytest.approx(R.scalar_a(t, 100.0, 20.0, 0.4, 0.1))


@pytest.mark.parametrize(
    "kf,kr,expected", [(0.0, 0.1, 120.0), (0.4, 0.0, 0.0), (0.4, 0.1, 24.0)]
)
def test_equilibrium_and_initial(kf, kr, expected):
    assert R.scalar_a(0.0, 100.0, 20.0, kf, kr) == pytest.approx(100.0)
    assert R.scalar_a(1000.0, 100.0, 20.0, kf, kr) == pytest.approx(expected)


@pytest.mark.parametrize("bad", [-1.0, float("nan"), float("inf"), True])
def test_bad_rate(bad):
    with pytest.raises(ValueError):
        R.terminal_objective(bad)


def test_all_zero_rates_outside_chart():
    with pytest.raises(ValueError):
        R.analytic_sensitivities(5.0, 100.0, 0.0, 0.0, 0.0)


def test_no_global_dtype_mutation():
    assert torch.get_default_dtype() == torch.float32


def test_terminal_scalar_oracle():
    loss, g, a = R.terminal_objective(0.4)
    # Independently differentiate equilibrium+transient on paper.
    e = math.exp(-2.5)
    expected_a = 20 + 80 * e
    sf = -40 * (1 - e) - 400 * e
    assert a == pytest.approx(expected_a)
    assert loss == pytest.approx((expected_a - 30) ** 2)
    assert g == pytest.approx(2 * (expected_a - 30) * sf, abs=1e-11)


def test_fd_sweep_convergence():
    g = R.terminal_objective(0.4)[1]
    assert abs(R.finite_difference_terminal(0.4, 1e-5) - g) < abs(
        R.finite_difference_terminal(0.4, 1e-3) - g
    )


@pytest.mark.parametrize("eps", [0.0, -1.0, float("nan"), 1e-30])
def test_bad_difference_step(eps):
    with pytest.raises(ValueError):
        R.central_difference(lambda x: x * x, 0.4, eps)


@pytest.mark.parametrize("steps", [10, 50, 200])
def test_euler_manual_discrete_derivative(steps):
    a, s = R.euler_sensitivity(5.0, 100.0, 0.0, 0.4, 0.1, steps)
    ad_a, g = R.euler_autograd(0.4, steps)
    # Independent geometric-series solution of the discretized recurrence.
    h = 5 / steps
    geom = (1 - 0.5 * h) ** steps
    oracle_a = 20 + 80 * geom
    oracle_s = -40 * (1 - geom) - 80 * steps * h * (1 - 0.5 * h) ** (steps - 1)
    assert a == pytest.approx(oracle_a)
    assert s == pytest.approx(oracle_s)
    assert ad_a == pytest.approx(a)
    assert g == pytest.approx(2 * (a - 30) * s)
    fd = R.central_difference(
        lambda k: (R.euler_sensitivity(5.0, 100.0, 0.0, k, 0.1, steps)[0] - 30) ** 2,
        0.4,
    )
    assert g == pytest.approx(fd, abs=2e-7)


def test_euler_gradient_converges_but_finite_h_different():
    g = R.terminal_objective(0.4)[1]
    errors = [abs(R.euler_autograd(0.4, n)[1] - g) for n in (50, 100, 200, 400)]
    assert all(a > b > 0 for a, b in zip(errors, errors[1:]))


def test_detach_mutant_forward_passes_gradient_fails():
    a, g = R.euler_autograd(0.4, 50)
    b, bad = R.euler_autograd(0.4, 50, True)
    assert a == b
    assert abs(g - bad) > 100


def test_euler_positivity_guard():
    with pytest.raises(ValueError):
        R.euler_sensitivity(5.0, 100.0, 0.0, 0.4, 0.1, 1)


def test_identifiability_rank_and_steady_ratio():
    row = R.analytic_sensitivities(5.0, 100.0, 0.0, 0.4, 0.1)
    # One row cannot identify both rates; nonzero perpendicular perturbation.
    tangent = (row[1], -row[0])
    assert sum(a * b for a, b in zip(row, tangent)) == 0
    rows = [R.analytic_sensitivities(t, 100.0, 0.0, 0.4, 0.1) for t in (1.0, 5.0)]
    assert abs(rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]) > 100
    assert R.scalar_a(1e6, 100.0, 0.0, 0.4, 0.1) == pytest.approx(
        R.scalar_a(1e6, 100.0, 0.0, 0.8, 0.2)
    )


def test_softplus_chain():
    rho = torch.tensor(-0.7, dtype=D, requires_grad=True)
    k = torch.nn.functional.softplus(rho)
    a = R.reversible_a_t(
        torch.tensor(5.0, dtype=D),
        torch.tensor(100.0, dtype=D),
        torch.tensor(0.0, dtype=D),
        k,
        torch.tensor(0.1, dtype=D),
    )
    (g,) = torch.autograd.grad((a - 30) ** 2, rho)
    outer = R.terminal_objective(float(k.detach()))[1]
    assert float(g) == pytest.approx(outer / (1 + math.exp(0.7)))


@pytest.mark.parametrize("tau", [0.3, 1.0, 2.0])
def test_softmax_all_gradient_entries(tau):
    generator = torch.Generator().manual_seed(29)
    logits = torch.randn(4, 4, dtype=D, generator=generator, requires_grad=True)
    p = R.soft_sequence(logits, tau)
    score = R.motif_score(p)
    (g,) = torch.autograd.grad(score, logits)
    oracle = R.soft_motif_gradient(logits.detach(), "ACGT", tau)
    assert torch.allclose(g, oracle, atol=1e-15, rtol=1e-13)
    assert torch.allclose(g.sum(-1), torch.zeros(4, dtype=D), atol=1e-15)
    assert torch.allclose(R.soft_sequence(logits.detach() + 7, tau), p.detach())


def test_expected_score_enumerates_discrete_sequences():
    logits = torch.arange(16, dtype=D).reshape(4, 4) / 7
    p = R.soft_sequence(logits)
    expected = 0.0
    for word in itertools.product(range(4), repeat=4):
        probability = math.prod(float(p[i, b]) for i, b in enumerate(word))
        exact = sum(b == i for i, b in enumerate(word)) / 4
        expected += probability * exact
    assert float(R.motif_score(p)) == pytest.approx(expected, abs=1e-14)


@pytest.mark.parametrize("tau", [0.0, -1.0, float("nan"), float("inf"), True])
def test_invalid_temperature(tau):
    with pytest.raises(ValueError):
        R.soft_sequence(torch.zeros(4, 4, dtype=D), tau)


def test_invalid_simplex_shape_alphabet():
    with pytest.raises(ValueError):
        R.soft_sequence(torch.zeros(4, 5, dtype=D))
    with pytest.raises(ValueError):
        R.motif_score(torch.ones(4, 4, dtype=D))
    with pytest.raises(ValueError):
        R.motif_score(torch.full((4, 4), 0.25, dtype=D), "ACGN")


def test_design_complete_history_and_local_rng():
    state = torch.random.get_rng_state().clone()
    hist, seq, p = R.optimize_soft_motif()
    assert len(hist) == 81 and hist[0] == 0.25
    assert all(b > a for a, b in zip(hist, hist[1:]))
    assert hist[-1] == float(R.motif_score(p))
    assert seq == "ACGT"
    assert bool(((p > 0) & (p < 1)).all())
    assert torch.equal(state, torch.random.get_rng_state())


def test_nonlinear_relaxation_failure_every_onehot():
    uniform = torch.full((4, 4), 0.25, dtype=D)
    assert float((1 - (uniform**2).sum(-1)).mean()) == 0.75
    for word in itertools.product(range(4), repeat=4):
        x = torch.zeros(4, 4, dtype=D)
        x[torch.arange(4), torch.tensor(word)] = 1
        assert float((1 - (x**2).sum(-1)).mean()) == 0


def test_expected_gc_not_argmax_constraint():
    # Uniform probabilities meet expected GC=2; deterministic A tie break gives GC=0.
    p = torch.full((4, 4), 0.25, dtype=D)
    assert float(p[:, 1:3].sum()) == 2
    assert "".join(R.ALPHABET[i] for i in p.argmax(-1)) == "AAAA"
    assert R.exact_constrained_design() == ("AACC", 0.5)


def test_constrained_design_matches_independent_binary_gc_patterns():
    word, score = R.exact_constrained_design("AAAA", 2)
    # Exactly two non-A symbols force at least two mismatches, attainable by AACC.
    assert sum(c in "GC" for c in word) == 2 and score == 0.5


@pytest.mark.parametrize("gc", [-1, 5, True, 2.5])
def test_invalid_constraint(gc):
    with pytest.raises(ValueError):
        R.exact_constrained_design(gc_count=gc)
