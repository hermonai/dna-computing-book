"""DNAD-22 exact aTAM teaching reference.

This is an abstract, finite-grid simulator. Glue strengths are integers in the
formal model; they are not inferred molecular binding energies.
"""

from dataclasses import dataclass
from typing import Dict, Tuple
import json
import math

Pos = Tuple[int, int]


@dataclass(frozen=True)
class Tile:
    name: str
    north: Tuple[str, int]
    east: Tuple[str, int]
    south: Tuple[str, int]
    west: Tuple[str, int]
    bit: int | None = None

    def __post_init__(self):
        for label, strength in (self.north, self.east, self.south, self.west):
            if (
                not isinstance(label, str)
                or not label
                or isinstance(strength, bool)
                or not isinstance(strength, int)
                or strength < 0
            ):
                raise ValueError(
                    "glues require a label and nonnegative integer strength"
                )
            if label == "0" and strength != 0:
                raise ValueError("null glue has zero strength")


def bond(a, b):
    """Matching labels with conflicting strengths are not a valid bond."""
    return a[1] if a[0] != "0" and a == b and a[1] > 0 else 0


def size(n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("size must be a nonnegative integer")
    return n


def support(tile: Tile, pos: Pos, assembly: Dict[Pos, Tile]):
    x, y = pos
    n = assembly.get((x, y + 1))
    e = assembly.get((x + 1, y))
    s = assembly.get((x, y - 1))
    w = assembly.get((x - 1, y))
    total = 0
    if n:
        total += bond(tile.north, n.south)
    if e:
        total += bond(tile.east, e.west)
    if s:
        total += bond(tile.south, s.north)
    if w:
        total += bond(tile.west, w.east)
    return total


def legal_tiles(pos, assembly, tiles, tau=2):
    if isinstance(tau, bool) or not isinstance(tau, int) or tau <= 0:
        raise ValueError("temperature is a positive integer")
    if pos in assembly:
        return []
    return [t for t in tiles if support(t, pos, assembly) >= tau]


def xor_tiles():
    # A computational tile receives one bit from south and one from west.
    # Both matching input bonds have strength 1, so tau=2 enforces cooperation.
    out = []
    for s in (0, 1):
        for w in (0, 1):
            z = s ^ w
            out.append(
                Tile(
                    f"X{s}{w}",
                    (f"v{z}", 1),
                    (f"h{z}", 1),
                    (f"v{s}", 1),
                    (f"h{w}", 1),
                    z,
                )
            )
    return out


def seed(n):
    """L-shaped boundary: bottom is 1,0,0,...; left boundary is all 0."""
    size(n)
    A = {}
    # Strength-two seed-only bonds connect the entire L at tau=2. They are
    # not recognized by computational tiles. Computational inputs stay one.
    for x in range(1, n + 1):
        b = 1 if x == 1 else 0
        A[(x, 0)] = Tile(
            f"B{x}",
            (f"v{b}", 1),
            ("seed-h", 2) if x < n else ("0", 0),
            ("0", 0),
            ("seed-h", 2),
            b,
        )
    for y in range(1, n + 1):
        A[(0, y)] = Tile(
            f"L{y}",
            ("seed-v", 2) if y < n else ("0", 0),
            ("h0", 1),
            ("seed-v", 2),
            ("0", 0),
            0,
        )
    A[(0, 0)] = Tile(
        "corner",
        ("seed-v", 2) if n else ("0", 0),
        ("seed-h", 2) if n else ("0", 0),
        ("0", 0),
        ("0", 0),
        0,
    )
    return A


def grow(n, tiles=None):
    size(n)
    tiles = xor_tiles() if tiles is None else tiles
    A = seed(n)
    trace = []
    # Diagonal-independent deterministic schedule. The legality test itself does
    # not depend on this order; tests enumerate alternative frontier choices.
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            legal = legal_tiles((x, y), A, tiles)
            if len(legal) != 1:
                raise RuntimeError(f"frontier {(x, y)} has {len(legal)} legal tiles")
            A[(x, y)] = legal[0]
            trace.append((x, y, legal[0].bit))
    return A, trace


def oracle(n):
    """Independent cellular-automaton recurrence z[x,y]=z[x,y-1] XOR z[x-1,y]."""
    size(n)
    z = {(x, 0): (1 if x == 1 else 0) for x in range(1, n + 1)}
    z.update({(0, y): 0 for y in range(1, n + 1)})
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            z[(x, y)] = z[(x, y - 1)] ^ z[(x - 1, y)]
    return z


def ambiguity_example():
    tiles = xor_tiles()
    mutant = Tile("mutant", ("v0", 1), ("h0", 1), ("v1", 1), ("h0", 1), 0)
    A = seed(2)
    # Position (1,1) receives south=1 and west=0. Reference X10 and mutant
    # both bind with strength 2 but have different names/outputs downstream.
    return [t.name for t in legal_tiles((1, 1), A, tiles + [mutant])]


def finite_yield(p, n):
    """Independent-site explanatory model: probability all n^2 placements are correct."""
    size(n)
    if not math.isfinite(p) or not 0 <= p <= 1:
        raise ValueError("probability must lie in [0,1]")
    if n == 0 or p == 0:
        return 1.0
    if p == 1:
        return 0.0
    return math.exp(n * n * math.log1p(-p))


def frontier(assembly):
    """All adjacent empty lattice positions, not just a raster-order choice."""
    return {
        (x + dx, y + dy)
        for x, y in assembly
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0))
        if (x + dx, y + dy) not in assembly
    }


