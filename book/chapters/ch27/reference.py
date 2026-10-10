"""DNAD-27: exact multiset transitions and honestly bounded graph exploration."""

from collections import deque
from dataclasses import dataclass
from collections.abc import Mapping
import json


def identifier(value):
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise ValueError("Nonempty stripped species/rule identity required")
    return value


def canon(value):
    """Canonical finite multiset; never truncate floats or silently merge duplicate IDs."""
    if isinstance(value, Mapping):
        pairs = list(value.items())
    elif isinstance(value, tuple):
        pairs = list(value)
    else:
        raise ValueError("Mapping or tuple of species/count pairs required")
    seen, out = set(), []
    for pair in pairs:
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise ValueError("Species/count pair required")
        name, count = pair
        identifier(name)
        if name in seen:
            raise ValueError("Duplicate species identity")
        seen.add(name)
        if type(count) is not int or count < 0:
            raise ValueError("Nonnegative exact integer count required")
        if count:
            out.append((name, count))
    return tuple(sorted(out))


@dataclass(frozen=True)
class Rule:
    name: str
    consume: tuple
    produce: tuple

    def __post_init__(self):
        identifier(self.name)
        if type(self.consume) is not tuple or type(self.produce) is not tuple:
            raise ValueError("Immutable canonical stoichiometric tuples required")
        if canon(self.consume) != self.consume or canon(self.produce) != self.produce:
            raise ValueError("Stoichiometry must be canonical")


def rule(name, consume, produce):
    return Rule(name, canon(consume), canon(produce))


@dataclass(frozen=True)
class Network:
    species: tuple
    rules: tuple

    def __post_init__(self):
        if type(self.species) is not tuple or not self.species:
            raise ValueError("Nonempty immutable species universe required")
        for name in self.species:
            identifier(name)
        if len(set(self.species)) != len(self.species):
            raise ValueError("Species universe identities must be unique")
        if type(self.rules) is not tuple or not all(
            isinstance(r, Rule) for r in self.rules
        ):
            raise ValueError("Immutable typed rule tuple required")
        if len({r.name for r in self.rules}) != len(self.rules):
            raise ValueError("Rule names must be unique")
        universe = set(self.species)
        for r in self.rules:
            if not {k for k, _ in r.consume + r.produce} <= universe:
                raise ValueError("Undeclared reaction species")


def network_state(value, network):
    if not isinstance(network, Network):
        raise ValueError("Typed network required")
    result = canon(value)
    if not {k for k, _ in result} <= set(network.species):
        raise ValueError("Undeclared state species")
    return result


def enabled(value, reaction):
    if not isinstance(reaction, Rule):
        raise ValueError("Typed rule required")
    counts = dict(canon(value))
    return all(counts.get(name, 0) >= amount for name, amount in reaction.consume)


def fire(value, reaction):
    """One atomic rewrite with exact stoichiometric precondition."""
    current = canon(value)
    if not enabled(current, reaction):
        raise ValueError("Rule not enabled")
    counts = dict(current)
    for name, amount in reaction.consume:
        counts[name] -= amount
    for name, amount in reaction.produce:
        counts[name] = counts.get(name, 0) + amount
    return canon(counts)


def successors(value, network):
    current = network_state(value, network)
    return tuple(
        (r.name, fire(current, r)) for r in network.rules if enabled(current, r)
    )


@dataclass
class Search:
    depth: dict
    predecessor: dict
    edges: tuple
    terminals: tuple
    max_steps: int
    complete_within_depth: bool
    exhaustive_closure: bool
    outside_successors: int | None
    status: str


def bounded_reachable(initial, network, max_steps, state_limit=10000):
    """BFS retains labeled edges; budgets never masquerade as completeness."""
    if type(max_steps) is not int or max_steps < 0:
        raise ValueError("Nonnegative integer depth bound required")
    if type(state_limit) is not int or state_limit < 1:
        raise ValueError("Positive integer state budget required")
    start = network_state(initial, network)
    depth, pred, queue = {start: 0}, {start: None}, deque([start])
    edges, terminals, boundary = [], [], []
    while queue:
        current = queue.popleft()
        next_states = successors(current, network)
        if not next_states:
            terminals.append(current)
        if depth[current] == max_steps:
            boundary.append(current)
            continue
        for label, target in next_states:
            if target not in depth:
                if len(depth) == state_limit:
                    return Search(
                        depth,
                        pred,
                        tuple(edges),
                        tuple(terminals),
                        max_steps,
                        False,
                        False,
                        None,
                        "state_budget_exhausted",
                    )
                depth[target] = depth[current] + 1
                pred[target] = (current, label)
                queue.append(target)
            edges.append((current, label, target))
    outside = {
        target
        for current in boundary
        for _, target in successors(current, network)
        if target not in depth
    }
    return Search(
        depth,
        pred,
        tuple(edges),
        tuple(terminals),
        max_steps,
        True,
        not outside,
        len(outside),
        "exhaustive_closure" if not outside else "depth_bounded",
    )


