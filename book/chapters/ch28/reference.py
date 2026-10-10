"""DNAD-28: strict reversible kinetics, direct SSA and independent finite-copy law."""

from dataclasses import dataclass
import json
import math
import random
import statistics

N_A = 6.02214076e23


def real(value, name, positive=False):
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError(f"Finite real {name} required")
    if value <= 0 if positive else value < 0:
        raise ValueError(f"Invalid {name} domain")
    return float(value)


def count(value, name):
    if type(value) is not int or value < 0:
        raise ValueError(f"Nonnegative exact integer {name} required")
    return value


def parameters(a, b, kf, kr):
    return tuple(real(v, n) for v, n in zip((a, b, kf, kr), ("a", "b", "kf", "kr")))


def ode_rhs(a, b, kf, kr):
    a, b, kf, kr = parameters(a, b, kf, kr)
    flux = kf * a - kr * b
    if not math.isfinite(flux):
        raise ValueError("Nonfinite reaction flux")
    return -flux, flux


def analytic_a(t, a0, b0, kf, kr):
    t = real(t, "time")
    a0, b0, kf, kr = parameters(a0, b0, kf, kr)
    rate = kf + kr
    if not math.isfinite(rate):
        raise ValueError("Nonfinite total rate")
    if rate == 0:
        return a0
    # Transition probability form avoids total*rate and preserves zero-rate cases.
    change = -math.expm1(-rate * t)
    result = a0 * (1 - kf / rate * change) + b0 * (kr / rate * change)
    if not math.isfinite(result):
        raise ValueError("Nonfinite analytic population")
    return result


def euler(a0, b0, kf, kr, dt, steps):
    a, b, kf, kr = parameters(a0, b0, kf, kr)
    dt = real(dt, "dt", True)
    steps = count(steps, "steps")
    # Transition matrix must be nonnegative for every nonnegative initial state.
    if dt * max(kf, kr) > 1:
        raise ValueError("Euler step violates universal positivity bound")
    out = [(0.0, a, b)]
    for i in range(steps):
        da, db = ode_rhs(a, b, kf, kr)
        a, b = a + dt * da, b + dt * db
        t = (i + 1) * dt
        if not all(math.isfinite(v) for v in (a, b, t)) or min(a, b) < 0:
            raise ValueError("Nonfinite or negative Euler result; no clipping")
        out.append((t, a, b))
    return tuple(out)


def propensities(A, B, kf, kr):
    A, B = count(A, "A"), count(B, "B")
    kf, kr = real(kf, "kf"), real(kr, "kr")
    values = (kf * A, kr * B)
    if not all(math.isfinite(v) for v in values) or not math.isfinite(sum(values)):
        raise ValueError("Nonfinite total propensity")
    return values


def event_draw(af, ar, u_time, u_rule):
    """Two uniforms with explicit endpoint policy; no biased epsilon clamp."""
    af, ar = real(af, "af"), real(ar, "ar")
    total = af + ar
    if not math.isfinite(total) or total <= 0:
        raise ValueError("Finite positive total propensity required")
    if type(u_time) not in (int, float) or not 0 < u_time < 1:
        raise ValueError("Waiting-time uniform must be strictly inside (0,1)")
    if type(u_rule) not in (int, float) or not 0 <= u_rule < 1:
        raise ValueError("Reaction uniform must lie in [0,1)")
    return -math.log(u_time) / total, 0 if u_rule * total < af else 1


@dataclass(frozen=True)
class Trajectory:
    events: tuple
    horizon: float
    simulated_until: float
    complete: bool
    status: str


def ssa(A0, B0, kf, kr, horizon, seed=28, event_limit=100000):
    """Direct method; interrupted paths may not be extrapolated to the horizon."""
    A, B = count(A0, "A0"), count(B0, "B0")
    kf, kr = real(kf, "kf"), real(kr, "kr")
    horizon = real(horizon, "horizon")
    event_limit = count(event_limit, "event limit")
    if type(seed) is not int:
        raise ValueError("Exact integer seed required")
    rng = random.Random(seed)
    t = 0.0
    events = [(t, A, B)]
    while t < horizon:
        af, ar = propensities(A, B, kf, kr)
        if af + ar == 0:
            return Trajectory(tuple(events), horizon, horizon, True, "absorbing")
        if len(events) - 1 == event_limit:
            return Trajectory(
                tuple(events), horizon, t, False, "event_budget_exhausted"
            )
        u = rng.random()
        while u == 0:  # redraw an excluded endpoint rather than clamp it
            u = rng.random()
        tau, which = event_draw(af, ar, u, rng.random())
        next_time = t + tau
        if next_time > horizon:
            break
        if not math.isfinite(next_time) or next_time <= t:
            raise ValueError("Floating event clock cannot advance")
        A, B = (A - 1, B + 1) if which == 0 else (A + 1, B - 1)
        if min(A, B) < 0:
            raise AssertionError("Propensity selected disabled reaction")
        t = next_time
        events.append((t, A, B))
    return Trajectory(tuple(events), horizon, horizon, True, "horizon_completed")


