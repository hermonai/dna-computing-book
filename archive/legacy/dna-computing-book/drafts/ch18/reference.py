"""An executable tape model and explicit reliability accounting."""

import json
import math

LISTINGS = ["run", "stack_step", "reliability"]
TABLES = [
    (
        "trace",
        ["Step", "Head", "Read", "Write", "Next"],
        ["step", "head", "read", "write", "next"],
        "rrlll",
    ),
    (
        "growth",
        ["Width", "Steps", "Tape span"],
        ["n", "steps", "span"],
        "rrr",
    ),
]
PLOTS = [
    ("growth-plot", "growth", "n", ["steps", "span"]),
    ("reliability-plot", "reliability", "events", ["independent", "union"]),
]
INCREMENT = {
    ("carry", "1"): ("carry", "0", 1),
    ("carry", "0"): ("halt", "1", 0),
    ("carry", "_"): ("halt", "1", 0),
}


def validate_program(program):
    for key, value in program.items():
        if not isinstance(key, tuple) or len(key) != 2:
            raise ValueError("state-symbol keys required")
        if not isinstance(value, tuple) or len(value) != 3:
            raise ValueError("next-state, write, move triples required")
        q, read = key
        nxt, write, move = value
        if not all(isinstance(s, str) and s for s in (q, nxt)):
            raise ValueError("named states required")
        if read not in ("0", "1", "_") or write not in ("0", "1", "_"):
            raise ValueError("binary tape alphabet required")
        if type(move) is not int or move not in (-1, 0, 1):
            raise ValueError("unit head move required")
        if q == "halt":
            raise ValueError("halt has no outgoing transitions")


def run(program, word, fuel):
    """Input is left-to-right tape contents, least-significant bit first."""
    validate_program(program)
    if not isinstance(word, str) or any(b not in "01" for b in word):
        raise ValueError("binary input required")
    if type(fuel) is not int or fuel < 0:
        raise ValueError("nonnegative integer fuel required")
    tape = dict(enumerate(word))
    head, state, trace = 0, "carry", []
    low, high = 0, max(0, len(word) - 1)
    for step in range(fuel):
        read = tape.get(head, "_")
        if (state, read) not in program:
            return "stuck", tape, trace, high - low + 1
        nxt, write, move = program[state, read]
        if write == "_":
            tape.pop(head, None)
        else:
            tape[head] = write
        trace.append(
            dict(step=step + 1, head=head, read=read, write=write, next=nxt)
        )
        head, state = head + move, nxt
        low, high = min(low, head), max(high, head)
        if state == "halt":
            return "halt", tape, trace, high - low + 1
    return "exhausted", tape, trace, high - low + 1


def stack_step(left, right, state, program):
    """Stack tops are list ends; right top is the current tape cell."""
    read = right[-1] if right else "_"
    nxt, write, move = program[state, read]
    if right:
        right.pop()
    right.append(write)
    if move == 1:
        left.append(right.pop())
    elif move == -1:
        right.append(left.pop() if left else "_")
    return nxt, read, write, move


def two_stack(program, word, fuel):
    """Independent tape representation; return the same observable contract."""
    validate_program(program)
    if not isinstance(word, str) or any(b not in "01" for b in word):
        raise ValueError("binary input required")
    if type(fuel) is not int or fuel < 0:
        raise ValueError("nonnegative integer fuel required")
    left, right = [], list(reversed(word))
    head, state, trace, status = 0, "carry", [], "exhausted"
    low, high = 0, max(0, len(word) - 1)
    for step in range(fuel):
        read = right[-1] if right else "_"
        if (state, read) not in program:
            status = "stuck"
            break
        state, read, write, move = stack_step(left, right, state, program)
        trace.append(
            dict(
                step=step + 1, head=head, read=read, write=write, next=state
            )
        )
        head += move
        low, high = min(low, head), max(high, head)
        if state == "halt":
            status = "halt"
            break
    tape = {
        head - 1 - i: b for i, b in enumerate(reversed(left)) if b != "_"
    }
    tape.update(
        {head + i: b for i, b in enumerate(reversed(right)) if b != "_"}
    )
    return status, tape, trace, high - low + 1


def reliability(events, error):
    """Independent no-error probability and marginal-error union lower bound."""
    if type(events) is not int or events < 0:
        raise ValueError("nonnegative event count required")
    if not math.isfinite(error) or not 0 <= error <= 1:
        raise ValueError("probability required")
    independent = (
        1.0
        if events == 0
        else 0.0
        if error == 1
        else math.exp(events * math.log1p(-error))
    )
    return independent, max(0.0, 1 - events * error)


def results():
    _, _, trace, _ = run(INCREMENT, "111", 4)
    return {
        "trace": trace,
        "growth": [
            dict(
                n=n,
                steps=len(run(INCREMENT, "1" * n, n + 1)[2]),
                span=run(INCREMENT, "1" * n, n + 1)[3],
            )
            for n in range(1, 13)
        ],
        "reliability": [
            dict(
                events=t,
                independent=reliability(t, 0.001)[0],
                union=reliability(t, 0.001)[1],
            )
            for t in range(0, 2001, 100)
        ],
    }


if __name__ == "__main__":
    print(json.dumps(results(), indent=2))
