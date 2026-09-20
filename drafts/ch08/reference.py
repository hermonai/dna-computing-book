"""Substrate contracts and catalytic kinetics; assigned teaching rates."""

import json
import math

PAIR = str.maketrans("ACGT", "TGCA")


def dna(sequence):
    if (
        not isinstance(sequence, str)
        or not sequence
        or set(sequence) - set("ACGT")
    ):
        raise ValueError("nonempty canonical uppercase DNA required")
    return sequence


def complement(sequence):
    """Complement in displayed coordinates, not reverse complement."""
    return dna(sequence).translate(PAIR)


def ecori_cut_sites(top):
    """Fully paired linear duplex; indices count bases left of each bond."""
    dna(top)
    return [
        (i + 1, i + 5)
        for i in range(len(top) - 5)
        if top[i : i + 6] == "GAATTC"
    ]


def seal_nick(
    left, right, template, *, phosphate=True, hydroxyl=True, atp=True
):
    """Idealized aligned nick contract; not a ligation-efficiency model."""
    joined = dna(left) + dna(right)
    if complement(joined) != dna(template):
        raise ValueError("requires a fully paired, gap-free aligned nick")
    if not all(type(v) is bool for v in (phosphate, hydroxyl, atp)):
        raise ValueError("terminal/cofactor flags must be boolean")
    if not (phosphate and hydroxyl and atp):
        raise ValueError("teaching ATP-dependent ligase contract not met")
    return joined


def extend_primer(template, primer, pool, *, hydroxyl=True):
    """Template is displayed 3'->5'; primer/result are 5'->3'."""
    target = complement(template)
    dna(primer)
    if not target.startswith(primer):
        raise ValueError(
            "primer must be a perfectly paired template prefix"
        )
    if type(hydroxyl) is not bool or not hydroxyl:
        raise ValueError("extendable primer 3-OH required")
    if set(pool) != set("ACGT") or any(
        type(n) is not int or n < 0 for n in pool.values()
    ):
        raise ValueError("nonnegative integer inventory for each dNTP")
    remaining = dict(pool)
    product, ppi = primer, 0
    for base in target[len(primer) :]:
        if remaining[base] == 0:
            break
        remaining[base] -= 1
        product += base
        ppi += 1
    return product, remaining, ppi


def parameters(*values):
    if any(
        isinstance(v, bool)
        or not isinstance(v, (int, float))
        or not math.isfinite(v)
        or v < 0
        for v in values
    ):
        raise ValueError("finite nonnegative parameters required")


def rhs(state, k1, km1, kcat):
    """E,S,C,P in micromolar; k1 in uM^-1 s^-1, other rates s^-1."""
    e, s, c, p = state
    binding, release, turnover = k1 * e * s, km1 * c, kcat * c
    return (
        -binding + release + turnover,
        -binding + release,
        binding - release - turnover,
        turnover,
    )


def integrate(e0, s0, k1, km1, kcat, end, dt=0.001):
    """Full mass-action RK4; reject a nonphysical stage, never clip."""
    parameters(e0, s0, k1, km1, kcat, end, dt)
    if dt == 0:
        raise ValueError("positive time step required")

    def f(y):
        if min(y) < 0 or not all(math.isfinite(v) for v in y):
            raise ValueError("nonphysical stage: reduce step")
        return rhs(y, k1, km1, kcat)

    t, y = 0.0, (e0, s0, 0.0, 0.0)
    trace = [(t, *y)]
    while t < end:
        h = min(dt, end - t)
        if t + h == t:
            raise ValueError("step below time resolution")
        a = f(y)
        b = f(tuple(v + h * d / 2 for v, d in zip(y, a)))
        c = f(tuple(v + h * d / 2 for v, d in zip(y, b)))
        d = f(tuple(v + h * z for v, z in zip(y, c)))
        y = tuple(
            v + h * (aa + 2 * bb + 2 * cc + dd) / 6
            for v, aa, bb, cc, dd in zip(y, a, b, c, d)
        )
        f(y)
        t += h
        trace.append((t, *y))
    return trace


def clamped(e0, substrate, k1, km1, kcat, t):
    """Exact initial transient when free substrate is externally clamped."""
    parameters(e0, substrate, k1, km1, kcat, t)
    alpha = k1 * substrate + km1 + kcat
    if alpha == 0:
        return 0.0, 0.0
    steady = e0 * k1 * substrate / alpha
    occupied = steady * -math.expm1(-alpha * t)
    return occupied, kcat * (steady * t - occupied / alpha)


def mm_rate(substrate, enzyme, k1, km1, kcat):
    parameters(substrate, enzyme, k1, km1, kcat)
    if k1 == 0 or km1 + kcat == 0:
        raise ValueError("positive association and escape sum required")
    km = (km1 + kcat) / k1
    return kcat * enzyme * substrate / (km + substrate)


def results():
    rates = (2.0, 1.0, 3.0)
    trace = integrate(0.02, 1.0, *rates, end=1.0, dt=0.002)
    curve = []
    for t, e, s, c, p in trace[::10] + trace[-1:]:
        cc, pp = clamped(0.02, 1.0, *rates, t)
        curve.append(
            dict(
                t=t,
                complex_nm=c * 1000,
                clamped_nm=cc * 1000,
                product_nm=p * 1000,
                clamped_product_nm=pp * 1000,
            )
        )
    return {
        "units": "uM and seconds; illustrative, not measured enzyme parameters",
        "km_um": 2.0,
        "kd_um": 0.5,
        "vmax_um_s": 0.06,
        "substrate_curve": [
            dict(s=i / 10, v=mm_rate(i / 10, 0.02, *rates))
            for i in range(101)
        ],
        "transient": curve,
        "rates": [
            dict(s=s, v=mm_rate(s, 0.02, *rates))
            for s in [0, 0.5, 1, 2, 10]
        ],
        "cuts": ecori_cut_sites("CCGAATTCTT"),
        "extension": extend_primer(
            "TGCATG", "AC", dict(A=1, C=1, G=1, T=1)
        ),
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
