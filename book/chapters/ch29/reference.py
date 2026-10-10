"""DNAD-29: derivatives of declared Float64 surrogates, not physical DNA."""

from __future__ import annotations

import itertools
import json
import math
import torch

ALPHABET = "ACGT"
DTYPE = torch.float64
LISTINGS = [
    "reversible_a_t",
    "analytic_sensitivities",
    "euler_sensitivity",
    "soft_motif_gradient",
    "exact_constrained_design",
]
TABLES = [
    (
        "gradient-checks",
        ["Route / step", "$dJ/dk_f$", "Absolute error"],
        ["route", "gradient", "error"],
        "lrr",
    ),
    (
        "euler-checks",
        ["$h$ [s]", "$A(T)$", "$dJ_h/dk_f$", "Gradient error"],
        ["h", "terminal", "gradient", "error"],
        "rrrr",
    ),
    (
        "identifiability",
        ["Observation", "$s_f$", "$s_r$"],
        ["observation", "sf", "sr"],
        "lrr",
    ),
]
PLOTS = [
    ("trajectory", "sensitivity", "t", ["A"]),
    ("sensitivity", "sensitivity", "t", ["sf", "sr"]),
    ("design", "design", "step", ["score"]),
]


def finite(x, name, *, nonnegative=False):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x):
        raise ValueError(f"{name}: finite scalar required")
    if nonnegative and x < 0:
        raise ValueError(f"{name}: nonnegative scalar required")
    return float(x)


def problem(t, a0, b0, kf, kr):
    values = [
        finite(v, n, nonnegative=True)
        for v, n in zip((t, a0, b0, kf, kr), ("t", "a0", "b0", "kf", "kr"))
    ]
    if values[3] + values[4] <= 0:
        raise ValueError("positive total rate required for this differentiable chart")
    return values


def tensor_scalar(x, name):
    if not isinstance(x, torch.Tensor) or x.ndim != 0 or x.dtype != DTYPE:
        raise ValueError(f"{name}: scalar Float64 tensor required")
    if x.device.type != "cpu" or not bool(torch.isfinite(x)) or float(x.detach()) < 0:
        raise ValueError(f"{name}: finite nonnegative CPU tensor required")


def reversible_a_t(t, a0, b0, kf, kr):
    """Graph-preserving solution; kf+kr>0, t>=0, common state units."""
    for x, n in zip((t, a0, b0, kf, kr), ("t", "a0", "b0", "kf", "kr")):
        tensor_scalar(x, n)
    lam = kf + kr
    if float(lam.detach()) <= 0:
        raise ValueError("positive total rate required")
    q = -torch.expm1(-lam * t)
    return a0 * (1 - kf * q / lam) + b0 * kr * q / lam


def scalar_a(t, a0, b0, kf, kr):
    """Independent Python/math closed form, no Torch or AD calls."""
    t, a0, b0, kf, kr = problem(t, a0, b0, kf, kr)
    lam = kf + kr
    equilibrium = (a0 + b0) * kr / lam
    return equilibrium + (a0 - equilibrium) * math.exp(-lam * t)


def analytic_sensitivities(t, a0, b0, kf, kr):
    """Partial derivatives of A(t); rate units inverse time."""
    t, a0, b0, kf, kr = problem(t, a0, b0, kf, kr)
    lam = kf + kr
    total = a0 + b0
    q = -math.expm1(-lam * t)
    decay = math.exp(-lam * t)
    displacement = a0 - total * kr / lam
    sf = -total * kr * q / lam**2 - displacement * t * decay
    sr = total * kf * q / lam**2 - displacement * t * decay
    return sf, sr


def terminal_objective(kf_value, target=30.0, t=5.0, a0=100.0, b0=0.0, kr=0.1):
    problem(t, a0, b0, kf_value, kr)
    target = finite(target, "target", nonnegative=True)
    tensors = [torch.tensor(v, dtype=DTYPE) for v in (t, a0, b0, kf_value, kr)]
    tensors[3].requires_grad_(True)
    a = reversible_a_t(*tensors)
    loss = (a - target) ** 2
    (gradient,) = torch.autograd.grad(loss, tensors[3])
    return float(loss.detach()), float(gradient), float(a.detach())


