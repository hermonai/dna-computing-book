"""Occupancy-register multiset semantics, not a selective-clear protocol."""

from collections import Counter
import math

LISTINGS = ["write", "separate", "and_gate", "retained"]


def check(pool, width):
    if type(width) is not int or width < 1:
        raise ValueError("positive register width required")
    if any(
        type(s) is not int
        or not 0 <= s < 2**width
        or type(k) is not int
        or k < 0
        for s, k in pool.items()
    ):
        raise ValueError("invalid occupancy or copy count")


def address(bit, width):
    if type(bit) is not int or not 0 <= bit < width:
        raise ValueError("bit address outside register")


def write(pool, bit, value, width):
    """Push forward counts: distinct input states can coalesce."""
    check(pool, width)
    address(bit, width)
    if type(value) is not int or value not in (0, 1):
        raise ValueError("write value must be 0 or 1")
    out = Counter()
    for state, count in pool.items():
        new = state | (1 << bit) if value else state & ~(1 << bit)
        if count:
            out[new] += count
    return out


def separate(pool, bit, width):
    check(pool, width)
    address(bit, width)
    on, off = Counter(), Counter()
    for state, count in pool.items():
        if count:
            (on if state & (1 << bit) else off)[state] = count
    return on, off


def and_gate(pool, a, b, out, width):
    """out := a AND b; inputs remain unchanged; out is cleared first."""
    check(pool, width)
    for bit in (a, b, out):
        address(bit, width)
    if len({a, b, out}) != 3:
        raise ValueError("distinct input and output addresses required")
    blank = write(pool, out, 0, width)
    a1, a0 = separate(blank, a, width)
    both, a1b0 = separate(a1, b, width)
    return write(both, out, 1, width) + a1b0 + a0


def retained(operations, probability):
    if type(operations) is not int or operations < 0:
        raise ValueError("nonnegative integer operation count required")
    if not math.isfinite(probability) or not 0 <= probability <= 1:
        raise ValueError("probability outside [0,1]")
    return probability**operations


def occupancy(bits):
    return sum(b << i for i, b in enumerate(bits))


def results():
    initial = Counter(
        {occupancy((a, b, 0)): 5 for a in (0, 1) for b in (0, 1)}
    )
    final = and_gate(initial, 0, 1, 2, 3)
    collision = write(Counter({0: 3, 4: 5}), 2, 0, 3)
    return dict(
        gate=[
            dict(
                a=a,
                b=b,
                c=int(a and b),
                copies=final[occupancy((a, b, int(a and b)))],
            )
            for a in (0, 1)
            for b in (0, 1)
        ],
        initial_copies=sum(initial.values()),
        final_copies=sum(final.values()),
        collision=dict(copies=collision[0], species=len(collision)),
        reuse_curve=[
            dict(
                operations=k, p99=retained(k, 0.99), p999=retained(k, 0.999)
            )
            for k in range(0, 501, 5)
        ],
        reuse=[
            dict(
                operations=k, p99=retained(k, 0.99), p999=retained(k, 0.999)
            )
            for k in (0, 10, 25, 50, 100, 200, 500)
        ],
    )
