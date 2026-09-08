"""Logical reconstruction on Adleman's graph, not a kinetic or wet-lab simulator."""
from collections import Counter
from fractions import Fraction
from itertools import permutations
import json
import math

# Original Fig. 1 visually transcribed; layout does not encode additional edges.
VERTICES = tuple(range(7))
EDGES = frozenset({(0, 1), (0, 3), (0, 6), (1, 2), (1, 3),
                   (2, 1), (2, 3), (3, 2), (3, 4), (4, 1),
                   (4, 5), (5, 1), (5, 2), (5, 6)})
START, END = 0, 6
# Only the three vertex codes actually printed in the paper's Fig. 2.
PUBLISHED_CODES = {2: "TATCGGATCGGTATATCCGA",
                   3: "GCTATTCGAGCTTAAAGCTA",
                   4: "GGCTAGGTACCAGCATGCTT"}


def complement(sequence):
    if not sequence or set(sequence) - set("ACGT"):
        raise ValueError("nonempty uppercase DNA required")
    return sequence.translate(str.maketrans("ACGT", "TGCA"))


def edge_sequence(u, v, codes=PUBLISHED_CODES, start=START, end=END):
    """Upper strand 5-prime to 3-prime; terminal vertices use whole codes."""
    left, right = codes[u], codes[v]
    if any(len(s) != 20 or set(s) - set("ACGT") for s in (left, right)):
        raise ValueError("vertex codes must be 20 canonical bases")
    return (left if u == start else left[10:]) + (right if v == end else right[:10])


def generate_candidates(max_vertices=8, vertices=VERTICES, edges=EDGES):
    """Finite exhaustive walk inventory, all starts, repeats allowed."""
    if type(max_vertices) is not int or max_vertices < 1:
        raise ValueError("positive integer bound required")
    if not vertices or len(set(vertices)) != len(vertices):
        raise ValueError("distinct nonempty vertices required")
    if any(u not in vertices or v not in vertices for u, v in edges):
        raise ValueError("edge outside vertex set")
    frontier = [(v,) for v in vertices]
    result = []
    for _ in range(max_vertices):
        result.extend(frontier)
        frontier = [p + (v,) for p in frontier for v in vertices if (p[-1], v) in edges]
    return result


def filter_start_end(pool, start=START, end=END):
    return [p for p in pool if p and p[0] == start and p[-1] == end]


def filter_length(pool, length=7):
    return [p for p in pool if len(p) == length]


def filter_all_vertices(pool, vertices=VERTICES):
    stages = []
    for vertex in vertices:
        pool = [p for p in pool if vertex in p]
        stages.append((vertex, list(pool)))
    return stages


def is_witness(route, edges=EDGES):
    return (len(route) == 7 and route[0] == START and route[-1] == END
            and set(route) == set(VERTICES)
            and all(edge in edges for edge in zip(route, route[1:])))


def pipeline(pool):
    stages = [("generated", list(pool))]
    stages.append(("endpoints", filter_start_end(stages[-1][1])))
    stages.append(("length", filter_length(stages[-1][1])))
    for vertex, kept in filter_all_vertices(stages[-1][1], range(1, 6)):
        stages.append((f"contains {vertex}", kept))
    stages.append(("verified", [p for p in stages[-1][1] if is_witness(p)]))
    return stages


def oracle(edges=EDGES):
    return [(START,) + p + (END,) for p in permutations(range(1, 6))
            if is_witness((START,) + p + (END,), edges)]


def graduated_bands(routes):
    """Ideal lengths by occurrence; no intensities, efficiencies or gel model."""
    bands = {v: set() for v in range(1, 7)}
    for route in routes:
        if not route or route[0] != START or set(route) - set(VERTICES):
            raise ValueError("routes must begin at 0 and use known vertices")
        for position, vertex in enumerate(route):
            if vertex != START:
                bands[vertex].add(20 * (position + 1))
    return {str(v): sorted(xs) for v, xs in bands.items()}


def survival(initial_true, initial_false, q, f, stages):
    """Independent molecules; constant conditional retention per stage."""
    if any(type(n) is not int or n < 0 for n in (initial_true, initial_false, stages)):
        raise ValueError("nonnegative integer counts required")
    q, f = Fraction(q), Fraction(f)
    if not 0 <= q <= 1 or not 0 <= f <= 1:
        raise ValueError("probabilities outside [0,1]")
    rows = [{"stage": k, "true_expected": float(initial_true * q ** k),
             "false_expected": float(initial_false * f ** k)} for k in range(stages + 1)]
    return {"rows": rows, "zero_true_probability": float((1 - q ** stages) ** initial_true)}


def results():
    pool = generate_candidates()
    pseudo = (0, 1, 2, 4, 3, 5, 6)
    paths = [(0, 1, 2, 3, 4, 5, 6), (0, 1, 3, 4, 5, 6), (0, 3, 2, 3, 4, 5, 6)]
    return {
        "scope": "Exact finite logical model; counts are not historical molecule yields.",
        "graph": {"vertices": list(VERTICES), "edges": sorted(EDGES), "start": START, "end": END},
        "bound": 8,
        "stages": [{"stage": n, "count": len(p)} for n, p in pipeline(pool)],
        "fault_stages": [{"stage": n, "count": len(p)} for n, p in pipeline(pool + [pseudo])],
        "witnesses": oracle(),
        "published_codes": PUBLISHED_CODES,
        "edge_2_3": edge_sequence(2, 3), "edge_3_4": edge_sequence(3, 4),
        "splint_3_aligned_3_to_5": complement(PUBLISHED_CODES[3]),
        "readout_individual": [graduated_bands([p]) for p in paths],
        "readout_mixture": graduated_bands(paths),
        "sensitivity": survival(3, 1000, Fraction(4, 5), Fraction(1, 10), 5),
        "copies_per_50_pmol": 50 * 10 ** -12 * 6.02214076 * 10 ** 23,
        "edge_species": len(EDGES), "internal_splint_species": 5,
        "fixed_endpoint_orders": [{"n": n, "orders": math.factorial(n - 2)} for n in (7, 10, 15, 20)],
        "route_length_histogram": dict(sorted(Counter(map(len, pool)).items())),
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
