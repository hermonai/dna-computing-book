"""Exact automata, transduction and an explicitly assigned noise channel."""

import itertools
import json
import math

LISTINGS = ["recognize", "add_bits", "noisy_distribution"]
# States: 0 no useful suffix, 1 suffix 0, 2 suffix 01.
DELTA = ((1, 0), (1, 2), (1, 0))


def bits(word):
    if not isinstance(word, str) or any(c not in "01" for c in word):
        raise ValueError("binary word required")
    return [int(c) for c in word]


def recognize(word):
    state, trace = 0, [0]
    for symbol in bits(word):
        state = DELTA[state][symbol]
        trace.append(state)
    return state == 2, trace


def add_bits(x, y):
    """Equal-width least-significant-bit-first inputs, with final carry retained."""
    a, b = bits(x), bits(y)
    if len(a) != len(b):
        raise ValueError("equal widths required")
    carry, output, trace = 0, [], []
    for i, (u, v) in enumerate(zip(a, b)):
        total = u + v + carry
        digit, nxt = total % 2, total // 2
        trace.append([i, u, v, carry, digit, nxt])
        output.append(str(digit))
        carry = nxt
    output.append(str(carry))
    return "".join(output), trace


def noisy_distribution(word, error, loss):
    """Wrong next state is uniform over the other two states; loss is absorbing."""
    symbols = bits(word)
    if any(not math.isfinite(p) or not 0 <= p <= 1 for p in (error, loss)):
        raise ValueError("probabilities must lie in [0,1]")
    state = [1.0, 0.0, 0.0, 0.0]
    for a in symbols:
        nxt = [0.0, 0.0, 0.0, state[3]]
        for q in range(3):
            nxt[3] += loss * state[q]
            for dest in range(3):
                probability = (
                    1 - error if dest == DELTA[q][a] else error / 2
                )
                nxt[dest] += (1 - loss) * state[q] * probability
        state = nxt
    return state


def results():
    accepted, trace = recognize("1101")
    output, addition = add_bits("1011", "1100")
    return {
        "recognition": [
            {"prefix": "1101"[:i] or "empty", "state": q}
            for i, q in enumerate(trace)
        ],
        "accepted": accepted,
        "addition": addition,
        "sum_lsb": output,
        "noise": [
            {
                "length": n,
                "accept": noisy_distribution(
                    "0" * (n - 1) + "1", 0.02, 0.01
                )[2],
                "lost": noisy_distribution("0" * (n - 1) + "1", 0.02, 0.01)[
                    3
                ],
            }
            for n in range(2, 51)
        ],
        "example_noise": noisy_distribution("1101", 0.02, 0.01),
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
