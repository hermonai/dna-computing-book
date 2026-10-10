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

def pipeline(pool):
    stages = [("generated", list(pool))]
    stages.append(("endpoints", filter_start_end(stages[-1][1])))
    stages.append(("length", filter_length(stages[-1][1])))
    for vertex, kept in filter_all_vertices(stages[-1][1], range(1, 6)):
        stages.append((f"contains {vertex}", kept))
    stages.append(("verified", [p for p in stages[-1][1] if is_witness(p)]))
    return stages

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