def witness(search, target):
    """Return shortest rule labels from recorded first-discovery predecessors."""
    current = canon(target)
    if current not in search.predecessor:
        raise ValueError("Target absent from explored states")
    path, seen = [], set()
    while search.predecessor[current] is not None:
        if current in seen:
            raise ValueError("Corrupt cyclic predecessor map")
        seen.add(current)
        current, label = search.predecessor[current]
        path.append(label)
    return tuple(reversed(path))


def weighted_total(value, weights):
    if not isinstance(weights, Mapping):
        raise ValueError("Explicit integer weight map required")
    current = canon(value)
    total = 0
    for name, count in current:
        if name not in weights or type(weights[name]) is not int:
            raise ValueError("Every present species needs an exact integer weight")
        total += weights[name] * count
    return total


def stoichiometry(network):
    """Rows follow declared species order, columns follow declared rule order."""
    return tuple(
        tuple(
            dict(r.produce).get(s, 0) - dict(r.consume).get(s, 0) for r in network.rules
        )
        for s in network.species
    )


def invariant_preserved(reaction, weights):
    return weighted_total(reaction.consume, weights) == weighted_total(
        reaction.produce, weights
    )


def assembly():
    return Network(
        ("A", "B", "C", "AB", "ABC"),
        (
            rule("bind_AB", {"A": 1, "B": 1}, {"AB": 1}),
            rule("bind_C", {"AB": 1, "C": 1}, {"ABC": 1}),
        ),
    )


def results():
    network = assembly()
    initial = {"A": 1, "B": 1, "C": 1}
    weights = {"A": 1, "B": 1, "C": 1, "AB": 2, "ABC": 3}
    trace = []
    for bound in (0, 1, 2, 3):
        search = bounded_reachable(initial, network, bound)
        trace.append(
            {
                "bound": bound,
                "states": len(search.depth),
                "edges": len(search.edges),
                "outside": search.outside_successors,
                "closure": int(search.exhaustive_closure),
            }
        )
    search = bounded_reachable(initial, network, 2)
    branch = Network(
        ("A", "B", "C", "AB", "AC", "ABC"),
        network.rules
        + (
            rule("bind_AC", {"A": 1, "C": 1}, {"AC": 1}),
            rule("bind_B", {"AC": 1, "B": 1}, {"ABC": 1}),
        ),
    )
    branching = bounded_reachable(initial, branch, 2)
    diverge = Network(
        ("A", "B", "C"),
        (rule("choose_B", {"A": 1}, {"B": 1}), rule("choose_C", {"A": 1}, {"C": 1})),
    )
    nonconfluent = bounded_reachable({"A": 1}, diverge, 1)
    capped = bounded_reachable(initial, branch, 2, state_limit=2)
    return {
        "trace": trace,
        "shortest_witness": witness(search, {"ABC": 1}),
        "all_weight_three": all(weighted_total(s, weights) == 3 for s in search.depth),
        "stoichiometric_rows": stoichiometry(network),
        "diamond_states": len(branching.depth),
        "diamond_edges": len(branching.edges),
        "divergent_terminals": len(nonconfluent.terminals),
        "budget_status": capped.status,
        "budget_complete": capped.complete_within_depth,
        "scope": "formal count reachability only; no time, probability, domain matching or wet lab",
    }


TABLES = [
    (
        "trace",
        ["Bound", "States", "Edges", "Outside", "Closure"],
        ["bound", "states", "edges", "outside", "closure"],
        "rrrrr",
    )
]
PLOTS = []
LISTINGS = ["canon", "fire", "bounded_reachable", "witness", "stoichiometry"]

if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
