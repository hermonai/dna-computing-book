"""Finite CRN teaching reference; no sequence compiler or fitted chemistry."""

import json
import math
from dataclasses import dataclass
import numpy as np

LISTINGS = [
    "network",
    "propensities",
    "fire",
    "completion_moments",
    "shared_fuel",
]
TABLES = [
    (
        "completion",
        ["A", "B", "Mean (s)", "SD (s)"],
        ["a", "b", "mean", "sd"],
        "rrrr",
    ),
    (
        "fuel",
        ["Time (s)", "F", "Y", "Z"],
        ["time", "fuel", "y", "z"],
        "rrrr",
    ),
]
PLOTS = [("tail-plot", "tail", "time", ["ode", "path"])]


@dataclass(frozen=True)
class Network:
    reactants: np.ndarray
    products: np.ndarray
    rates: np.ndarray

    @property
    def change(self):
        return self.products - self.reactants


def network(reactants, products, rates):
    """Rows are species, columns are reactions; own immutable input copies."""
    r, p = np.asarray(reactants), np.asarray(products)
    k = np.asarray(rates, dtype=float)
    if r.ndim != 2 or p.shape != r.shape or 0 in r.shape:
        raise ValueError(
            "matching nonempty species-by-reaction arrays required"
        )
    if any(a.dtype.kind not in "iu" or (a < 0).any() for a in (r, p)):
        raise ValueError("stoichiometry must be nonnegative integers")
    if max(int(r.max()), int(p.max())) > 100:
        raise ValueError("teaching reference limits coefficients to 100")
    if (
        k.shape != (r.shape[1],)
        or not np.isfinite(k).all()
        or (k < 0).any()
    ):
        raise ValueError(
            "one finite nonnegative rate per reaction required"
        )
    arrays = (r.astype(np.int64), p.astype(np.int64), k.copy())
    for a in arrays:
        a.setflags(write=False)
    return Network(*arrays)


def state_vector(crn, state, integer=False):
    x = np.asarray(state)
    if x.shape != (crn.reactants.shape[0],):
        raise ValueError("one state entry per species required")
    if integer and (x.dtype.kind not in "iu" or (x > 10**9).any()):
        raise ValueError("integer counts from 0 to 10**9 required")
    if not np.isfinite(x).all() or (x < 0).any():
        raise ValueError("finite nonnegative state required")
    return x.astype(np.int64 if integer else float)


def drift(crn, concentration):
    x = state_vector(crn, concentration)
    flux = crn.rates * np.prod(x[:, None] ** crn.reactants, axis=0)
    return crn.change @ flux


def propensities(crn, counts, omega=1.0):
    """Macroscopic k convention: falling factorials, no factorial divisor."""
    n = state_vector(crn, counts, integer=True)
    if not math.isfinite(omega) or omega <= 0:
        raise ValueError(
            "positive finite count/concentration scale required"
        )
    hazards = []
    for j, rate in enumerate(crn.rates):
        factors = 1
        for count, required in zip(n, crn.reactants[:, j]):
            if count < required:
                factors = 0
                break
            for offset in range(int(required)):
                factors *= int(count) - offset
        order = int(crn.reactants[:, j].sum())
        hazards.append(rate * factors / omega ** (order - 1))
    answer = np.array(hazards)
    if not np.isfinite(answer).all():
        raise ValueError("hazard overflow: rescale the model")
    return answer


def fire(crn, counts, reaction):
    n = state_vector(crn, counts, integer=True)
    if type(reaction) is not int or not 0 <= reaction < len(crn.rates):
        raise ValueError("invalid reaction index")
    if (n < crn.reactants[:, reaction]).any():
        raise ValueError("reaction is not stoichiometrically enabled")
    return n + crn.change[:, reaction]


def completion_moments(a, b, k=1.0, omega=1.0):
    """A+B -> W: sum independent holding-time means and variances."""
    if any(type(n) is not int or n < 0 for n in (a, b)):
        raise ValueError("nonnegative integer inputs required")
    if not all(math.isfinite(v) and v > 0 for v in (k, omega)):
        raise ValueError("positive finite k and omega required")
    means = [omega / (k * (a - j) * (b - j)) for j in range(min(a, b))]
    return math.fsum(means), math.fsum(x * x for x in means)


def annihilation_path(a, b, rng, k=1.0, omega=1.0):
    completion_moments(
        a, b, k, omega
    )  # validate before drawing randomness
    time = 0.0
    path = [(time, a, b)]
    while a and b:
        time += rng.exponential(omega / (k * a * b))
        a, b = a - 1, b - 1
        path.append((float(time), a, b))
    return path


def shared_fuel(f0, alpha, beta, time):
    """Fixed catalysts: F -> Y at hazard alpha, F -> Z at hazard beta."""
    if not all(
        math.isfinite(v) and v >= 0 for v in (f0, alpha, beta, time)
    ):
        raise ValueError("finite nonnegative inputs required")
    total = alpha + beta
    if total == 0:
        return f0, 0.0, 0.0
    used = f0 * -math.expm1(-total * time)
    return (
        f0 * math.exp(-total * time),
        used * alpha / total,
        used * beta / total,
    )


def results():
    path = annihilation_path(4, 4, np.random.default_rng(20))
    tail = []
    sample_times = sorted(
        set(np.linspace(0, 4, 81)) | {p[0] for p in path}
    )
    for time in sample_times:
        state = next((p for p in reversed(path) if p[0] <= time), path[0])
        tail.append(
            dict(time=float(time), ode=4 / (1 + 4 * time), path=state[1])
        )
    moments = []
    for a, b in [(1, 1), (4, 4), (8, 8), (8, 4)]:
        mean, variance = completion_moments(a, b)
        moments.append(
            dict(
                a=a,
                b=b,
                mean=round(mean, 6),
                sd=round(math.sqrt(variance), 6),
            )
        )
    fuel = []
    for time in [0, 1, 5, 10, 50]:
        f, y, z = shared_fuel(100, 0.1, 0.3, time)
        fuel.append(
            dict(
                time=time,
                fuel=float(f"{f:.6g}"),
                y=round(y, 6),
                z=round(z, 6),
            )
        )
    return dict(
        completion=moments,
        fuel=fuel,
        tail=tail,
        sample_path=[list(p) for p in path],
    )


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
