"""Closed, well-mixed A+B <-> D: teaching models, not measured kinetics."""

import json
import math
import random

AVOGADRO = 6.02214076e23


def nonnegative(*values):
    if any(
        isinstance(v, bool)
        or not isinstance(v, (int, float))
        or not math.isfinite(v)
        or v < 0
        for v in values
    ):
        raise ValueError("finite nonnegative numbers required")


def fluxes(duplex, a_total, b_total, kon, koff):
    nonnegative(duplex, a_total, b_total, kon, koff)
    if duplex > min(a_total, b_total):
        raise ValueError("duplex exceeds inventory")
    return kon * (a_total - duplex) * (b_total - duplex), koff * duplex


def equal_pool_exact(t, total, kon, koff):
    """Equal totals, initially no duplex, strictly positive rates."""
    nonnegative(t, total, kon, koff)
    if kon == 0 or koff == 0:
        raise ValueError("positive rates required by this closed form")
    if total == 0:
        return 0.0
    kd = koff / kon
    gap = math.sqrt(kd * (4 * total + kd))
    upper = (2 * total + kd + gap) / 2
    lower = total * (total / upper)
    q = math.exp(-kon * gap * t)
    return lower * (-math.expm1(-kon * gap * t)) / (1 - lower / upper * q)


def rk4(t_end, dt, a_total, b_total, kon, koff, initial=0.0):
    """Fixed maximum step; reject invalid stages rather than clipping."""
    nonnegative(t_end, dt)
    if dt == 0:
        raise ValueError("positive step required")

    def f(x):
        on, off = fluxes(x, a_total, b_total, kon, koff)
        return on - off

    f(initial)
    t, x = 0.0, initial
    while t < t_end:
        step = min(dt, t_end - t)
        if t + step == t:
            raise ValueError("time step below floating-point resolution")
        k1 = f(x)
        k2 = f(x + step * k1 / 2)
        k3 = f(x + step * k2 / 2)
        k4 = f(x + step * k3)
        x += step * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        f(x)
        t += step
    return x


def propensities(duplex, a_total, b_total, volume_l, kon, koff):
    """Counts -> events/s. A and B are distinct species, not 2A."""
    for n in (duplex, a_total, b_total):
        if type(n) is not int or n < 0:
            raise ValueError("nonnegative integer counts required")
    nonnegative(volume_l, kon, koff)
    if volume_l == 0 or duplex > min(a_total, b_total):
        raise ValueError("positive volume and conserved inventory required")
    omega = AVOGADRO * volume_l
    return kon / omega * (a_total - duplex) * (
        b_total - duplex
    ), koff * duplex


def ssa(
    a_total,
    b_total,
    volume_l,
    kon,
    koff,
    horizon,
    seed=0,
    initial=0,
    max_events=100000,
):
    """Direct SSA; event states are right-continuous; horizon is not an event."""
    nonnegative(horizon)
    propensities(initial, a_total, b_total, volume_l, kon, koff)
    if type(max_events) is not int or max_events <= 0:
        raise ValueError("positive event budget required")
    rng = random.Random(seed)
    t, d = 0.0, initial
    events = [(t, d)]
    while t < horizon:
        on, off = propensities(d, a_total, b_total, volume_l, kon, koff)
        rate = on + off
        if rate == 0:
            break
        u = rng.random()
        while u == 0:
            u = rng.random()
        future = t - math.log(u) / rate
        if future > horizon:
            break
        if future <= t:
            raise ValueError("event time below floating-point resolution")
        if len(events) - 1 >= max_events:
            raise RuntimeError(
                "event budget exhausted; no silent truncation"
            )
        t = future
        d += 1 if rng.random() * rate < on else -1
        events.append((t, d))
    return events


def stationary(a_total, b_total, volume_l, kon, koff):
    """Normalized birth-death equilibrium by detailed balance, in log space."""
    propensities(0, a_total, b_total, volume_l, kon, koff)
    if kon == 0 or koff == 0:
        raise ValueError("positive rates required")
    logs = [0.0]
    for d in range(min(a_total, b_total)):
        birth, _ = propensities(d, a_total, b_total, volume_l, kon, koff)
        _, death = propensities(
            d + 1, a_total, b_total, volume_l, kon, koff
        )
        logs.append(logs[-1] + math.log(birth) - math.log(death))
    peak = max(logs)
    weights = [math.exp(v - peak) for v in logs]
    total = math.fsum(weights)
    return [w / total for w in weights]


def results():
    total, kon, koff = 100e-9, 1e6, 0.005
    volume = 20 / (AVOGADRO * total)
    p = stationary(20, 20, volume, kon, koff)
    mean = math.fsum(i * w for i, w in enumerate(p))
    variance = math.fsum((i - mean) ** 2 * w for i, w in enumerate(p))
    trace = ssa(20, 20, volume, kon, koff, 120, seed=1701)
    return {
        "assumptions": "illustrative rates; closed well-mixed distinct species",
        "kon_m_inv_s_inv": kon,
        "koff_s_inv": koff,
        "total_m": total,
        "volume_l": volume,
        "relaxation_s": 1
        / (kon * math.sqrt((koff / kon) * (4 * total + koff / kon))),
        "curves": [
            {
                "t": t,
                "normal_nm": equal_pool_exact(t, total, kon, koff) * 1e9,
                "fast_nm": equal_pool_exact(t, total, 10 * kon, 10 * koff)
                * 1e9,
            }
            for t in (i / 5 for i in range(601))
        ],
        "convergence": [
            {
                "step": dt,
                "error_nm": abs(
                    rk4(20, dt, total, total, kon, koff)
                    - equal_pool_exact(20, total, kon, koff)
                )
                * 1e9,
            }
            for dt in [2, 1, 0.5, 0.25]
        ],
        "stationary": p,
        "mean_count": mean,
        "variance_count": variance,
        "stationary_mean_nm": mean / 20 * 100,
        "trace": trace,
        "one_pair_bound_probability": stationary(
            1, 1, 1 / (AVOGADRO * total), kon, koff
        )[1],
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
