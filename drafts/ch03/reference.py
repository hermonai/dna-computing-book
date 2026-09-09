"""Exact small-instance complexity examples; no molecular or runtime simulation."""
from itertools import combinations, permutations
import json


def graph(n, edges):
    """Normalize a simple directed graph with vertices 0,...,n-1."""
    if type(n) is not int or n < 2:
        raise ValueError("integer n >= 2 required")
    result = set()
    for edge in edges:
        if len(edge) != 2:
            raise ValueError("edge must contain two endpoints")
        u, v = edge
        if any(type(x) is not int or not 0 <= x < n for x in edge) or u == v:
            raise ValueError("distinct integer endpoints inside graph required")
        result.add((u, v))
    return frozenset(result)


def instance(n, edges, start, end):
    edges = graph(n, edges)
    if any(type(x) is not int or not 0 <= x < n for x in (start, end)) or start == end:
        raise ValueError("distinct endpoints inside graph required")
    return edges


def verify(n, edges, start, end, route):
    edges = instance(n, edges, start, end)
    if len(route) != n or any(type(v) is not int or not 0 <= v < n for v in route):
        return False
    return (route[0] == start and route[-1] == end and len(set(route)) == n
            and all((u, v) in edges for u, v in zip(route, route[1:])))


def permutation_oracle(n, edges, start, end):
    """Deliberately independent brute-force witness enumeration."""
    edges = instance(n, edges, start, end)
    middle = [v for v in range(n) if v not in (start, end)]
    return [(start,) + p + (end,) for p in permutations(middle)
            if all(e in edges for e in zip((start,) + p, p + (end,)))]


def subset_search(n, edges, start, end):
    """Reachability over (visited mask, last vertex), with one predecessor each.

    Counters measure this implementation's states and outgoing-neighbor scans,
    not processor time, chemical work or all possible path prefixes.
    """
    edges = instance(n, edges, start, end)
    neighbors = [sorted(v for u, v in edges if u == x) for x in range(n)]
    first = (1 << start, start)
    parents = {first: None}
    frontier = [first]
    scans = 0
    layers = [1]
    full = (1 << n) - 1
    for _ in range(1, n):
        following = []
        for mask, last in frontier:
            for nxt in neighbors[last]:
                scans += 1
                if mask & (1 << nxt):
                    continue
                newmask = mask | (1 << nxt)
                if nxt == end and newmask != full:
                    continue
                state = (newmask, nxt)
                if state not in parents:
                    parents[state] = (mask, last)
                    following.append(state)
        frontier = following
        layers.append(len(frontier))
    state = (full, end)
    route = None
    if state in parents:
        reversed_route = []
        while state is not None:
            reversed_route.append(state[1])
            state = parents[state]
        route = tuple(reversed(reversed_route))
    return {"route": route, "reachable_states": len(parents),
            "neighbor_scans": scans, "states_by_cardinality": layers}


def search_via_decision(n, edges, start, end):
    """Self-reduction; the actual oracle is exponential subset_search."""
    kept = set(instance(n, edges, start, end))
    calls = 1
    if subset_search(n, kept, start, end)["route"] is None:
        return {"route": None, "oracle_calls": calls, "kept_edges": sorted(kept)}
    for edge in sorted(kept):
        trial = kept - {edge}
        calls += 1
        if subset_search(n, trial, start, end)["route"] is not None:
            kept = trial
    # An edge-minimal yes-graph consists of exactly one spanning path.
    route = [start]
    for _ in range(n - 1):
        successors = [v for u, v in kept if u == route[-1]]
        if len(successors) != 1:
            raise AssertionError("self-reduction invariant failed")
        route.append(successors[0])
    assert verify(n, kept, start, end, route) and len(kept) == n - 1
    return {"route": tuple(route), "oracle_calls": calls, "kept_edges": sorted(kept)}


def cycle_to_path(n, edges, pivot=0):
    """Split pivot into source 0 and sink n; preserve all nonpivot vertices."""
    edges = graph(n, edges)
    if type(pivot) is not int or not 0 <= pivot < n:
        raise ValueError("pivot outside graph")
    others = [v for v in range(n) if v != pivot]
    relabel = {v: i + 1 for i, v in enumerate(others)}
    transformed = {(0 if u == pivot else relabel[u],
                    n if v == pivot else relabel[v]) for u, v in edges}
    return {"n": n + 1, "edges": frozenset(transformed), "start": 0, "end": n,
            "interior_original_labels": others}


def path_cnf(n, edges, start, end):
    """x[v,p] is variable v*n+p+1; elementary pairwise exactly-one encoding."""
    edges = instance(n, edges, start, end)
    clauses = []

    def exactly_one(ids):
        clauses.append(tuple(ids))
        clauses.extend((-a, -b) for a, b in combinations(ids, 2))

    def x(v, p):
        return v * n + p + 1

    for p in range(n):
        exactly_one([x(v, p) for v in range(n)])
    for v in range(n):
        exactly_one([x(v, p) for p in range(n)])
    clauses.extend([(x(start, 0),), (x(end, n - 1),)])
    for p in range(n - 1):
        for u in range(n):
            for v in range(n):
                if (u, v) not in edges:
                    clauses.append((-x(u, p), -x(v, p + 1)))
    return tuple(clauses)


def satisfies(clauses, values):
    """Values index positive variables from one; no implicit missing values."""
    if any(type(v) is not bool for v in values):
        raise ValueError("Boolean values required")
    if any(type(lit) is not int or lit == 0 or abs(lit) > len(values)
           for clause in clauses for lit in clause):
        raise ValueError("literal outside supplied assignment")
    return all(any(values[abs(lit) - 1] == (lit > 0) for lit in clause) for clause in clauses)


def encode_route(n, route):
    if len(route) != n or any(type(v) is not int or not 0 <= v < n for v in route):
        raise ValueError("n vertex labels required")
    return tuple(route[p] == v for v in range(n) for p in range(n))


def decode_assignment(n, values):
    if type(n) is not int or n < 2 or len(values) != n * n or any(type(v) is not bool for v in values):
        raise ValueError("Boolean n-by-n assignment required")
    rows = [[values[v * n + p] for p in range(n)] for v in range(n)]
    if any(sum(row) != 1 for row in rows) or any(sum(rows[v][p] for v in range(n)) != 1 for p in range(n)):
        raise ValueError("assignment is not a permutation matrix")
    return tuple(next(v for v in range(n) if rows[v][p]) for p in range(n))


def results():
    # Original four-vertex teaching instance, not the historical Adleman graph.
    n = 4
    edges = graph(n, [(0, 1), (0, 2), (1, 2), (2, 1), (1, 3), (2, 3)])
    witnesses = permutation_oracle(n, edges, 0, 3)
    cnf = path_cnf(n, edges, 0, 3)
    return {"scope": "Exact finite digital examples; no timing or molecular measurement",
            "instance": {"n": n, "edges": sorted(edges), "start": 0, "end": 3},
            "witnesses": witnesses, "subset_search": subset_search(n, edges, 0, 3),
            "self_reduction": search_via_decision(n, edges, 0, 3),
            "cnf": {"variables": n * n, "clauses": len(cnf),
                    "literal_occurrences": sum(map(len, cnf)),
                    "accepted_witnesses": [satisfies(cnf, encode_route(n, p)) for p in witnesses]},
            "dense_graph_counts": [{"n": k, **subset_search(k, [(u, v) for u in range(k)
                                       for v in range(k) if u != v], 0, k - 1)} for k in range(2, 9)]}


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
