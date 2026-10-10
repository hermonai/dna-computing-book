"""Assigned-rate circuit reference, not a sequence-level DNA simulator."""

import itertools
import json
import math

LISTINGS = [
    "restored",
    "gate_bounds",
    "read_window",
    "race_output",
    "feedback",
]
TABLES = [
    (
        "truth",
        ["Gate", "Inputs", "Minimum", "Maximum", "Bit"],
        ["gate", "bits", "lo", "hi", "answer"],
        "llrrr",
    ),
    (
        "race",
        ["Capture rate", "Output at 50 s", "Limit"],
        ["capture", "output", "limit"],
        "rrr",
    ),
    (
        "loads",
        ["Receivers", "Free input", "Output at 6 s"],
        ["receivers", "free", "output"],
        "rrr",
    ),
]
PLOTS = [
    ("transfer-plot", "transfer", "input", ["nominal", "low", "high"]),
    ("feedback-plot", "growth", "time", ["seed1", "seed2", "zero"]),
]


def nonnegative(*values):
    if not all(math.isfinite(v) and v >= 0 for v in values):
        raise ValueError("finite nonnegative values required")


def restored(signal, threshold, time, fuel=1.0, rate=1.0, leak=0.0):
    """Instant completed capture, then fixed residual catalyst."""
    nonnegative(signal, threshold, time, fuel, rate, leak)
    residual = max(signal - threshold, 0.0)
    return fuel * -math.expm1(-(rate * residual + leak) * time)


def gate_bounds(bits, kind, time=6.0, tolerance=0.05):
    """Independent input boxes and threshold/leak uncertainty."""
    if kind not in ("OR", "AND") or len(bits) != 2:
        raise ValueError("two-input OR or AND required")
    if any(type(b) is not int or b not in (0, 1) for b in bits):
        raise ValueError("bits must be integers 0 or 1")
    nonnegative(time, tolerance)
    theta = 0.3 if kind == "OR" else 1.3
    if tolerance > theta:
        raise ValueError("threshold uncertainty crosses zero")
    boxes = [(0.0, 0.1) if b == 0 else (0.9, 1.1) for b in bits]
    lo = restored(sum(b[0] for b in boxes), theta + tolerance, time)
    hi = restored(
        sum(b[1] for b in boxes), theta - tolerance, time, leak=0.001
    )
    return lo, hi


def read_window(
    residual, low=0.1, high=0.9, leak=0.001, fuel=1.0, rate=1.0
):
    """Guaranteed ON uses zero leak; worst OFF uses maximum leak."""
    nonnegative(residual, low, high, leak, fuel, rate)
    if not (0 < low < high < fuel and residual > 0 and rate > 0):
        raise ValueError(
            "strictly separated bands and positive drive required"
        )
    earliest = -math.log1p(-high / fuel) / (rate * residual)
    latest = math.inf if leak == 0 else -math.log1p(-low / fuel) / leak
    return earliest, latest


def race_output(signal, sink, capture, release, time, fuel=1.0):
    """Concurrent X+Q capture and X-catalysed F->Y; sink > signal."""
    nonnegative(signal, sink, capture, release, time, fuel)
    if sink <= signal or capture == 0:
        raise ValueError(
            "this closed form requires sink > signal and capture > 0"
        )
    delta = sink - signal
    exposure = (
        math.log1p(signal * -math.expm1(-capture * delta * time) / delta)
        / capture
    )
    return fuel * -math.expm1(-release * exposure)


def loaded_signal(total, loads, kd):
    """Rapid equilibrium with undepleted loads: a restricted load model."""
    nonnegative(total, kd, *loads)
    if kd == 0:
        raise ValueError("positive dissociation constant required")
    return total / (1 + math.fsum(loads) / kd)


def feedback(seed, total, rate, time):
    """Y+F -> 2Y, with total=Y+F; closed-system logistic solution."""
    nonnegative(seed, total, rate, time)
    if seed > total:
        raise ValueError("seed cannot exceed total material")
    if seed == 0:
        return 0.0
    return total / (
        1 + (total / seed - 1) * math.exp(-rate * total * time)
    )


def results():
    truth = []
    for kind in ("OR", "AND"):
        for bits in itertools.product((0, 1), repeat=2):
            lo, hi = gate_bounds(bits, kind)
            answer = int(any(bits) if kind == "OR" else all(bits))
            truth.append(
                dict(
                    gate=kind,
                    bits="".join(map(str, bits)),
                    lo=round(lo, 6),
                    hi=round(hi, 6),
                    answer=answer,
                )
            )
    return dict(
        truth=truth,
        race=[
            dict(
                capture=q,
                output=round(race_output(0.2, 0.3, q, 1, 50), 6),
                limit=round(-math.expm1(-math.log(3) / q), 6),
            )
            for q in (1, 10, 100)
        ],
        loads=[
            dict(
                receivers=n,
                free=round(loaded_signal(0.5, [1.0] * n, 1), 6),
                output=round(
                    restored(loaded_signal(0.5, [1.0] * n, 1), 0, 6), 6
                ),
            )
            for n in (0, 1, 3, 9)
        ],
        transfer=[
            dict(
                input=s / 50,
                nominal=restored(s / 50, 1.3, 6),
                low=restored(s / 50, 1.35, 6),
                high=restored(s / 50, 1.25, 6, leak=0.001),
            )
            for s in range(111)
        ],
        growth=[
            dict(
                time=t / 2,
                seed1=feedback(0.1, 1, 1, t / 2),
                seed2=feedback(0.001, 1, 1, t / 2),
                zero=0.0,
            )
            for t in range(25)
        ],
    )


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