def explore(n, tiles=None, max_states=100000):
    """Enumerate all reachable finite states, merging identical assemblies.

    The bound is an exploration safeguard, not an undecidability oracle.
    This routine never restricts attachments to the preferred square window.
    """
    size(n)
    tiles = xor_tiles() if tiles is None else tiles
    key = lambda a: tuple(sorted((x, y, t.name) for (x, y), t in a.items()))
    start = seed(n)
    todo = [start]
    seen = {key(start)}
    terminals = []
    while todo:
        a = todo.pop()
        choices = [
            (p, t) for p in sorted(frontier(a)) for t in legal_tiles(p, a, tiles)
        ]
        if not choices:
            terminals.append(a)
        for p, t in choices:
            b = dict(a)
            b[p] = t
            k = key(b)
            if k not in seen:
                if len(seen) >= max_states:
                    raise RuntimeError("exploration budget exhausted")
                seen.add(k)
                todo.append(b)
    return len(seen), terminals


def minimum_cut(assembly):
    """Exhaustive independent stability oracle for very small binding graphs."""
    positions = sorted(assembly)
    if len(positions) <= 1:
        return math.inf
    if len(positions) > 18:
        raise ValueError("cut oracle is intentionally small")
    edges = []
    for i, (x, y) in enumerate(positions):
        for j in range(i + 1, len(positions)):
            xx, yy = positions[j]
            if (xx, yy) == (x + 1, y):
                edges.append(
                    (i, j, bond(assembly[(x, y)].east, assembly[(xx, yy)].west))
                )
            if (xx, yy) == (x, y + 1):
                edges.append(
                    (i, j, bond(assembly[(x, y)].north, assembly[(xx, yy)].south))
                )
    return min(
        sum(w for i, j, w in edges if bool(mask & (1 << i)) != bool(mask & (1 << j)))
        for mask in range(1, 1 << (len(positions) - 1))
    )


def trap_probability(detach, lock):
    """Competing exponential clocks after a wrong single-contact attachment."""
    if (
        not all(math.isfinite(v) and v >= 0 for v in (detach, lock))
        or detach + lock == 0
    ):
        raise ValueError("positive total exit rate required")
    return lock / (detach + lock)


def results():
    n = 8
    A, tr = grow(n)
    z = oracle(n)
    grid = [[A[(x, y)].bit for x in range(1, n + 1)] for y in range(1, n + 1)]
    return {
        "n": n,
        "grid": grid,
        "oracle_match": all(
            A[(x, y)].bit == z[(x, y)] for x in range(1, n + 1) for y in range(1, n + 1)
        ),
        "placements": len(tr),
        "tile_types": len(xor_tiles()),
        "all_schedule_check_n3": {
            "reachable_states": explore(3)[0],
            "terminal_assemblies": len(explore(3)[1]),
        },
        "seed_minimum_cut_n3": minimum_cut(seed(3)),
        "wrong_contact_lock_probability": trap_probability(9, 1),
        "ambiguous_legal_tiles": ambiguity_example(),
        "yield_examples": [
            {"p": p, "n": m, "all_correct": finite_yield(p, m)}
            for p, m in [(0.01, 10), (0.01, 100), (0.001, 100)]
        ],
    }


TABLES = [
    (
        "yield_examples",
        ["Error probability", "Side length", "All-correct probability"],
        ["p", "n", "all_correct"],
        "rrr",
    )
]
PLOTS = []
LISTINGS = ["bond", "legal_tiles", "seed", "explore", "trap_probability"]

if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
