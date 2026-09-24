"""Original finite-copy CNF construction; symbolic domains, no chemistry."""

from collections import Counter
from itertools import product
import math

LISTINGS = ["clause_partition", "solve", "witness_probability"]
CNF = ((1, 2), (-1, 3), (-2, -3))


def validate(n, clauses):
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative variable count required")
    if any(
        type(l) is not int or not 1 <= abs(l) <= n
        for c in clauses
        for l in c
    ):
        raise ValueError("literals use signed one-based variable IDs")


def holds(bits, literal):
    return bits[abs(literal) - 1] == (1 if literal > 0 else 0)


def clause_partition(pool, clause):
    """Consume successive residuals, never clone a physical copy."""
    residual, accepted = Counter(pool), Counter()
    branches = []
    for literal in clause:
        yes = Counter(
            {a: k for a, k in residual.items() if holds(a, literal)}
        )
        residual.subtract(yes)
        residual = +residual
        accepted.update(yes)
        branches.append(sum(yes.values()))
    return accepted, residual, branches


def solve(n, clauses, copies=1):
    validate(n, clauses)
    if type(copies) is not int or copies < 0:
        raise ValueError("nonnegative integer copies required")
    pool = Counter({a: copies for a in product((0, 1), repeat=n) if copies})
    trace = [dict(stage=0, species=len(pool), copies=sum(pool.values()))]
    for i, clause in enumerate(clauses, 1):
        pool, rejected, branches = clause_partition(pool, clause)
        trace.append(
            dict(
                stage=i,
                species=len(pool),
                copies=sum(pool.values()),
                rejected=sum(rejected.values()),
                branches=branches,
            )
        )
    return pool, trace


def oracle(n, clauses):
    """Integer enumeration, independent of sequential tube operations."""
    validate(n, clauses)
    answers = []
    for mask in range(2**n):
        values = tuple((mask >> i) & 1 for i in range(n))
        if all(
            any((values[abs(l) - 1] == 1) == (l > 0) for l in clause)
            for clause in clauses
        ):
            answers.append(values)
    return sorted(answers)


def witness_probability(n, samples, witnesses=1, survival=1.0):
    """IID uniform assignments, followed by independent survival."""
    validate(n, ())
    if type(samples) is not int or samples < 0:
        raise ValueError("nonnegative integer samples required")
    if type(witnesses) is not int or not 0 <= witnesses <= 2**n:
        raise ValueError("invalid number of witnesses")
    if not math.isfinite(survival) or not 0 <= survival <= 1:
        raise ValueError("survival must lie in [0,1]")
    q = witnesses / 2**n * survival
    if samples == 0 or q == 0:
        return 0.0
    return 1.0 if q == 1 else -math.expm1(samples * math.log1p(-q))


def results():
    pool, trace = solve(3, CNF, 7)
    duplicate = Counter()
    original = Counter({(1, 1, 0): 7})
    for literal in CNF[0]:
        duplicate.update(
            {a: k for a, k in original.items() if holds(a, literal)}
        )
    return dict(
        trace=trace,
        witnesses=["".join(map(str, a)) for a in sorted(pool)],
        oracle=["".join(map(str, a)) for a in oracle(3, CNF)],
        duplicate_bug=sum(duplicate.values()),
        coverage_curve=[
            dict(samples=m, probability=witness_probability(10, m))
            for m in range(0, 8193, 64)
        ],
        coverage=[
            dict(samples=m, probability=witness_probability(10, m))
            for m in (0, 256, 512, 1024, 2048, 4096, 8192)
        ],
        truth=[
            dict(
                assignment="".join(map(str, a)),
                literals=[int(any(holds(a, l) for l in c)) for c in CNF],
            )
            for a in product((0, 1), repeat=3)
        ],
    )
