"""DNAD-23 reliability calculations; model outputs, not fitted DNA measurements."""

from math import comb, exp, fsum, isfinite, log, log1p, sqrt
import json
import random


def count(value, minimum=0):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError("integer count outside domain")
    return value


def probability(value):
    if isinstance(value, bool) or not isfinite(value) or not 0 <= value <= 1:
        raise ValueError("finite probability in [0,1] required")
    return value


def object_yield_independent(p, n_sites):
    probability(p)
    count(n_sites)
    if n_sites == 0 or p == 0:
        return 1.0
    return 0.0 if p == 1 else exp(n_sites * log1p(-p))


def yield_bounds(p, n_sites):
    """Sharp all-correct bounds for equal error marginals, without independence."""
    probability(p)
    count(n_sites)
    return (1.0, 1.0) if n_sites == 0 else (max(0.0, 1 - n_sites * p), 1 - p)


def majority_failure(p, copies):
    """Exact binomial tail for odd IID repetition."""
    probability(p)
    count(copies, 1)
    if copies % 2 == 0:
        raise ValueError("odd repetition required")
    return fsum(
        comb(copies, k) * p**k * (1 - p) ** (copies - k)
        for k in range(copies // 2 + 1, copies + 1)
    )


def beta_parameters(alpha, beta):
    if any(isinstance(v, bool) or not isfinite(v) or v <= 0 for v in (alpha, beta)):
        raise ValueError("positive finite beta parameters required")
    if not isfinite(alpha + beta):
        raise ValueError("beta parameter sum exceeds floating range")


def beta_binomial_pmf(k, n, alpha, beta):
    """Beta mixture of binomial counts; sum logarithms to avoid lgamma cancellation."""
    count(n)
    count(k)
    beta_parameters(alpha, beta)
    if k > n:
        raise ValueError("defects exceed eligible sites")
    # B(k+a,n-k+b)/B(a,b) = (a)_k (b)_(n-k)/(a+b)_n.
    logp = (
        log(comb(n, k))
        + fsum(log(alpha + i) for i in range(k))
        + fsum(log(beta + i) for i in range(n - k))
        - fsum(log(alpha + beta + i) for i in range(n))
    )
    return exp(logp)


def all_correct_beta_binomial(n, alpha, beta):
    count(n)
    beta_parameters(alpha, beta)
    # More stable direct product ratio for k=0.
    return exp(
        fsum(
            log1p(-alpha / (alpha + beta + i))
            if alpha < beta + i
            else log(beta + i) - log(alpha + beta + i)
            for i in range(n)
        )
    )


def correlated_majority_failure(copies, alpha, beta):
    count(copies, 1)
    beta_parameters(alpha, beta)
    if copies % 2 == 0:
        raise ValueError("odd repetition required")
    return fsum(
        beta_binomial_pmf(k, copies, alpha, beta)
        for k in range(copies // 2 + 1, copies + 1)
    )


def wilson(k, n, z=1.96):
    count(n, 1)
    count(k)
    if k > n or isinstance(z, bool) or not isfinite(z) or z <= 0:
        raise ValueError("valid count and positive finite quantile required")
    ph = k / n
    den = 1 + z * z / n
    center = (ph + z * z / (2 * n)) / den
    half = z * sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return max(0.0, center - half), min(1.0, center + half)


def observed_defect_probability(true_p, false_positive, false_negative):
    for p in (true_p, false_positive, false_negative):
        probability(p)
    return false_positive * (1 - true_p) + (1 - false_negative) * true_p


def infer_defect_probability(observed_p, false_positive, false_negative):
    for p in (observed_p, false_positive, false_negative):
        probability(p)
    contrast = 1 - false_positive - false_negative
    if contrast == 0:
        raise ValueError("classifier provides no defect information")
    p = (observed_p - false_positive) / contrast
    if not -1e-12 <= p <= 1 + 1e-12:
        raise ValueError("observation incompatible with calibrated classifier")
    return max(0.0, min(1.0, p))


def simulate_repetition(p, copies, trials=100000, seed=23):
    majority_failure(p, copies)  # validates the same domain
    count(trials, 1)
    rng = random.Random(seed)
    return (
        sum(
            sum(rng.random() < p for _ in range(copies)) > copies // 2
            for _ in range(trials)
        )
        / trials
    )


def amplification_fraction(fraction, gain_target, gain_background, cycles):
    """Two-species, constant per-cycle gain model. No stochastic PCR simulation."""
    probability(fraction)
    count(cycles)
    if any(
        isinstance(v, bool) or not isfinite(v) or v <= 0
        for v in (gain_target, gain_background)
    ):
        raise ValueError("positive finite per-cycle multipliers required")
    if fraction in (0, 1):
        return fraction
    odds_log = (
        log(fraction)
        - log1p(-fraction)
        + cycles * (log(gain_target) - log(gain_background))
    )
    return (
        1 / (1 + exp(-odds_log))
        if odds_log >= 0
        else exp(odds_log) / (1 + exp(odds_log))
    )


def results():
    a, b = 0.99, 98.01
    repetition = [
        {
            "copies": r,
            "iid": majority_failure(0.01, r),
            "correlated": correlated_majority_failure(r, a, b),
        }
        for r in (1, 3, 5, 7)
    ]
    yields = [
        {
            "sites": n,
            "iid": object_yield_independent(0.01, n),
            "correlated": all_correct_beta_binomial(n, a, b),
            "lower": yield_bounds(0.01, n)[0],
            "upper": yield_bounds(0.01, n)[1],
        }
        for n in (1, 10, 100, 1000, 10000)
    ]
    curves = [
        {
            "sites": n,
            "iid": object_yield_independent(0.01, n),
            "correlated": all_correct_beta_binomial(n, a, b),
        }
        for n in range(0, 201, 5)
    ]
    observed = observed_defect_probability(0.01, 0.02, 0.1)
    return {
        "model_scope": "stipulated probabilities; no wet-lab fit or yield forecast",
        "repetition": repetition,
        "yield_examples": yields,
        "yield_curve": curves,
        "beta_model": {
            "alpha": a,
            "beta": b,
            "mean_p": a / (a + b),
            "site_correlation": 1 / (a + b + 1),
        },
        "five_copy_simulation": {
            "trials": 80000,
            "seed": 8,
            "estimate": simulate_repetition(0.02, 5, 80000, 8),
            "exact": majority_failure(0.02, 5),
        },
        "wilson": [
            {"defects": k, "sites": n, "low": wilson(k, n)[0], "high": wilson(k, n)[1]}
            for k, n in ((0, 20), (1, 100), (10, 1000))
        ],
        "amplification": {
            "initial_fraction": 0.1,
            "target_gain": 2.0,
            "background_gain": 1.8,
            "cycles": 20,
            "final_fraction": amplification_fraction(0.1, 2.0, 1.8, 20),
        },
        "measurement": {
            "true_p": 0.01,
            "false_positive": 0.02,
            "false_negative": 0.1,
            "observed_p": observed,
            "recovered_p": infer_defect_probability(observed, 0.02, 0.1),
        },
    }


TABLES = [
    (
        "repetition",
        ["Copies", "IID failure", "Correlated failure"],
        ["copies", "iid", "correlated"],
        "rrr",
    ),
    (
        "yield_examples",
        ["Sites", "IID yield", "Correlated yield", "Lower", "Upper"],
        ["sites", "iid", "correlated", "lower", "upper"],
        "rrrrr",
    ),
    (
        "wilson",
        ["Defects", "Sites", "Lower", "Upper"],
        ["defects", "sites", "low", "high"],
        "rrrr",
    ),
]
PLOTS = [("yield-plot", "yield_curve", "sites", ["iid", "correlated"])]
LISTINGS = [
    "all_correct_beta_binomial",
    "majority_failure",
    "observed_defect_probability",
    "infer_defect_probability",
    "wilson",
    "amplification_fraction",
]

if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