def sample_at(trajectory, time):
    time = real(time, "query time")
    if not isinstance(trajectory, Trajectory) or time > trajectory.simulated_until:
        raise ValueError("Query exceeds simulated interval")
    value = trajectory.events[0]
    for event in trajectory.events:
        if event[0] > time:
            break
        value = event
    return value[1:]


def exact_moments(A0, B0, kf, kr, time):
    """Independent two-state molecule law; two binomial groups, not always one."""
    A0, B0 = count(A0, "A0"), count(B0, "B0")
    kf, kr = real(kf, "kf"), real(kr, "kr")
    time = real(time, "time")
    rate = kf + kr
    if not math.isfinite(rate):
        raise ValueError("Nonfinite total rate")
    if rate == 0:
        return float(A0), 0.0
    change = -math.expm1(-rate * time)
    pAA = 1 - kf / rate * change
    pBA = kr / rate * change
    mean = A0 * pAA + B0 * pBA
    variance = A0 * pAA * (1 - pAA) + B0 * pBA * (1 - pBA)
    return mean, variance


def ensemble(n, A0, B0, kf, kr, time, seed=2800):
    n = count(n, "trajectory count")
    if n < 2:
        raise ValueError("At least two independent-seed trajectories required")
    if type(seed) is not int:
        raise ValueError("Exact integer seed required")
    values = [sample_at(ssa(A0, B0, kf, kr, time, seed + i), time)[0] for i in range(n)]
    return {
        "n": n,
        "mean": statistics.mean(values),
        "sample_variance": statistics.variance(values),
        "mean_se": statistics.stdev(values) / math.sqrt(n),
    }


def bimolecular_propensity(k, A, B, volume_liters, identical=False):
    """Molar event law k*a*b, or k*a**2 for 2A; latter has no extra 1/2."""
    k = real(k, "molar bimolecular k")
    A, B = count(A, "A"), count(B, "B")
    volume = real(volume_liters, "volume", True)
    if type(identical) is not bool or (identical and A != B):
        raise ValueError(
            "Identical-reactant mode requires the same species count twice"
        )
    omega = N_A * volume
    if not math.isfinite(omega) or omega == 0:
        raise ValueError("Finite positive concentration-to-copy scale required")
    result = k / omega * (A * (A - 1) if identical else A * B)
    if not math.isfinite(result):
        raise ValueError("Nonfinite propensity")
    return result


def results():
    A0, B0, kf, kr, T = 100, 0, 0.4, 0.1, 5.0
    exact, variance = exact_moments(A0, B0, kf, kr, T)
    summary = ensemble(2000, A0, B0, kf, kr, T)
    tr = ssa(A0, B0, kf, kr, T)
    rows = []
    for dt in (0.1, 0.05, 0.025, 0.0125):
        last = euler(A0, B0, kf, kr, dt, round(T / dt))[-1][1]
        rows.append({"dt": dt, "A": last, "error": abs(last - exact)})
    p = exact / A0
    distribution = [
        {"A": j, "probability": math.comb(A0, j) * p**j * (1 - p) ** (A0 - j)}
        for j in range(A0 + 1)
    ]
    path = [{"time": t, "A": a} for t, a, _ in tr.events]
    if path[-1]["time"] < T:
        path.append({"time": T, "A": sample_at(tr, T)[0]})
    curve = [
        {"time": i / 10, "A": analytic_a(i / 10, A0, B0, kf, kr)} for i in range(51)
    ]
    return {
        "analytic_mean": exact,
        "analytic_variance": variance,
        "ensemble": summary,
        "ensemble_standardized_mean_error": (summary["mean"] - exact)
        / math.sqrt(variance / summary["n"]),
        "ssa_events": len(tr.events) - 1,
        "ssa_final": sample_at(tr, T),
        "ssa_status": tr.status,
        "conserved": all(a + b == 100 for _, a, b in tr.events),
        "euler": rows,
        "path": path,
        "curve": curve,
        "distribution": distribution,
        "tiny_volume_example": bimolecular_propensity(1e6, 10, 20, 1e-15),
        "scope": "declared well-mixed first-order CTMC/ODE and unit oracle; not experimentally calibrated DNA kinetics",
    }


TABLES = [
    ("euler", ["Step", "Terminal A", "Absolute error"], ["dt", "A", "error"], "rrr")
]
PLOTS = [
    ("ode-curve", "curve", "time", ["A"]),
    ("ssa-path", "path", "time", ["A"]),
    ("exact-distribution", "distribution", "A", ["probability"]),
]
LISTINGS = ["euler", "event_draw", "ssa", "exact_moments", "bimolecular_propensity"]

if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
