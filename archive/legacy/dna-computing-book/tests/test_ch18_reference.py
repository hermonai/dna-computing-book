from pathlib import Path
import importlib.util
import json
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna_computing_book_ch18", ROOT / "drafts/ch18/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_results_are_reproducible():
    assert m.results() == json.loads(
        (ROOT / "drafts/ch18/results.json").read_text()
    )


from itertools import product
import math


@pytest.mark.parametrize("width", range(10))
def test_increment_exhaustive(width):
    for parts in product("01", repeat=width):
        word = "".join(parts)
        status, tape, trace, span = m.run(m.INCREMENT, word, width + 1)
        assert status == "halt"
        value = sum(int(b) * 2**i for i, b in tape.items())
        before = sum(int(b) * 2**i for i, b in enumerate(word))
        assert value == before + 1
        ones = len(word) - len(word.lstrip("1"))
        assert len(trace) == ones + 1
        assert span == max(1, width, ones + 1)


def test_budget_stuck_and_negative_head():
    assert m.run(m.INCREMENT, "111", 3)[0] == "exhausted"
    assert m.run(m.INCREMENT, "111", 4)[0] == "halt"
    assert m.run({}, "0", 1)[0] == "stuck"
    loop = {("carry", "0"): ("carry", "0", 0)}
    assert m.run(loop, "0", 10)[0] == "exhausted"
    left = {
        ("carry", "0"): ("next", "0", -1),
        ("next", "_"): ("halt", "1", 0),
    }
    status, tape, _, span = m.run(left, "0", 2)
    assert status == "halt" and tape[-1] == "1" and span == 2


def test_two_stack_simulation_random_programs():
    import random

    rng = random.Random(1801)
    for _ in range(500):
        program = {
            (q, s): (
                rng.choice(("carry", "q", "halt")),
                rng.choice("01_"),
                rng.choice((-1, 0, 1)),
            )
            for q in ("carry", "q")
            for s in "01_"
            if rng.random() < 0.8
        }
        word = "".join(rng.choice("01") for _ in range(rng.randrange(6)))
        fuel = rng.randrange(20)
        assert m.two_stack(program, word, fuel) == m.run(
            program, word, fuel
        )


@pytest.mark.parametrize("t", [0, 1, 2, 100, 1000])
@pytest.mark.parametrize("e", [0, 0.001, 0.5, 1])
def test_probability_oracles(t, e):
    independent, union = m.reliability(t, e)
    assert independent == pytest.approx((1 - e) ** t)
    assert 0 <= union <= independent + 1e-12 <= 1 + 1e-12


def test_validation_and_input_ownership():
    original = dict(m.INCREMENT)
    m.run(original, "10", 2)
    assert original == m.INCREMENT
    for fuel in (-1, True):
        with pytest.raises(ValueError):
            m.run(original, "", fuel)
    for word in ("N", "10 "):
        with pytest.raises(ValueError):
            m.run(original, word, 4)
    with pytest.raises(ValueError):
        m.run({("halt", "0"): ("halt", "1", 0)}, "0", 1)
    with pytest.raises(ValueError):
        m.reliability(1, math.nan)
    with pytest.raises(ValueError):
        m.run({("carry", "0"): ("halt", "1", True)}, "0", 1)
