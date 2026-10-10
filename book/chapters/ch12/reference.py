"""Finite multiset semantics and explicit imperfect-observation models."""

from collections import Counter
from itertools import product
import math

VERTICES = tuple("ABCD")
EDGES = {
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "B"),
    ("B", "D"),
    ("C", "D"),
}
LISTINGS = [
    "walks",
    "retain",
    "verify",
    "filter_trace",
    "expected_pass",
    "detect_probability",
    "capacity_filter",
]


def walks(vertices, edges, max_length):
    """All directed walks of one through max_length vertices, once each."""
    if type(max_length) is not int or max_length < 1:
        raise ValueError("positive integer maximum length required")
    if not vertices or len(set(vertices)) != len(vertices):
        raise ValueError("nonempty distinct vertex list required")
    if any(u not in vertices or v not in vertices for u, v in edges):
        raise ValueError("unknown edge endpoint")
    frontier = [(v,) for v in vertices]
    pool = Counter(frontier)
    for _ in range(1, max_length):
        frontier = [
            p + (v,)
            for p in frontier
            for v in vertices
            if (p[-1], v) in edges
        ]
        pool.update(frontier)
    return pool


def retain(pool, predicate):
    """An exact filter preserves multiplicity of retained species."""
    if any(type(n) is not int or n < 0 for n in pool.values()):
        raise ValueError("nonnegative integer copy counts required")
    return Counter(
        {p: n for p, n in pool.items() if n > 0 and predicate(p)}
    )


def verify(path, vertices, edges, start, end):
    """Independent certificate check: identities, multiplicities and edges."""
    return (
        len(path) == len(vertices)
        and bool(path)
        and path[0] == start
        and path[-1] == end
        and Counter(path) == Counter(vertices)
        and all((u, v) in edges for u, v in zip(path, path[1:]))
    )


def filter_trace(pool, vertices, start, end):
    """Does not check edges: correctness requires a valid-walk generator."""
    stages = [
        ("endpoints", lambda p: bool(p) and p[0] == start and p[-1] == end),
        ("length", lambda p: len(p) == len(vertices)),
    ]
    stages += [(f"contains {v}", lambda p, v=v: v in p) for v in vertices]
    history = [
        dict(
            stage="generated", species=len(+pool), copies=sum(pool.values())
        )
    ]
    for name, predicate in stages:
        pool = retain(pool, predicate)
        history.append(
            dict(stage=name, species=len(pool), copies=sum(pool.values()))
        )
    return pool, history


def expected_pass(population, probabilities):
    """Expected counts under fixed species-wise retention, no capacity."""
    if len(population) != len(probabilities):
        raise ValueError("matched species axes required")
    if any(not math.isfinite(n) or n < 0 for n in population):
        raise ValueError("finite nonnegative population required")
    if any(not math.isfinite(p) or not 0 <= p <= 1 for p in probabilities):
        raise ValueError("retention probabilities must lie in [0, 1]")
    return [n * p for n, p in zip(population, probabilities)]


def detect_probability(copies, survival, detection=1.0):
    """Independent copies; survival and conditional detection are fixed."""
    if type(copies) is not int or copies < 0:
        raise ValueError("nonnegative integer copy count required")
    if any(
        not math.isfinite(p) or not 0 <= p <= 1
        for p in (survival, detection)
    ):
        raise ValueError("probabilities must lie in [0, 1]")
    q = survival * detection
    if copies == 0 or q == 0:
        return 0.0
    if q == 1:
        return 1.0
    return -math.expm1(copies * math.log1p(-q))


def capacity_filter(items, eligible, capacity):
    """Ordered physical-copy IDs, first-arrival admission, no replacement."""
    if type(capacity) is not int or capacity < 0:
        raise ValueError("nonnegative integer capacity required")
    return [x for x in items if eligible(x)][:capacity]


def results():
    generated = walks(VERTICES, EDGES, 5)
    kept, trace = filter_trace(generated, VERTICES, "A", "D")
    # Brute-force tuples are a separate candidate generator for the oracle.
    oracle = [
        p
        for p in product(VERTICES, repeat=4)
        if verify(p, VERTICES, EDGES, "A", "D")
    ]
    signal = expected_pass([10, 10000], [0.8, 0.01])
    signal2 = expected_pass(signal, [0.8, 0.01])
    order = ["bad", "good"]
    f = lambda xs: capacity_filter(xs, lambda _: True, 1)
    g = lambda xs: capacity_filter(xs, lambda x: x == "good", 2)
    return dict(
        trace=trace,
        kept=["".join(p) for p in sorted(kept)],
        oracle=["".join(p) for p in sorted(oracle)],
        noisy=[
            dict(stage=i, true=t, false=f, purity=t / (t + f))
            for i, (t, f) in enumerate([[10, 10000], signal, signal2])
        ],
        survival=[
            dict(copies=n, probability=detect_probability(n, 0.8**6, 0.9))
            for n in [0, 1, 2, 5, 10, 20, 50]
        ],
        order=dict(F_then_G=g(f(order)), G_then_F=f(g(order))),
    )