def central_difference(f, x, eps=1e-6):
    x, eps = finite(x, "x"), finite(eps, "eps")
    if eps <= 0 or x + eps == x or x - eps == x:
        raise ValueError("positive representable finite-difference step required")
    result = (f(x + eps) - f(x - eps)) / (2 * eps)
    if not math.isfinite(result):
        raise ValueError("nonfinite finite difference")
    return result


def finite_difference_terminal(kf, eps=1e-6):
    # Differentiates a pure scalar objective, not the AD wrapper.
    return central_difference(
        lambda k: (scalar_a(5.0, 100.0, 0.0, k, 0.1) - 30.0) ** 2, kf, eps
    )


def steps_count(steps):
    if type(steps) is not int or steps < 1:
        raise ValueError("positive exact integer steps required")


def euler_sensitivity(t, a0, b0, kf, kr, steps):
    """Forward Euler plus simultaneous manual sensitivity recurrence."""
    t, a0, b0, kf, kr = problem(t, a0, b0, kf, kr)
    steps_count(steps)
    h, total, a, s = t / steps, a0 + b0, a0, 0.0
    if h * max(kf, kr) > 1:
        raise ValueError("Euler positivity bound violated")
    for _ in range(steps):
        old_a, old_s = a, s
        a = old_a + h * (-kf * old_a + kr * (total - old_a))
        s = old_s + h * (-old_a - (kf + kr) * old_s)
    return a, s


def euler_autograd(kf_value, steps, detach_mutant=False):
    steps_count(steps)
    problem(5.0, 100.0, 0.0, kf_value, 0.1)
    h = 5 / steps
    if h * max(kf_value, 0.1) > 1:
        raise ValueError("Euler positivity bound violated")
    k = torch.tensor(kf_value, dtype=DTYPE, requires_grad=True)
    a = torch.tensor(100.0, dtype=DTYPE)
    for _ in range(steps):
        previous = a.detach() if detach_mutant else a
        a = previous + h * (-k * previous + 0.1 * (100 - previous))
    loss = (a - 30) ** 2
    (grad,) = torch.autograd.grad(loss, k)
    return float(a.detach()), float(grad)


def soft_sequence(logits, temperature=1.0):
    temperature = finite(temperature, "temperature")
    if temperature <= 0:
        raise ValueError("positive temperature required")
    if not isinstance(logits, torch.Tensor) or logits.dtype != DTYPE:
        raise ValueError("Float64 logits required")
    if logits.ndim != 2 or logits.shape[0] < 1 or logits.shape[1] != 4:
        raise ValueError("nonempty [L,4] logits required")
    if not bool(torch.isfinite(logits).all()):
        raise ValueError("finite logits required")
    return torch.softmax(logits / temperature, dim=-1)


def motif_score(probs, motif="ACGT"):
    if not isinstance(motif, str) or not motif or any(c not in ALPHABET for c in motif):
        raise ValueError("nonempty ACGT motif required")
    if not isinstance(probs, torch.Tensor) or probs.dtype != DTYPE:
        raise ValueError("Float64 probabilities required")
    if probs.shape != (len(motif), 4) or not bool(torch.isfinite(probs).all()):
        raise ValueError("finite [L,4] probability matrix required")
    if bool((probs < 0).any()) or not torch.allclose(
        probs.sum(-1), torch.ones(len(motif), dtype=DTYPE), atol=1e-12, rtol=0
    ):
        raise ValueError("probability simplex required")
    idx = torch.tensor([ALPHABET.index(c) for c in motif], device=probs.device)
    return probs[torch.arange(len(motif), device=probs.device), idx].mean()


def soft_motif_gradient(logits, motif="ACGT", temperature=1.0):
    """Manual softmax-chain derivative, independent of backward()."""
    p = soft_sequence(logits, temperature)
    motif_score(p, motif)  # validate the score domain
    onehot = torch.zeros_like(p)
    ids = torch.tensor([ALPHABET.index(c) for c in motif], device=p.device)
    onehot[torch.arange(len(motif), device=p.device), ids] = 1
    matches = (p * onehot).sum(-1, keepdim=True)
    return matches * (onehot - p) / (len(motif) * temperature)


