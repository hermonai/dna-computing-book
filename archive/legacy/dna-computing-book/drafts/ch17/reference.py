"""Finite, advancing paired-input automata; no chemical kinetics."""

from collections import deque
from itertools import product
import json

LISTINGS = ["validate", "paired_run", "lower_words"]
TABLES = [
    (
        "trace",
        ["State", "Upper cursor", "Lower cursor"],
        ["state", "i", "j"],
        "lrr",
    ),
    (
        "growth",
        ["Input length", "Visited", "Grid bound"],
        ["n", "visited", "bound"],
        "rrr",
    ),
]
PLOTS = [("growth-plot", "growth", "n", ["visited", "bound"])]
RULES = (
    ("seek", "", "a", "seek"),
    ("seek", "a", "b", "pair"),
    ("pair", "a", "b", "pair"),
    ("pair", "b", "", "drain"),
    ("drain", "b", "", "drain"),
)
RHO = frozenset({("a", "a"), ("b", "b")})


def validate(upper, lower, rules, rho):
    if not isinstance(upper, str) or not isinstance(lower, str):
        raise ValueError("strings required")
    if len(upper) != len(lower) or any(
        p not in rho for p in zip(upper, lower)
    ):
        raise ValueError("input is not in the paired domain")
    for rule in rules:
        if len(rule) != 4 or any(not isinstance(x, str) for x in rule):
            raise ValueError("four string fields per rule required")
        if not rule[0] or not rule[3] or not (rule[1] or rule[2]):
            raise ValueError("named states and an advancing rule required")


def paired_run(
    upper,
    lower,
    rules=RULES,
    rho=RHO,
    start="seek",
    finals=frozenset({"seek", "drain"}),
):
    validate(upper, lower, rules, rho)
    initial = (start, 0, 0)
    queue, parent = deque([initial]), {initial: None}
    while queue:
        state, i, j = current = queue.popleft()
        if state in finals and i == j == len(upper):
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return True, path[::-1], len(parent)
        for source, u, v, target in rules:
            if (
                source == state
                and upper.startswith(u, i)
                and lower.startswith(v, j)
            ):
                nxt = (target, i + len(u), j + len(v))
                if nxt not in parent:
                    parent[nxt] = (state, i, j)
                    queue.append(nxt)
    return False, [], len(parent)


def lower_words(upper, rho):
    """Enumerate witnesses; this cost is not part of paired_run."""
    choices = [sorted({b for a, b in rho if a == x}) for x in upper]
    return ("".join(parts) for parts in product(*choices))


def results():
    accepted, path, _ = paired_run("aabb", "aabb")
    return {
        "accepted": accepted,
        "trace": [dict(state=q, i=i, j=j) for q, i, j in path],
        "growth": [
            dict(
                n=2 * k,
                visited=paired_run("a" * k + "b" * k, "a" * k + "b" * k)[2],
                bound=3 * (2 * k + 1) ** 2,
            )
            for k in range(9)
        ],
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
