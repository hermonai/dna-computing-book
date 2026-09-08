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
