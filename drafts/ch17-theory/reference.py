"""Advancing automata and assigned-rate stochastic teaching models, not assays."""

from collections import deque
from itertools import product
import json
import math

LISTINGS = [
    "validate",
    "paired_run",
    "lower_words",
    "prefix_conflicts",
    "expand_rules",
    "race",
    "parity_distribution",
]
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
TABLES += [
    (
        "race",
        ["Time (s)", "Correct", "Incorrect", "Uncommitted"],
        ["time", "correct", "incorrect", "uncommitted"],
        "rrrr",
    ),
    (
        "parity",
        ["Symbols read", "Even", "Odd", "Lost"],
        ["n", "even", "odd", "lost"],
        "rrrr",
    ),
]
PLOTS += [
    (
        "race-plot",
        "race_curve",
        "time",
        ["correct", "incorrect", "uncommitted"],
    )
]


def prefix_conflicts(rules):
    """Syntactic criterion only; not a reachable-state determinism decider."""
    rules = tuple(rules)
    validate("", "", rules, frozenset())
    comparable = lambda a, b: a.startswith(b) or b.startswith(a)
    return [
        (i, j)
        for i, a in enumerate(rules)
        for j, b in enumerate(rules[i + 1 :], i + 1)
        if a[0] == b[0]
        and comparable(a[1], b[1])
        and comparable(a[2], b[2])
    ]


def expand_rules(rules, reserved=()):
    """Acceptance-preserving private paths; no determinism guarantee."""
    rules = tuple(rules)
    validate("", "", rules, frozenset())
    used = {r[i] for r in rules for i in (0, 3)} | set(reserved)
    expanded, serial = [], 0
    for source, upper, lower, target in rules:
        tokens = [(x, "") for x in upper] + [("", y) for y in lower]
        current = source
        for index, (x, y) in enumerate(tokens):
            if index == len(tokens) - 1:
                nxt = target
            else:
                while f"private{serial}" in used:
                    serial += 1
                nxt = f"private{serial}"
                used.add(nxt)
            expanded.append((current, x, y, nxt))
            current = nxt
    return tuple(expanded)


def race(rates, time):
    """Independent constant commitment hazards; finite-time output masses."""
    rates = tuple(rates)
    if not rates or any(not math.isfinite(v) or v < 0 for v in rates):
        raise ValueError("nonempty finite nonnegative rates required")
    if not math.isfinite(time) or time < 0:
        raise ValueError("finite nonnegative time required")
    total = math.fsum(rates)
    if not math.isfinite(total):
        raise ValueError("total rate overflow")
    if total == 0:
        return tuple(0.0 for _ in rates), 1.0
    completed = -math.expm1(-total * time)
    return tuple(v / total * completed for v in rates), math.exp(
        -total * time
    )


def encounter_statistics(binding, dissociation, commitment):
    """Exact renewal branch probabilities and mean time, not a time-course fit."""
    b, d, c = map(tuple, (binding, dissociation, commitment))
    if not b or not len(b) == len(d) == len(c):
        raise ValueError("nonempty equal-length rate vectors required")
    if any(not math.isfinite(x) or x < 0 for x in b + d + c):
        raise ValueError("finite nonnegative rates required")
    active = [(br, dr, cr) for br, dr, cr in zip(b, d, c) if br > 0]
    if any(dr + cr == 0 for br, dr, cr in active):
        raise ValueError(
            "active bound trap violates the renewal assumptions"
        )
    weights = [
        br * cr / (dr + cr) if br else 0.0 for br, dr, cr in zip(b, d, c)
    ]
    rate = math.fsum(weights)
    if rate == 0:
        raise ValueError("eventual commitment is unavailable")
    bound_time = math.fsum(br / (dr + cr) for br, dr, cr in active)
    return tuple(x / rate for x in weights), (1 + bound_time) / rate


def parity_distribution(word, error=0.0, loss=0.0):
    """Two-state parity reader; loss is absorbing, error flips intended state."""
    if any(a not in "ab" for a in word):
        raise ValueError("binary-symbol input required")
    if any(not math.isfinite(v) or not 0 <= v <= 1 for v in (error, loss)):
        raise ValueError("probabilities in [0,1] required")
    even, odd, lost = 1.0, 0.0, 0.0
    history = [(even, odd, lost)]
    for a in word:
        if a == "b":
            even, odd = odd, even
        even, odd, lost = (
            (1 - loss) * ((1 - error) * even + error * odd),
            (1 - loss) * ((1 - error) * odd + error * even),
            lost + loss * (even + odd),
        )
        history.append((even, odd, lost))
    return tuple(history)


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
        "syntactic_conflicts": prefix_conflicts(RULES),
        "expanded_rule_count": len(expand_rules(RULES)),
        "race_curve": [
            dict(
                time=t / 20,
                correct=race((0.6, 0.4), t / 20)[0][0],
                incorrect=race((0.6, 0.4), t / 20)[0][1],
                uncommitted=race((0.6, 0.4), t / 20)[1],
            )
            for t in range(101)
        ],
        "race": [
            dict(
                time=t,
                correct=round(race((0.6, 0.4), t)[0][0], 6),
                incorrect=round(race((0.6, 0.4), t)[0][1], 6),
                uncommitted=round(race((0.6, 0.4), t)[1], 6),
            )
            for t in (0, 0.5, 1, 2, 5)
        ],
        "parity": [
            dict(n=n, even=round(e, 6), odd=round(o, 6), lost=round(l, 6))
            for n, (e, o, l) in enumerate(
                parity_distribution("abba", 0.1, 0.05)
            )
        ],
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
