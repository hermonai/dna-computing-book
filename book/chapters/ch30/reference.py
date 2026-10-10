"""DNAD-30: stipulated regulatory dynamics, not calibrated biology."""

from dataclasses import dataclass
import json
import math
import random


def nonnegative(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(name)
    if not math.isfinite(value) or value < 0:
        raise ValueError(name)
    return float(value)


def hill_activation(x, K=1.0, n=2.0):
    """Stable phenomenological occupancy; n is not a counted binding stoichiometry."""
    x, K, n = [nonnegative(v, k) for v, k in [(x, "x"), (K, "K"), (n, "n")]]
    if K == 0 or n == 0:
        raise ValueError("positive K and n required")
    if x == 0:
        return 0.0
    z = n * (math.log(x) - math.log(K))
    return 1 / (1 + math.exp(-z)) if z >= 0 else math.exp(z) / (1 + math.exp(z))


def hill_repression(x, K=1.0, n=2.0):
    # Evaluate independently to retain tiny repression at very high x.
    x, K, n = [nonnegative(v, k) for v, k in [(x, "x"), (K, "K"), (n, "n")]]
    if K == 0 or n == 0:
        raise ValueError("positive K and n required")
    if x == 0:
        return 1.0
    z = n * (math.log(x) - math.log(K))
    return math.exp(-z) / (1 + math.exp(-z)) if z >= 0 else 1 / (1 + math.exp(z))


def allele_rates(cis, accessibility, factor, K=1.0):
    """Two stipulated allele rates: shared trans concentration, separate cis context."""
    if len(cis) != 2 or len(accessibility) != 2:
        raise ValueError("two alleles required")
    c = [nonnegative(v, "cis") for v in cis]
    q = [nonnegative(v, "accessibility") for v in accessibility]
    if max(q) > 1:
        raise ValueError("accessibility in [0,1]")
    occupancy = hill_activation(factor, K, n=1)
    return tuple(c[i] * q[i] * occupancy for i in range(2))


@dataclass(frozen=True)
class Genotype:
    # Dimensionless maximum production alpha = p_max/(delta K).
    a_cis: float = 3.0
    b_cis: float = 3.0

    def __post_init__(self):
        nonnegative(self.a_cis, "a_cis")
        nonnegative(self.b_cis, "b_cis")


def production(a, b, g=Genotype(), signal=1.0, intervene_a=None):
    a, b, signal = [
        nonnegative(v, k) for v, k in [(a, "a"), (b, "b"), (signal, "signal")]
    ]
    pa = g.a_cis * signal * hill_repression(b)
    if intervene_a is not None:
        pa = nonnegative(intervene_a, "A production intervention")
    pb = g.b_cis * hill_repression(a)
    if not all(math.isfinite(x) for x in (pa, pb)):
        raise ValueError("production overflow")
    return pa, pb


def rhs(a, b, g=Genotype(), signal=1.0, intervene_a=None):
    pa, pb = production(a, b, g, signal, intervene_a)
    return pa - a, pb - b


def euler_step(a, b, h, g=Genotype(), signal=1.0, intervene_a=None):
    """Simultaneous old-state update; positivity without numerical clipping."""
    h = nonnegative(h, "step")
    if not 0 < h <= 1:
        raise ValueError("dimensionless step in (0,1]")
    pa, pb = production(a, b, g, signal, intervene_a)
    result = ((1 - h) * a + h * pa, (1 - h) * b + h * pb)
    if not all(math.isfinite(v) and v >= 0 for v in result):
        raise ValueError("invalid numerical state")
    return result


def simulate(
    g=Genotype(), a0=0.11, b0=0.1, signal=1.0, dt=0.01, steps=6000, intervene_a=None
):
    a, b = nonnegative(a0, "a0"), nonnegative(b0, "b0")
    if type(steps) is not int or not 0 <= steps <= 100000:
        raise ValueError("bounded integer steps")
    if not 0 < nonnegative(dt, "dt") <= 1:
        raise ValueError("step in (0,1]")
    production(a, b, g, signal, intervene_a)
    out = [(0.0, a, b)]
    for i in range(steps):
        a, b = euler_step(a, b, dt, g, signal, intervene_a)
        out.append(((i + 1) * dt, a, b))
    return out


def fixed_points(alpha=3.0):
    """Exact asymmetric roots plus monotone-bisection symmetric root."""
    alpha = nonnegative(alpha, "alpha")
    if alpha > 100:
        raise ValueError("teaching fixed-point domain alpha<=100")
    low, high = 0.0, max(1.0, alpha)
    for _ in range(80):
        c = (low + high) / 2
        if c * (1 + c * c) < alpha:
            low = c
        else:
            high = c
    c = (low + high) / 2
    points = [(c, c)]
    if alpha > 2:
        large = (alpha + math.sqrt(alpha * alpha - 4)) / 2
        small = 1 / large
        points += [(large, small), (small, large)]
    return points


def eigenvalues(a, b, alpha=3.0):
    """Jacobian of the symmetric-parameter Hill-n=2 model, not arbitrary GRNs."""
    a, b, alpha = [nonnegative(v, "Jacobian") for v in (a, b, alpha)]
    da_db = -2 * alpha * b / (1 + b * b) ** 2
    db_da = -2 * alpha * a / (1 + a * a) ** 2
    coupling = math.sqrt(da_db * db_da)
    return (-1 - coupling, -1 + coupling)


def partition_counts(n, seed=30, probability=0.5):
    """Independent binomial allocation of N identical abstract molecules."""
    if type(n) is not int or not 0 <= n <= 100000:
        raise ValueError("bounded count")
    if type(seed) is not int:
        raise ValueError("integer seed")
    p = nonnegative(probability, "probability")
    if p > 1:
        raise ValueError("probability <=1")
    rng = random.Random(seed)
    left = sum(rng.random() < p for _ in range(n))
    return left, n - left


def partition_law(n=3, probability=0.5):
    if type(n) is not int or not 0 <= n <= 100:
        raise ValueError("bounded count")
    p = nonnegative(probability, "probability")
    if p > 1:
        raise ValueError("probability <=1")
    return tuple(math.comb(n, k) * p**k * (1 - p) ** (n - k) for k in range(n + 1))


def selection_mutation(p, w1, w0, mu=0.0, nu=0.0):
    """Haploid two-type frequency: reproduction, then bidirectional mutation."""
    p, w1, w0, mu, nu = [
        nonnegative(v, k)
        for v, k in [(p, "p"), (w1, "w1"), (w0, "w0"), (mu, "mu"), (nu, "nu")]
    ]
    if p > 1 or mu > 1 or nu > 1:
        raise ValueError("probabilities <=1")
    mean = p * w1 + (1 - p) * w0
    if mean <= 0:
        raise ValueError("positive mean reproductive weight")
    selected = p * w1 / mean
    return (1 - mu) * selected + nu * (1 - selected)


@dataclass(frozen=True)
class Cell:
    name: str
    parent: str | None
    time: float
    pseudotime: float


def lineage_edges(cells):
    """Validate ancestry independently of an inferred snapshot ordering."""
    cells = tuple(cells)
    names = [c.name for c in cells]
    if (
        not cells
        or len(names) != len(set(names))
        or any(not isinstance(n, str) or not n for n in names)
    ):
        raise ValueError("unique nonempty identities")
    lookup = {c.name: c for c in cells}
    edges = []
    for c in cells:
        nonnegative(c.time, "observed time")
        nonnegative(c.pseudotime, "pseudotime")
        if c.parent is not None:
            if c.parent not in lookup or lookup[c.parent].time >= c.time:
                raise ValueError("parent must precede child in observed time")
            edges.append((c.parent, c.name))
    return tuple(edges)


def results():
    g = Genotype()
    paths = [simulate(g), simulate(g, a0=0.1, b0=0.11), simulate(g, a0=0.1, b0=0.1)]
    knock = simulate(g, intervene_a=0)
    points = fixed_points()
    cells = (
        Cell("root", None, 0, 0.2),
        Cell("left", "root", 1, 0.9),
        Cell("right", "root", 1, 0.1),
    )
    history = [dict(generation=0, frequency=0.25)]
    for generation in range(1, 7):
        history.append(
            dict(
                generation=generation,
                frequency=selection_mutation(history[-1]["frequency"], 2, 1),
            )
        )
    return {
        "alleles": [
            dict(case=k, a=v[0], b=v[1])
            for k, v in [
                ("base", allele_rates((1, 1), (1, 1), 1)),
                ("cis A", allele_rates((0.5, 1), (1, 1), 1)),
                ("trans", allele_rates((1, 1), (1, 1), 3)),
                ("closed A", allele_rates((1, 1), (0, 1), 1)),
            ]
        ],
        "fixed-points": [
            dict(a=a, b=b, low=eigenvalues(a, b)[0], high=eigenvalues(a, b)[1])
            for a, b in points
        ],
        "terminal": [
            dict(case=k, a=p[-1][1], b=p[-1][2])
            for k, p in zip(
                ["A bias", "B bias", "symmetric", "A production off"], paths + [knock]
            )
        ],
        "refinement": [
            dict(
                h=h,
                a=simulate(dt=h, steps=round(10 / h))[-1][1],
                b=simulate(dt=h, steps=round(10 / h))[-1][2],
            )
            for h in [0.04, 0.02, 0.01, 0.005]
        ],
        "trajectory": [dict(t=t, a=a, b=b) for t, a, b in paths[0][::20]],
        "partition": [dict(k=k, probability=p) for k, p in enumerate(partition_law())],
        "selection": history,
        "lineage": lineage_edges(cells),
        "pseudotime_order": [c.name for c in sorted(cells, key=lambda c: c.pseudotime)],
        "production_off_a": knock[-1][1],
        "initial_loss_exact_a": 0.11 * math.exp(-60),
    }


TABLES = [
    (
        "alleles",
        ["Perturbation", "Allele A rate", "Allele B rate"],
        ["case", "a", "b"],
        "lrr",
    ),
    (
        "fixed-points",
        ["$a$", "$b$", "$\\lambda_-$", "$\\lambda_+$"],
        ["a", "b", "low", "high"],
        "rrrr",
    ),
    (
        "terminal",
        ["Initial/context choice", "$a(60)$", "$b(60)$"],
        ["case", "a", "b"],
        "lrr",
    ),
    ("refinement", ["$h$", "$a(10)$", "$b(10)$"], ["h", "a", "b"], "rrr"),
    ("partition", ["Daughter A count", "Probability"], ["k", "probability"], "rr"),
    (
        "selection",
        ["Generation", "Type-1 frequency"],
        ["generation", "frequency"],
        "rr",
    ),
]
PLOTS = [("regulation-path", "trajectory", "t", ["a", "b"])]
LISTINGS = [
    "allele_rates",
    "euler_step",
    "fixed_points",
    "lineage_edges",
    "selection_mutation",
]

if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