def optimize_soft_motif(steps=80, lr=0.4, temperature=1.0):
    if type(steps) is not int or steps < 0:
        raise ValueError("nonnegative exact integer steps required")
    lr = finite(lr, "lr")
    if lr <= 0:
        raise ValueError("positive learning rate required")
    logits = torch.zeros((4, 4), dtype=DTYPE, requires_grad=True)
    history = [float(motif_score(soft_sequence(logits, temperature)).detach())]
    for _ in range(steps):
        score = motif_score(soft_sequence(logits, temperature))
        (gradient,) = torch.autograd.grad(score, logits)
        with torch.no_grad():
            logits.add_(lr * gradient)
        history.append(float(motif_score(soft_sequence(logits, temperature)).detach()))
    p = soft_sequence(logits, temperature).detach()
    sequence = "".join(ALPHABET[i] for i in p.argmax(-1).tolist())
    return history, sequence, p


def exact_constrained_design(motif="AAAA", gc_count=2):
    """Exhaustive discrete oracle, length<=8; exact GC count, lexical ties."""
    if not isinstance(motif, str) or not 1 <= len(motif) <= 8:
        raise ValueError("nonempty motif length <=8 required")
    if any(c not in ALPHABET for c in motif):
        raise ValueError("ACGT alphabet required")
    if type(gc_count) is not int or not 0 <= gc_count <= len(motif):
        raise ValueError("valid exact integer GC count required")
    best, best_score = None, -1.0
    for word in itertools.product(ALPHABET, repeat=len(motif)):
        if sum(c in "GC" for c in word) != gc_count:
            continue
        score = sum(a == b for a, b in zip(word, motif)) / len(motif)
        if score > best_score:
            best, best_score = "".join(word), score
    return best, best_score


def results():
    loss, ad, terminal = terminal_objective(0.4)
    sf, sr = analytic_sensitivities(5.0, 100.0, 0.0, 0.4, 0.1)
    analytic = 2 * (scalar_a(5.0, 100.0, 0.0, 0.4, 0.1) - 30) * sf
    checks = [
        {"route": "Analytic", "gradient": analytic, "error": 0.0},
        {"route": "Autograd", "gradient": ad, "error": abs(ad - analytic)},
    ]
    for eps in (1e-2, 1e-3, 1e-5, 1e-6, 1e-8):
        fd = finite_difference_terminal(0.4, eps)
        checks.append(
            {"route": f"FD {eps:g}", "gradient": fd, "error": abs(fd - analytic)}
        )
    euler = []
    for n in (50, 100, 200, 400):
        a, s = euler_sensitivity(5.0, 100.0, 0.0, 0.4, 0.1, n)
        g = 2 * (a - 30) * s
        euler.append(
            {"h": 5 / n, "terminal": a, "gradient": g, "error": abs(g - analytic)}
        )
    rows = []
    for t in (1.0, 5.0):
        s1, s2 = analytic_sensitivities(t, 100.0, 0.0, 0.4, 0.1)
        rows.append({"observation": f"T={t:g} s", "sf": s1, "sr": s2})
    det = rows[0]["sf"] * rows[1]["sr"] - rows[0]["sr"] * rows[1]["sf"]
    hist, sequence, p = optimize_soft_motif()
    uniform = torch.full((4, 4), 0.25, dtype=DTYPE)
    false_relaxation = float((1 - (uniform**2).sum(-1)).mean())
    constrained, score = exact_constrained_design()
    full_a, full_g = euler_autograd(0.4, 50)
    bad_a, bad_g = euler_autograd(0.4, 50, True)
    return {
        "kinetic": {
            "terminal": terminal,
            "loss": loss,
            "sf": sf,
            "sr": sr,
            "gradient": ad,
        },
        "gradient-checks": checks,
        "euler-checks": euler,
        "identifiability": rows,
        "two_time_sensitivity_determinant": det,
        "detach_counterexample": {
            "same_forward": full_a == bad_a,
            "correct_gradient": full_g,
            "mutant_gradient": bad_g,
        },
        "sequence": {
            "initial": hist[0],
            "final": hist[-1],
            "argmax": sequence,
            "probabilities": p.tolist(),
            "false_soft_score": false_relaxation,
            "all_discrete_false_scores": 0.0,
            "constrained_sequence": constrained,
            "constrained_score": score,
        },
        "sensitivity": [
            {
                "t": t / 4,
                "A": scalar_a(t / 4, 100.0, 0.0, 0.4, 0.1),
                "sf": analytic_sensitivities(t / 4, 100.0, 0.0, 0.4, 0.1)[0],
                "sr": analytic_sensitivities(t / 4, 100.0, 0.0, 0.4, 0.1)[1],
            }
            for t in range(21)
        ],
        "design": [{"step": i, "score": s} for i, s in enumerate(hist)],
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
