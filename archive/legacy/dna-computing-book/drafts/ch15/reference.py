"""Original symbolic rewriting models. No laboratory kinetics."""

from collections import Counter
import json

LISTINGS = ["cuts", "splice", "react", "edits", "explore"]


def cuts(word, left, right):
    """Every boundary with the specified adjacent contexts, overlaps included."""
    return [
        i
        for i in range(len(word) + 1)
        if word[:i].endswith(left) and word[i:].startswith(right)
    ]


def splice(x, y, rule):
    """Return both products for every compatible pair of symbolic cuts."""
    a, b, c, d = rule
    return [
        (i, j, x[:i] + y[j:], y[:j] + x[i:])
        for i in cuts(x, a, b)
        for j in cuts(y, c, d)
    ]


def react(pool, x, y, rule, i, j):
    """Consume two parent copies and return two products; failure changes nothing."""
    if any(type(n) is not int or n < 0 for n in pool.values()):
        raise ValueError("nonnegative integer counts required")
    if i not in cuts(x, *rule[:2]) or j not in cuts(y, *rule[2:]):
        raise ValueError("inapplicable cut")
    need = Counter([x, y])
    if any(pool.get(w, 0) < n for w, n in need.items()):
        raise ValueError("insufficient parent copies")
    out = Counter(pool)
    out.subtract(need)
    out.update([x[:i] + y[j:], y[:j] + x[i:]])
    return +out


def edits(word, left, payload, right, delete=False):
    """Single local insertion or deletion, with preserved adjacent contexts."""
    if not payload:
        raise ValueError("nonempty payload required")
    if type(delete) is not bool:
        raise ValueError("explicit Boolean mode required")
    if not delete:
        return sorted(
            {word[:i] + payload + word[i:] for i in cuts(word, left, right)}
        )
    return sorted(
        {
            word[:i] + word[i + len(payload) :]
            for i in range(len(word) - len(payload) + 1)
            if word[:i].endswith(left)
            and word[i:].startswith(payload + right)
        }
    )


def explore(seed, rules, depth, max_words=10000):
    """Breadth-first unary edit closure; capped search is explicitly incomplete."""
    if type(depth) is not int or depth < 0:
        raise ValueError("nonnegative integer depth required")
    if type(max_words) is not int or max_words < 1:
        raise ValueError("positive word cap required")
    seen, frontier = {seed}, {seed}
    layers = [1]
    for _ in range(depth):
        nxt = {
            v for w in frontier for rule in rules for v in edits(w, *rule)
        } - seen
        if len(seen | nxt) > max_words:
            raise ValueError("word budget exceeded; no closure certificate")
        if not nxt:
            return sorted(seen), layers, True
        seen |= nxt
        frontier = nxt
        layers.append(len(seen))
    # An extra expansion decides whether this finite set is actually closed.
    closed = all(
        v in seen
        for w in frontier
        for rule in rules
        for v in edits(w, *rule)
    )
    return sorted(seen), layers, closed


def results():
    parents = ("LABR", "MCDN")
    products = splice(*parents, ("A", "B", "C", "D"))
    words, layers, closed = explore(
        "", [("", "0", "", False), ("", "1", "", False)], 5
    )
    return {
        "products": [list(v) for v in products],
        "after_reaction": dict(
            react(Counter(parents), *parents, ("A", "B", "C", "D"), 2, 2)
        ),
        "growth": [{"depth": i, "words": n} for i, n in enumerate(layers)],
        "closed": closed,
        "word_count": len(words),
        "insert": edits("ABAB", "A", "X", "B"),
        "delete": edits("AXB", "A", "X", "B", True),
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
