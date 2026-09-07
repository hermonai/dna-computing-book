"""Original bounded symbolic companion; no chemical kinetics or laboratory prediction."""
from itertools import permutations
from math import ceil, factorial, log1p, log

VERTICES = tuple("ABCDEF")
EDGES = frozenset({
    ("A","B"),("A","C"),("B","C"),("B","D"),("C","B"),
    ("C","D"),("D","E"),("D","F"),("E","F"),
})
START, END = "A", "F"

def edge_valid(route, edges=EDGES):
    return all((a,b) in edges for a,b in zip(route,route[1:]))

def is_hamiltonian(route, vertices=VERTICES, edges=EDGES, start=START, end=END):
    return (len(route)==len(vertices) and bool(route)
            and route[0]==start and route[-1]==end
            and set(route)==set(vertices) and len(set(route))==len(route)
            and edge_valid(route,edges))

def walks(max_vertices=7, vertices=VERTICES, edges=EDGES):
    """Enumerate all legal directed walks of lengths 1..max_vertices, with repeats."""
    if type(max_vertices) is not int or max_vertices < 1:
        raise ValueError("positive maximum length required")
    frontier=[(v,) for v in vertices]
    result=[]
    for _ in range(max_vertices):
        result.extend(frontier)
        frontier=[r+(v,) for r in frontier for v in vertices if (r[-1],v) in edges]
    return result

def filter_pool(pool, vertices=VERTICES, edges=EDGES, start=START, end=END):
    """Do not assume generation was sound: final edge verification is independent."""
    stages=[("generated",list(pool))]
    predicates=[
        ("endpoints",lambda r: bool(r) and r[0]==start and r[-1]==end),
        ("length",lambda r: len(r)==len(vertices)),
        ("coverage",lambda r: set(vertices)<=set(r)),
        ("verified",lambda r: is_hamiltonian(r,vertices,edges,start,end)),
    ]
    for name,predicate in predicates:
        stages.append((name,[r for r in stages[-1][1] if predicate(r)]))
    return stages

def permutation_oracle(vertices=VERTICES, edges=EDGES, start=START, end=END):
    """Independent witness construction: enumerate each internal vertex exactly once."""
    middle=[v for v in vertices if v not in (start,end)]
    return [(start,)+p+(end,) for p in permutations(middle)
            if all((a,b) in edges for a,b in zip((start,)+p,p+(end,)))]

def required_samples(p, delta):
    """Smallest integer M from the independent fixed-probability miss bound."""
    if not 0 < p <= 1 or not 0 < delta < 1:
        raise ValueError("require 0 < p <= 1 and 0 < delta < 1")
    return 1 if p == 1 else ceil(log(delta)/log1p(-p))

def reverse_complement(sequence):
    if set(sequence)-set("ACGT"):
        raise ValueError("only unambiguous DNA letters are supported")
    return sequence.translate(str.maketrans("ACGT","TGCA"))[::-1]

def results():
    stages=filter_pool(walks())
    pseudo=tuple("ABECDF")
    contaminated=filter_pool(walks()+[pseudo])
    return {
        "graph":{"vertices":list(VERTICES),"edges":[list(e) for e in sorted(EDGES)]},
        "scope":"All legal walks of 1..7 vertices; symbolic identities, not concentration or yield",
        "counts":{name:len(pool) for name,pool in stages},
        "survivors":["".join(r) for r in stages[-1][1]],
        "oracle":["".join(r) for r in permutation_oracle()],
        "contaminated_counts":{name:len(pool) for name,pool in contaminated},
        "scaling":[{"n":n,"internal_orders":factorial(n-2)} for n in (6,10,15,20,25)],
        "sampling":{"p":1/24,"delta":0.01,"M":required_samples(1/24,0.01)},
    }

if __name__ == "__main__":
    import json
    print(json.dumps(results(),indent=2))
