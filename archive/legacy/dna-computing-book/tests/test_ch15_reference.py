from pathlib import Path
import importlib.util
import json
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna_computing_book_ch15", ROOT / "drafts/ch15/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_committed_results_match_execution():
    assert m.results() == json.loads(
        (ROOT / "drafts/ch15/results.json").read_text()
    )


def test_all_context_cuts_and_length_conservation():
    from itertools import product

    words = ["".join(w) for n in range(4) for w in product("AB", repeat=n)]
    for x in words:
        for y in words:
            for rule in [
                ("", "", "", ""),
                ("A", "B", "B", "A"),
                ("", "A", "B", ""),
            ]:
                got = m.splice(x, y, rule)
                expected = []
                for i in range(len(x) + 1):
                    for j in range(len(y) + 1):
                        a, b, c, d = rule
                        if (
                            x[:i].endswith(a)
                            and x[i:].startswith(b)
                            and y[:j].endswith(c)
                            and y[j:].startswith(d)
                        ):
                            expected.append(
                                (i, j, x[:i] + y[j:], y[:j] + x[i:])
                            )
                assert got == expected
                assert all(
                    len(u) + len(v) == len(x) + len(y) for _, _, u, v in got
                )


def test_overlap_is_not_lost():
    assert m.cuts("AAA", "A", "A") == [1, 2]
    assert m.edits("AAA", "A", "X", "A") == ["AAXA", "AXAA"]


def test_reaction_counts_and_failure_atomicity():
    from collections import Counter

    pool = Counter({"LABR": 3, "MCDN": 2})
    old = pool.copy()
    out = m.react(pool, "LABR", "MCDN", ("A", "B", "C", "D"), 2, 2)
    assert pool == old and sum(out.values()) == 5
    assert out == Counter({"LABR": 2, "MCDN": 1, "LADN": 1, "MCBR": 1})
    assert sum(len(w) * n for w, n in out.items()) == sum(
        len(w) * n for w, n in pool.items()
    )
    with pytest.raises(ValueError):
        m.react(Counter({"AA": 1}), "AA", "AA", ("A", "A", "A", "A"), 1, 1)


def test_edits_and_search_caps():
    assert m.edits("AXB", "A", "X", "B", True) == ["AB"]
    assert m.edits("AB", "A", "X", "B") == ["AXB"]
    rules = [("", "0", "", False), ("", "1", "", False)]
    words, layers, closed = m.explore("", rules, 5)
    assert layers == [2 ** (n + 1) - 1 for n in range(6)]
    assert len(words) == 63 and not closed
    assert m.explore("AB", [("X", "0", "Y", False)], 8) == (
        ["AB"],
        [1],
        True,
    )
    with pytest.raises(ValueError):
        m.explore("", rules, 5, max_words=10)
    with pytest.raises(ValueError):
        m.edits("AB", "A", "", "B")
    with pytest.raises(ValueError):
        m.explore("", rules, -1)


def test_insert_delete_inverse_relation():
    from itertools import product

    for n in range(5):
        for word in map("".join, product("AB", repeat=n)):
            for changed in m.edits(word, "A", "X", "B"):
                assert word in m.edits(changed, "A", "X", "B", True)
