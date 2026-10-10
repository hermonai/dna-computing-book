"""Assigned-rate strand-displacement models; not sequence or assay predictions."""

import json
import math
import numpy as np

LISTINGS = ["branch_chain", "first_passage", "conversion", "reporter"]
TABLES = [
    (
        "passage",
        [
            "m",
            "Detach (/s)",
            "Success",
            "Mean (s)",
            "Success mean (s)",
        ],
        ["m", "detach", "success", "mean", "conditional"],
        "rrrrr",
    ),
    (
        "batch",
        ["Time (s)", "Output (nM)", "Input left", "Gate left"],
        ["time", "output", "input", "gate"],
        "rrrr",
    ),
]
PLOTS = [
    ("commitment-plot", "commitment", "detach", ["short", "long"]),
    ("leak-plot", "leak", "time", ["present", "blank"]),
]


def nonnegative(*values):
    if any(not math.isfinite(x) or x < 0 for x in values):
        raise ValueError("finite nonnegative parameters required")


def branch_chain(m, forward=2.0, backward=2.0, detach=1.0):
    """Row generator on j=0..m-1; product and detached are absorbing exits."""
    nonnegative(forward, backward, detach)
    if type(m) is not int or m < 1 or forward == 0:
        raise ValueError(
            "positive integer length and positive forward rate required"
        )
    q = np.zeros((m, m))
    product_exit = np.zeros(m)
    for j in range(m):
        if j + 1 < m:
            q[j, j + 1] = forward
        else:
            product_exit[j] = forward
        if j:
            q[j, j - 1] = backward
        q[j, j] = -forward - (backward if j else detach)
    return q, product_exit


def first_passage(m, forward=2.0, backward=2.0, detach=1.0):
    q, exit_rate = branch_chain(m, forward, backward, detach)
    success = np.linalg.solve(-q, exit_rate)
    mean = np.linalg.solve(-q, np.ones(m))
    success_weighted_time = np.linalg.solve(-q, success)
    return (
        float(success[0]),
        float(mean[0]),
        float(success_weighted_time[0] / success[0]),
    )


def conversion(input0, gate0, rate, time):
    """Exact irreversible I+G -> W+O extent, nM and seconds; no leak."""
    nonnegative(input0, gate0, rate, time)
    low, high = sorted((input0, gate0))
    if low == 0 or rate == 0 or time == 0:
        return 0.0
    gap = high - low
    if gap == 0:
        z = rate * low * time
        fraction = z / (1 + z) if z < 1 else 1 - 1 / (1 + z)
        return low * fraction
    gain = -math.expm1(-rate * gap * time)
    return low * gain / (gap / high + (low / high) * gain)


def reporter(time, input_hazard=0.01, leak_hazard=0.001):
    """Normalized converted gate; excess-input approximation, not finite-input batch."""
    nonnegative(time, input_hazard, leak_hazard)
    present = -math.expm1(-(input_hazard + leak_hazard) * time)
    blank = -math.expm1(-leak_hazard * time)
    return present, blank


def results():
    passage = []
    for m in (1, 4, 8):
        p, t, tc = first_passage(m)
        passage.append(
            dict(
                m=m,
                detach=1,
                success=round(p, 6),
                mean=round(t, 6),
                conditional=round(tc, 6),
            )
        )
    return {
        "passage": passage,
        "batch": [
            dict(
                time=t,
                output=round(conversion(100, 100, 0.0001, t), 6),
                input=round(100 - conversion(100, 100, 0.0001, t), 6),
                gate=round(100 - conversion(100, 100, 0.0001, t), 6),
            )
            for t in (0, 10, 50, 100, 500)
        ],
        "commitment": [
            dict(
                detach=d / 20,
                short=first_passage(4, detach=d / 20)[0],
                long=first_passage(12, detach=d / 20)[0],
            )
            for d in range(81)
        ],
        "leak": [
            dict(time=t, present=reporter(t)[0], blank=reporter(t)[1])
            for t in range(0, 1001, 10)
        ],
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
