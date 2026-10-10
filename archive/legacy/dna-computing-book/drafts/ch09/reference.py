"""Chapter 9: explicit teaching models, not a PCR assay simulator."""

import math


def integer(value, name):
    if type(value) is not int or value < 0:
        raise ValueError(name + " must be a nonnegative integer")


def nonnegative(*values):
    if any(not math.isfinite(v) or v < 0 for v in values):
        raise ValueError("finite nonnegative values required")


def efficiency(value):
    nonnegative(value)
    if value > 1:
        raise ValueError("efficiency must be in [0,1]")


def primer_pair(top, a, b, lf, lr):
    """top is 5'->3'; [a,b) is a nonoverlapping-primer interval."""
    for value in (a, b, lf, lr):
        integer(value, "coordinate/length")
    if not top or set(top) - set("ACGT"):
        raise ValueError("canonical uppercase DNA required")
    if not (0 <= a < b <= len(top) and 0 < lf and 0 < lr):
        raise ValueError("invalid interval or primer length")
    if lf + lr > b - a:
        raise ValueError("this model requires nonoverlapping primers")
    rc = top[b - lr : b].translate(str.maketrans("ACGT", "TGCA"))[::-1]
    return top[a : a + lf], rc, top[a:b]


def lineage(cycles):
    """Counts after extension; one long parental duplex initially."""
    integer(cycles, "cycles")
    original, one_end, exact = 2, 0, 0
    rows = [
        dict(
            cycle=0,
            original=2,
            one_end=0,
            exact=0,
            duplexes=1,
            exact_duplexes=0,
        )
    ]
    for n in range(1, cycles + 1):
        exact_duplexes = exact
        one_end, exact = one_end + original, 2 * exact + one_end
        rows.append(
            dict(
                cycle=n,
                original=original,
                one_end=one_end,
                exact=exact,
                duplexes=2**n,
                exact_duplexes=exact_duplexes,
            )
        )
    return rows


def amplify(initial, efficiencies):
    """Mature-target equivalent counts; no resource limitation."""
    nonnegative(initial)
    trace = [float(initial)]
    for e in efficiencies:
        efficiency(e)
        value = trace[-1] * (1 + e)
        if not math.isfinite(value):
            raise ValueError("population overflow")
        trace.append(value)
    return trace


def budgeted(initial, efficiencies, forward, reverse, dntp, length, lf, lr):
    """Balanced-copy mean model. One added duplex uses both primers."""
    nonnegative(initial, forward, reverse, dntp)
    for v in (length, lf, lr):
        integer(v, "length")
    if not (lf > 0 and lr > 0 and lf + lr <= length):
        raise ValueError("positive nonoverlapping primer lengths required")
    cost = 2 * length - lf - lr
    n, f, r, b = map(float, (initial, forward, reverse, dntp))
    rows = [dict(cycle=0, n=n, forward=f, reverse=r, dntp=b, added=0)]
    for cycle, e in enumerate(efficiencies, 1):
        efficiency(e)
        added = min(e * n, f, r, b / cost)
        n, f, r, b = n + added, f - added, r - added, b - cost * added
        # Roundoff at the active nucleotide constraint is not negative mass.
        if -1e-9 < b < 0:
            b = 0.0
        rows.append(
            dict(
                cycle=cycle, n=n, forward=f, reverse=r, dntp=b, added=added
            )
        )
    return rows


def branching_moments(mean, variance, efficiencies):
    """N_next=N+Binomial(N,e), with independent copying conditional on N."""
    nonnegative(mean, variance)
    rows = [(mean, variance)]
    for e in efficiencies:
        efficiency(e)
        variance = (1 + e) ** 2 * variance + e * (1 - e) * mean
        mean = (1 + e) * mean
        rows.append((mean, variance))
    return rows


def cq(initial, e, threshold, gain=1.0, background=0.0):
    """Fractional crossing in the constant-efficiency exponential model."""
    nonnegative(initial, threshold, gain, background)
    efficiency(e)
    if gain == 0 or threshold <= background:
        raise ValueError(
            "positive gain and threshold above background required"
        )
    target = (threshold - background) / gain
    if initial >= target:
        return 0.0
    if initial == 0 or e == 0:
        return None
    return math.log(target / initial) / math.log1p(e)


def efficiency_from_slope(slope):
    if not math.isfinite(slope) or slope >= 0:
        raise ValueError("finite negative calibration slope required")
    e = math.expm1(-math.log(10) / slope)
    efficiency(e)
    return e


def empty_probability(mean):
    nonnegative(mean)
    return math.exp(-mean)


def results():
    bounded = budgeted(100, [0.85] * 20, 99900, 120000, 1398600, 10, 3, 3)
    ideal = amplify(100, [1] * 20)
    reduced = amplify(100, [0.85] * 20)
    return {
        "primers": primer_pair("TTACGATCGTACGG", 2, 12, 3, 3),
        "lineage": lineage(6),
        "growth": [
            dict(
                cycle=i,
                ideal=ideal[i],
                reduced=reduced[i],
                bounded=bounded[i]["n"],
            )
            for i in range(21)
        ],
        "budget": budgeted(10, [1] * 5, 90, 120, 1400, 10, 3, 3),
        "bias": [dict(cycle=n, ratio=(1.9 / 1.7) ** n) for n in range(21)],
        "thresholds": [
            dict(initial=n, cq=cq(n, 1, 102400))
            for n in (100, 200, 400, 800)
        ],
        "signal": [
            dict(cycle=n, low=100 * 2**n, high=400 * 2**n)
            for n in range(13)
        ],
        "sampling": [
            dict(mean=n, empty=empty_probability(n))
            for n in (0, 0.1, 1, 3, 5)
        ],
        "moments": branching_moments(1, 0, [0.5] * 4),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(results(), indent=2))
