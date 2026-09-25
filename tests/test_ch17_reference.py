from pathlib import Path
import importlib.util
import json
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "dna_computing_book_ch17", ROOT / "drafts/ch17/reference.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


def test_results_are_reproducible():
    assert m.results() == json.loads(
        (ROOT / "drafts/ch17/results.json").read_text()
    )


from itertools import product


def oracle(word):
    n = len(word) // 2
    return word == "a" * n + "b" * n


def test_all_binary_words_through_nine():
    for n in range(10):
        for letters in product("ab", repeat=n):
            word = "".join(letters)
            ok, path, visited = m.paired_run(word, word)
            assert ok == oracle(word)
            assert visited <= 3 * (n + 1) ** 2
            if ok:
                assert path[0] == ("seek", 0, 0)
                assert path[-1][1:] == (n, n)
                for a, b in zip(path, path[1:]):
                    assert b[1] + b[2] > a[1] + a[2]
                    assert any(
                        q == a[0]
                        and target == b[0]
                        and a[1] + len(u) == b[1]
                        and a[2] + len(v) == b[2]
                        and word[a[1] : b[1]] == u
                        and word[a[2] : b[2]] == v
                        for q, u, v, target in m.RULES
                    )


def test_trace_and_rule_order():
    ok, path, _ = m.paired_run("aabb", "aabb")
    assert ok
    assert path == [
        ("seek", 0, 0),
        ("seek", 0, 1),
        ("seek", 0, 2),
        ("pair", 1, 3),
        ("pair", 2, 4),
        ("drain", 3, 4),
        ("drain", 4, 4),
    ]
    assert m.paired_run("aabb", "aabb", rules=m.RULES[::-1])[0]


def test_noninjective_witness_and_incomplete_input():
    rho = frozenset({("a", "x"), ("x", "a"), ("a", "y"), ("y", "a")})
    rules = (("s", "a", "y", "f"),)
    witnesses = list(m.lower_words("aa", rho))
    assert witnesses == ["xx", "xy", "yx", "yy"]
    assert not m.paired_run("a", "x", rules, rho, "s", {"f"})[0]
    assert m.paired_run("a", "y", rules, rho, "s", {"f"})[0]
    assert not m.paired_run("aa", "yy", rules, rho, "s", {"f"})[0]
    assert list(m.lower_words("", rho)) == [""]


@pytest.mark.parametrize("u,v", [("a", "b"), ("a", ""), ("c", "c")])
def test_invalid_pair(u, v):
    with pytest.raises(ValueError):
        m.paired_run(u, v)


def test_nonadvancing_rules_rejected_and_dead_end_is_rejection():
    with pytest.raises(ValueError):
        m.paired_run("", "", rules=(("s", "", "", "s"),))
    assert not m.paired_run("ab", "ab", rules=())[0]
