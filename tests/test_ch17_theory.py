"""Independent finite checks for the expanded, separately preserved edition."""

from itertools import product
from pathlib import Path
import importlib.util
import json
import math

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "drafts/ch17-theory"
spec = importlib.util.spec_from_file_location(
    "ch17_theory", HERE / "reference.py"
)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def words(maximum):
    for n in range(maximum + 1):
        yield from ("".join(w) for w in product("ab", repeat=n))


def test_generated_results():
    assert m.results() == json.loads((HERE / "results.json").read_text())


def test_equal_blocks_and_normalization_through_nine():
    expanded = m.expand_rules(m.RULES)
    assert len(expanded) == 7
    assert all(len(u) + len(v) == 1 for _, u, v, _ in expanded)
    assert m.prefix_conflicts(m.RULES) == []
    for w in words(9):
        oracle = w == "a" * (len(w) // 2) + "b" * (len(w) // 2)
        for rules in (m.RULES, expanded):
            ok, path, visited = m.paired_run(w, w, rules)
            assert ok == oracle
            q = {r[i] for r in rules for i in (0, 3)}
            assert visited <= len(q) * (len(w) + 1) ** 2
            if ok:
                assert path[-1][1:] == (len(w), len(w))
                assert len(path) - 1 <= 2 * len(w)


def test_private_paths_preserve_pair_acceptance_with_nonidentity_relation():
    rules = (
        ("s", "ab", "ba", "f"),
        ("s", "a", "", "t"),
        ("t", "b", "ab", "f"),
        ("f", "", "a", "f"),
    )
    reserved = {"private0", "private2", "isolated_final"}
    expanded = m.expand_rules(rules, reserved)
    originals = {r[i] for r in rules for i in (0, 3)}
    introduced = {r[i] for r in expanded for i in (0, 3)} - originals
    assert not introduced & reserved
    assert len(introduced) == sum(
        len(x) + len(y) - 1 for _, x, y, _ in rules
    )
    rho = frozenset(product("ab", repeat=2))
    for n in range(5):
        for u in product("ab", repeat=n):
            for v in product("ab", repeat=n):
                args = ("".join(u), "".join(v))
                before = m.paired_run(*args, rules, rho, "s", {"f"})[0]
                after = m.paired_run(*args, expanded, rho, "s", {"f"})[0]
                assert before == after


def test_normalization_does_not_preserve_syntactic_determinism():
    rules = (("s", "a", "b", "f"), ("s", "a", "a", "g"))
    assert m.prefix_conflicts(rules) == []
    assert m.prefix_conflicts(m.expand_rules(rules)) == [(0, 2)]


def test_syntactic_conflict_is_not_necessarily_reachable():
    rules = m.RULES + (("z", "a", "a", "z"), ("z", "aa", "aa", "z"))
    assert m.prefix_conflicts(rules) == [(5, 6)]
    for w in words(6):
        assert m.paired_run(w, w, rules)[0] == m.paired_run(w, w)[0]
    assert m.prefix_conflicts(
        (("s", "a", "a", "f"), ("s", "ab", "ab", "g"))
    ) == [(0, 1)]


@pytest.mark.parametrize("function", [m.expand_rules, m.prefix_conflicts])
def test_nonadvancing_rules_not_silently_normalized(function):
    with pytest.raises(ValueError):
        function((("s", "", "", "s"),))


@pytest.mark.parametrize(
    "rates", [(0, 0), (0.6, 0.4), (0, 2), (1e-12, 3e-12), (1e6, 1)]
)
@pytest.mark.parametrize("time", [0, 1e-8, 1, 10, 1e6])
def test_race_probability_mass_and_scaling(rates, time):
    out, pending = m.race(rates, time)
    assert all(0 <= p <= 1 for p in (*out, pending))
    assert math.fsum(out) + pending == pytest.approx(1)
    scaled = m.race(tuple(r * 10 for r in rates), time / 10)
    assert scaled[0] == pytest.approx(out)
    assert scaled[1] == pytest.approx(pending)
    if sum(rates) and time:
        assert out == pytest.approx(
            tuple(
                r / sum(rates) * (-math.expm1(-sum(rates) * time))
                for r in rates
            )
        )


@pytest.mark.parametrize(
    "rates,time",
    [
        ([], 1),
        ((-1, 2), 1),
        ((math.nan,), 1),
        ((math.inf,), 1),
        ((1,), -1),
        ((1,), math.nan),
    ],
)
def test_race_invalid_parameters(rates, time):
    with pytest.raises(ValueError):
        m.race(rates, time)


@pytest.mark.parametrize(
    "b,d,c",
    [
        ((1, 1), (0, 3), (1, 1)),
        ((0.2, 0.8), (3, 6), (1, 4)),
        ((1, 0), (2, 0), (3, 0)),
        ((1, 2), (1, 3), (0, 4)),
    ],
)
def test_renewal_formula_against_transient_generator(b, d, c):
    # Independent absorption calculation on states F,C1,...,Ck:
    # -Q t = 1 and -Q H = R, with unreachable zero-rate traps omitted.
    active = [i for i, br in enumerate(b) if br]
    q = np.zeros((len(active) + 1, len(active) + 1))
    r = np.zeros((len(active) + 1, len(b)))
    q[0, 0] = -sum(b)
    for j, i in enumerate(active, 1):
        q[0, j] = b[i]
        q[j, 0] = d[i]
        q[j, j] = -d[i] - c[i]
        r[j, i] = c[i]
    p, mean = m.encounter_statistics(b, d, c)
    assert p == pytest.approx(np.linalg.solve(-q, r)[0])
    assert mean == pytest.approx(np.linalg.solve(-q, np.ones(len(q)))[0])
    if b == (1, 1):
        assert p == pytest.approx((0.8, 0.2))
        assert mean == pytest.approx(1.8)


@pytest.mark.parametrize(
    "b,d,c",
    [
        ((), (), ()),
        ((1,), (), (1,)),
        ((1,), (0,), (0,)),
        ((0,), (1,), (1,)),
        ((1,), (1,), (0,)),
        ((-1,), (1,), (1,)),
    ],
)
def test_renewal_invalid_or_noncommitting_model(b, d, c):
    with pytest.raises(ValueError):
        m.encounter_statistics(b, d, c)


def enumerated_parity(word, error, loss):
    # Enumerate independent per-symbol events; absorption makes later events irrelevant.
    masses = [0.0, 0.0, 0.0]
    probabilities = ((1 - loss) * (1 - error), (1 - loss) * error, loss)
    for events in product(range(3), repeat=len(word)):
        mass = math.prod(probabilities[e] for e in events)
        state = 0
        for symbol, event in zip(word, events):
            if state == 2:
                continue
            if event == 2:
                state = 2
            else:
                state ^= (symbol == "b") ^ (event == 1)
        masses[state] += mass
    return masses


@pytest.mark.parametrize("error", [0, 0.1, 0.5, 1])
@pytest.mark.parametrize("loss", [0, 0.05, 1])
def test_parity_closed_form_and_exhaustive_histories(error, loss):
    for w in words(4):
        row = m.parity_distribution(w, error, loss)[-1]
        assert row == pytest.approx(enumerated_parity(w, error, loss))
    for n in range(9):
        w = ("abba" * 3)[:n]
        row = m.parity_distribution(w, error, loss)[-1]
        correct = w.count("b") % 2
        assert sum(row) == pytest.approx(1)
        assert row[2] == pytest.approx(1 - (1 - loss) ** n)
        assert row[correct] == pytest.approx(
            (1 - loss) ** n * (1 + (1 - 2 * error) ** n) / 2
        )


@pytest.mark.parametrize(
    "word,error,loss",
    [("c", 0, 0), ("a", -0.1, 0), ("", math.nan, 0), ("b", 0, 1.1)],
)
def test_invalid_parity_parameters(word, error, loss):
    with pytest.raises(ValueError):
        m.parity_distribution(word, error, loss)


def test_worked_parity_answer():
    assert m.parity_distribution("abba", 0.1, 0.05)[-1][0] == pytest.approx(
        0.574064005
    )
