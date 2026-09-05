"""Exact, finite walk-pool filtering. This is not a chemical simulator."""
from dataclasses import dataclass
from collections.abc import Iterable


@dataclass(frozen=True)
class PoolResult:
    witnesses: tuple[tuple[str, ...], ...]
    stages: tuple[tuple[str, int], ...]


def validate_graph(vertices: tuple[str, ...], edges: frozenset[tuple[str, str]]) -> None:
    if not vertices or len(set(vertices)) != len(vertices):
        raise ValueError("vertices must be nonempty and unique")
    if any(not isinstance(v, str) or not v for v in vertices):
        raise ValueError("vertices must be nonempty strings")
    if any(len(edge) != 2 or any(v not in vertices for v in edge) for edge in edges):
        raise ValueError("every edge must join two declared vertices")


def enumerate_walks(vertices: tuple[str, ...], edges: frozenset[tuple[str, str]],
                    max_vertices: int) -> tuple[tuple[str, ...], ...]:
    """Enumerate all walks of lengths 1..max_vertices; repeats/loops allowed.

    Exhaustive teaching algorithm: time and materialized memory can grow
    exponentially. Length counts vertices, not edges.
    """
    validate_graph(vertices, edges)
    if type(max_vertices) is not int or max_vertices < 1:
        raise ValueError("max_vertices must be a positive integer")
    frontier = [(v,) for v in vertices]
    walks = list(frontier)
    for _ in range(1, max_vertices):
        frontier = [walk + (v,) for walk in frontier for v in vertices
                    if (walk[-1], v) in edges]
        walks.extend(frontier)
    return tuple(walks)


def filter_pool(pool: Iterable[tuple[str, ...]], vertices: tuple[str, ...],
                edges: frozenset[tuple[str, str]], start: str, end: str) -> PoolResult:
    """Filter a given pool; completeness depends on what that pool contains."""
    validate_graph(vertices, edges)
    if start not in vertices or end not in vertices:
        raise ValueError("endpoints must be declared vertices")
    candidates = tuple(pool)
    if any(not w or any(v not in vertices for v in w) or
           any((a, b) not in edges for a, b in zip(w, w[1:])) for w in candidates):
        raise ValueError("pool contains an invalid walk")
    stages = [("generated", len(candidates))]
    candidates = tuple(w for w in candidates if w[0] == start and w[-1] == end)
    stages.append(("endpoints", len(candidates)))
    candidates = tuple(w for w in candidates if len(w) == len(vertices))
    stages.append(("length", len(candidates)))
    candidates = tuple(w for w in candidates if set(w) == set(vertices))
    stages.append(("coverage", len(candidates)))
    return PoolResult(candidates, tuple(stages))


def hamiltonian_filter(vertices: tuple[str, ...], edges: frozenset[tuple[str, str]],
                       start: str, end: str) -> PoolResult:
    pool = enumerate_walks(vertices, edges, len(vertices))
    return filter_pool(pool, vertices, edges, start, end)


def chapter_example() -> PoolResult:
    vertices = ("s", "u", "v", "t")
    edges = frozenset({("s", "u"), ("s", "v"), ("u", "u"),
                       ("u", "v"), ("v", "u"), ("u", "t"), ("v", "t")})
    return hamiltonian_filter(vertices, edges, "s", "t")
